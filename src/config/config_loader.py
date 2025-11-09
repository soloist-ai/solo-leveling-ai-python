import os
import re
import yaml
from pathlib import Path
from dotenv import load_dotenv
from typing import Optional


def load_config(env: Optional[str] = None) -> dict:
    """Загружает конфигурацию из application.yml"""
    if env is None:
        env = os.getenv("APP_ENV", "development")

    if env == "production":
        load_dotenv(".env.production", override=True)
    else:
        load_dotenv(".env", override=True)

    base_path = Path(__file__).parent.parent
    config_path = base_path / "resources" / "application.yml"

    with open(config_path, "r", encoding="utf-8") as f:
        content = f.read()

    content = _substitute_env_vars(content)
    return yaml.safe_load(content)


def _substitute_env_vars(content: str) -> str:
    pattern = r"\$\{([^}:]+)(?::([^}]*))?\}"

    def replacer(match):
        var_name = match.group(1)
        default_value = match.group(2) if match.group(2) is not None else ""
        return os.getenv(var_name, default_value)

    return re.sub(pattern, replacer, content)


config = load_config()


# ========== Kafka ==========
def get_kafka_bootstrap_servers() -> str:
    return config["kafka"]["bootstrap_servers"]


def get_kafka_topics() -> dict:
    return config["kafka"]["topics"]


def get_kafka_consumer_config() -> dict:
    return config["kafka"]["consumer"]


def get_kafka_producer_config() -> dict:
    return config["kafka"]["producer"]


# ========== Schema Registry ==========
def get_schema_registry_url() -> str:
    return config["schema_registry"]["url"]


def get_schema_registry_timeout() -> int:
    return config["schema_registry"]["timeout"]


# ========== AI ==========
def get_ai_config() -> dict:
    return config["ai"]


# ========== Feature Flags ==========
def is_feature_enabled(feature_name: str) -> bool:
    return config.get("features", {}).get(feature_name, False)


# ========== Environment ==========
def get_environment() -> str:
    return config["app"]["environment"]


def is_production() -> bool:
    return get_environment() == "production"


def is_development() -> bool:
    return get_environment() == "development"


# ========== Avro ==========
def get_avro_namespace() -> str:
    return config["avro"]["namespace"]


def get_avro_compatibility() -> str:
    return config["avro"]["compatibility"]
