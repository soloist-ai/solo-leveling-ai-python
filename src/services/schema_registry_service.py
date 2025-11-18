import logging
import json
import threading
from typing import Dict, Optional, Tuple, Any
import requests
from cachetools import TTLCache

from src.config.config_loader import (
    get_schema_registry_url,
    get_schema_registry_timeout,
    is_feature_enabled,
)

logger = logging.getLogger(__name__)


class SchemaRegistryService:
    """Service for managing schema registry operations with TTL caching"""

    def __init__(self, cache_ttl_seconds: int = 3600, max_cache_size: int = 256):
        self.enabled = is_feature_enabled("use_schema_registry")
        self.url = get_schema_registry_url()
        self.timeout = get_schema_registry_timeout()
        self._cache_lock = threading.RLock()
        self._metadata_cache: TTLCache[str, Dict[str, Any]] = TTLCache(
            maxsize=max_cache_size, ttl=cache_ttl_seconds
        )
        self._schema_with_refs_cache: TTLCache[
            str, Tuple[Dict[str, Any], Dict[str, Dict[str, Any]]]
        ] = TTLCache(maxsize=max_cache_size, ttl=cache_ttl_seconds)
        self._named_schemas_cache: TTLCache[str, Dict[str, Any]] = TTLCache(
            maxsize=max_cache_size * 2, ttl=cache_ttl_seconds
        )

        if not self.enabled:
            logger.info("Schema Registry disabled by feature flag")
        else:
            logger.info(f"Schema Registry initialized: {self.url}")
            logger.info(
                f"Cache TTL: {cache_ttl_seconds} seconds, Max size: {max_cache_size}"
            )

    def get_schema_metadata(
        self, subject: str, version: str = "latest"
    ) -> Dict[str, Any]:
        """Get schema metadata with caching"""
        if not self.enabled:
            raise RuntimeError("Schema Registry is disabled")

        cache_key = f"{subject}:{version}"
        with self._cache_lock:
            cached = self._metadata_cache.get(cache_key)
            if cached is not None:
                logger.debug(f"Cache HIT for schema metadata: {cache_key}")
                return cached

        try:
            url = f"{self.url}/subjects/{subject}/versions/{version}"
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            metadata = response.json()

            with self._cache_lock:
                self._metadata_cache[cache_key] = metadata

            logger.debug(
                f"Cache MISS for schema metadata: {cache_key}, "
                f"version={metadata['version']}, id={metadata['id']}"
            )
            return metadata
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to get schema for {subject}: {e}")
            raise

    def get_schema_with_references(
        self, subject: str
    ) -> Tuple[Dict[str, Any], Dict[str, Dict[str, Any]]]:
        """Get schema with all references resolved"""
        if not self.enabled:
            raise RuntimeError("Schema Registry is disabled")

        cache_key = f"schema_with_refs:{subject}"
        with self._cache_lock:
            cached = self._schema_with_refs_cache.get(cache_key)
            if cached is not None:
                return cached

        try:
            metadata = self.get_schema_metadata(subject)
            schema_str = metadata["schema"]
            main_schema = json.loads(schema_str)
            references = metadata.get("references", [])

            logger.debug(f"References for {subject}: {references}")
            named_schemas: Dict[str, Dict[str, Any]] = {}

            if references:
                logger.debug(f"Loading {len(references)} references for {subject}")
                for ref in references:
                    ref_subject = ref["subject"]
                    ref_name = ref["name"]

                    with self._cache_lock:
                        cached_ref = self._named_schemas_cache.get(ref_name)
                    if cached_ref is not None:
                        named_schemas[ref_name] = cached_ref
                        logger.debug(f"Cache HIT for reference: {ref_name}")
                        continue

                    ref_metadata = self.get_schema_metadata(ref_subject)
                    ref_schema = json.loads(ref_metadata["schema"])

                    with self._cache_lock:
                        self._named_schemas_cache[ref_name] = ref_schema
                    named_schemas[ref_name] = ref_schema

            result = (main_schema, named_schemas)
            with self._cache_lock:
                self._schema_with_refs_cache[cache_key] = result

            return result
        except Exception as e:
            logger.error(f"Failed to load schema with references for {subject}: {e}")
            raise

    def clear_cache(self) -> None:
        """Clear all caches"""
        with self._cache_lock:
            self._metadata_cache.clear()
            self._schema_with_refs_cache.clear()
            self._named_schemas_cache.clear()
        logger.info("Cache cleared")

    def get_cache_stats(self) -> Dict[str, Any]:
        """Get cache statistics"""
        with self._cache_lock:
            return {
                "metadata": {
                    "size": len(self._metadata_cache),
                    "maxsize": self._metadata_cache.maxsize,
                    "ttl": self._metadata_cache.ttl,
                    "currsize": self._metadata_cache.currsize,
                },
                "schema_with_refs": {
                    "size": len(self._schema_with_refs_cache),
                    "maxsize": self._schema_with_refs_cache.maxsize,
                    "ttl": self._schema_with_refs_cache.ttl,
                    "currsize": self._schema_with_refs_cache.currsize,
                },
                "named_schemas": {
                    "size": len(self._named_schemas_cache),
                    "maxsize": self._named_schemas_cache.maxsize,
                    "ttl": self._named_schemas_cache.ttl,
                    "currsize": self._named_schemas_cache.currsize,
                },
            }

    def register_schema(self, subject: str, schema: dict) -> Optional[int]:
        """Register a new schema version"""
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

            # Invalidate cache after registration
            self.clear_cache()

            logger.info(f"Schema registered: subject={subject}, id={schema_id}")
            return schema_id

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to register schema for {subject}: {e}")
            raise


schema_registry_service = SchemaRegistryService(cache_ttl_seconds=3600)
