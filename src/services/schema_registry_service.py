import logging
import json
import time
import threading
from typing import Dict, Optional, Tuple, Any
import requests

from src.config.config_loader import (
    get_schema_registry_url,
    get_schema_registry_timeout,
    is_feature_enabled,
)

logger = logging.getLogger(__name__)


class TTLCache:
    def __init__(self, ttl_seconds: int = 3600):
        self._cache: Dict[str, Tuple[Any, float]] = {}
        self._ttl = ttl_seconds
        self._lock = threading.Lock()
        self._last_cleanup = time.time()
        self._cleanup_interval = 300  # Очистка каждые 5 минут

    def get(self, key: str) -> Optional[Any]:
        with self._lock:
            self._auto_cleanup()

            if key not in self._cache:
                return None

            value, expiration_time = self._cache[key]
            if time.time() > expiration_time:
                del self._cache[key]
                logger.debug(f"Cache entry expired on access: {key}")
                return None

            return value

    def set(self, key: str, value: Any) -> None:
        with self._lock:
            expiration_time = time.time() + self._ttl
            self._cache[key] = (value, expiration_time)

    def clear(self) -> None:
        with self._lock:
            self._cache.clear()
            logger.debug("Cache cleared")

    def _auto_cleanup(self) -> None:
        now = time.time()
        if now - self._last_cleanup < self._cleanup_interval:
            return

        expired_keys = [
            key for key, (_, exp_time) in self._cache.items() if now > exp_time
        ]

        for key in expired_keys:
            del self._cache[key]

        self._last_cleanup = now

        if expired_keys:
            logger.debug(f"Auto-cleanup removed {len(expired_keys)} expired entries")

    def cleanup_expired(self) -> int:
        with self._lock:
            now = time.time()
            expired_keys = [
                key for key, (_, exp_time) in self._cache.items() if now > exp_time
            ]

            for key in expired_keys:
                del self._cache[key]

            self._last_cleanup = now
            return len(expired_keys)

    def get_stats(self) -> dict:
        with self._lock:
            now = time.time()
            total = len(self._cache)
            expired = sum(
                1 for _, (_, exp_time) in self._cache.items() if now > exp_time
            )
            return {
                "total_entries": total,
                "expired_entries": expired,
                "active_entries": total - expired,
                "ttl_seconds": self._ttl,
            }


class SchemaRegistryService:
    def __init__(self, cache_ttl_seconds: int = 3600):
        self.enabled = is_feature_enabled("use_schema_registry")

        # ВСЕГДА инициализируем поля
        self.url = get_schema_registry_url()
        self.timeout = get_schema_registry_timeout()
        self._schema_cache = TTLCache(ttl_seconds=cache_ttl_seconds)
        self._named_schemas_cache = TTLCache(ttl_seconds=cache_ttl_seconds)

        if not self.enabled:
            logger.info("Schema Registry disabled by feature flag")
        else:
            logger.info(f"✅ Schema Registry initialized: {self.url}")
            logger.info(f"Cache TTL: {cache_ttl_seconds} seconds")

    def get_schema_metadata(self, subject: str, version: str = "latest") -> dict:
        if not self.enabled:
            raise RuntimeError("Schema Registry is disabled")

        cache_key = f"{subject}:{version}"
        cached = self._schema_cache.get(cache_key)
        if cached is not None:
            logger.debug(f"Cache HIT for schema metadata: {cache_key}")
            return cached

        try:
            url = f"{self.url}/subjects/{subject}/versions/{version}"
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            metadata = response.json()

            self._schema_cache.set(cache_key, metadata)
            logger.debug(
                f"Cache MISS for schema metadata: {cache_key}, "
                f"version={metadata['version']}, id={metadata['id']}"
            )
            return metadata
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to get schema for {subject}: {e}")
            raise

    def get_schema_with_references(self, subject: str) -> Tuple[dict, dict]:
        if not self.enabled:
            raise RuntimeError("Schema Registry is disabled")

        cache_key = f"schema_with_refs:{subject}"
        cached = self._schema_cache.get(cache_key)
        if cached is not None:
            schema_cached, named_schemas_cached = cached
            logger.info(
                f"[DEBUG] Cache HIT for schema with references: {subject}, "
                f"named_schemas keys: {list(named_schemas_cached.keys())}"
            )
            return cached

        try:
            metadata = self.get_schema_metadata(subject)
            schema_str = metadata["schema"]
            main_schema = json.loads(schema_str)
            references = metadata.get("references", [])

            logger.info(f"[DEBUG] References for {subject}: {references}")

            named_schemas: Dict[str, dict] = {}

            if references:
                logger.info(
                    f"[DEBUG] Loading {len(references)} references for {subject}"
                )
                for ref in references:
                    ref_subject = ref["subject"]
                    ref_name = ref["name"]

                    cached_ref = self._named_schemas_cache.get(ref_name)
                    if cached_ref is not None:
                        named_schemas[ref_name] = cached_ref
                        logger.info(f"[DEBUG] Cache HIT for reference: {ref_name}")
                        continue

                    ref_metadata = self.get_schema_metadata(ref_subject)
                    ref_schema = json.loads(ref_metadata["schema"])
                    self._named_schemas_cache.set(ref_name, ref_schema)
                    named_schemas[ref_name] = ref_schema
                    logger.info(f"[DEBUG] Loaded reference: {ref_name}")

            result = (main_schema, named_schemas)
            self._schema_cache.set(cache_key, result)

            logger.info(
                f"[DEBUG] Final named_schemas keys for {subject}: {list(named_schemas.keys())}"
            )
            logger.info(
                f"✅ Loaded schema for {subject} with "
                f"{len(references)} references (id={metadata['id']})"
            )
            return result
        except Exception as e:
            logger.error(f"Failed to load schema with references for {subject}: {e}")
            raise

    def clear_cache(self) -> None:
        self._schema_cache.clear()
        self._named_schemas_cache.clear()
        logger.info("Cache cleared")

    def cleanup_expired_cache(self) -> int:
        expired_schemas = self._schema_cache.cleanup_expired()
        expired_named = self._named_schemas_cache.cleanup_expired()
        total = expired_schemas + expired_named
        if total > 0:
            logger.info(f"Cleaned up {total} expired cache entries")
        return total

    def get_cache_stats(self) -> dict:
        return {
            "schemas": self._schema_cache.get_stats(),
            "named_schemas": self._named_schemas_cache.get_stats(),
        }

    def register_schema(self, subject: str, schema: dict) -> Optional[int]:
        if not self.enabled:
            logger.debug("Schema Registry disabled, skipping registration")
            return None

        try:
            url = f"{self.url}/subjects/{subject}/versions"
            payload = {"schema": json.dumps(schema)}
            response = requests.post(
                url,
                json=payload,
                timeout=self.timeout,
                headers={"Content-Type": "application/vnd.schemaregistry.v1+json"},
            )
            response.raise_for_status()
            schema_id = response.json().get("id")

            self.clear_cache()
            logger.info(f"✅ Schema registered: subject={subject}, id={schema_id}")
            return schema_id
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to register schema for {subject}: {e}")
            raise


schema_registry_service = SchemaRegistryService(cache_ttl_seconds=3600)
