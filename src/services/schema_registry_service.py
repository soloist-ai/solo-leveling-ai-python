import logging
import requests
import json
from typing import Optional
from src.config.config_loader import (
    get_schema_registry_url,
    get_schema_registry_timeout,
    is_feature_enabled,
)

logger = logging.getLogger(__name__)


class SchemaRegistryService:
    def __init__(self):
        self.enabled = is_feature_enabled("use_schema_registry")

        if not self.enabled:
            logger.info("Schema Registry disabled by feature flag")
            return

        self.url = get_schema_registry_url()
        self.timeout = get_schema_registry_timeout()
        logger.info(f"Schema Registry initialized: {self.url}")

    def register_schema(self, subject: str, schema: dict) -> Optional[int]:
        if not self.enabled:
            logger.debug("Schema Registry disabled, skipping registration")
            return None

        try:
            url = f"{self.url}/subjects/{subject}/versions"
            payload = {"schema": json.dumps(schema)}

            logger.debug(f"Registering schema for subject: {subject}")

            response = requests.post(
                url,
                json=payload,
                timeout=self.timeout,
                headers={"Content-Type": "application/vnd.schemaregistry.v1+json"},
            )
            response.raise_for_status()

            schema_id = response.json().get("id")
            logger.info(f"Schema registered: subject={subject}, id={schema_id}")
            return schema_id

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to register schema for {subject}: {e}")
            if hasattr(e, "response") and e.response is not None:
                try:
                    error_detail = e.response.json()
                    logger.error(f"Error details: {error_detail}")
                except (ValueError, KeyError, TypeError):
                    logger.error(f"Response text: {e.response.text}")

            raise

    def get_schema(self, subject: str, version: str = "latest") -> Optional[dict]:
        if not self.enabled:
            return None

        try:
            url = f"{self.url}/subjects/{subject}/versions/{version}"
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()

            schema_data = response.json()
            logger.info(f"Retrieved schema: subject={subject}, version={version}")
            return schema_data

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to get schema for {subject}: {e}")
            raise

    def check_compatibility(self, subject: str, schema: dict) -> bool:
        if not self.enabled:
            return True

        try:
            url = f"{self.url}/compatibility/subjects/{subject}/versions/latest"
            payload = {"schema": json.dumps(schema)}

            response = requests.post(
                url,
                json=payload,
                timeout=self.timeout,
                headers={"Content-Type": "application/vnd.schemaregistry.v1+json"},
            )
            response.raise_for_status()

            is_compatible = response.json().get("is_compatible", False)
            logger.info(
                f"Schema compatibility check: subject={subject}, compatible={is_compatible}"
            )
            return is_compatible

        except requests.exceptions.RequestException as e:
            logger.warning(f"Failed to check compatibility for {subject}: {e}")
            return True


schema_registry_service = SchemaRegistryService()
