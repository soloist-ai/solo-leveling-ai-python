import os
import re
import yaml
from pathlib import Path
from dotenv import load_dotenv
from typing import Optional, Any, Dict


def deep_update(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Рекурсивно объединяет два словаря (для override конфигураций)"""
    result = base.copy()
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_update(result[key], value)
        else:
            result[key] = value
    return result


def load_config(env: Optional[str] = None) -> dict:
    """Загружает конфигурацию из application.yml и application-{profile}.yml"""
    if env is None:
        env = os.getenv("APP_ENV", "development")

    base_path = Path(__file__).parent.parent
    resources_path = base_path / "resources"

    # Загружаем базовую конфигурацию
    base_config_path = resources_path / "application.yml"
    with open(base_config_path, "r", encoding="utf-8") as f:
        content = f.read()
        content = _substitute_env_vars(content)
        config = yaml.safe_load(content)

    # Загружаем profile-specific конфигурацию (если есть)
    if env != "development":
        profile_config_path = resources_path / f"application-{env}.yml"
        if profile_config_path.exists():
            with open(profile_config_path, "r", encoding="utf-8") as f:
                profile_content = f.read()
                profile_content = _substitute_env_vars(profile_content)
                profile_config = yaml.safe_load(profile_content)
                # Объединяем базовую конфигурацию с profile-specific
                config = deep_update(config, profile_config)

    return config

def _substitute_env_vars(content: str) -> str:
    """Заменяет ${VAR_NAME:default} на значения из environment variables"""
    pattern = r"\$\{([^}:]+)(?::([^}]*))?\}"

    def replacer(match):
        var_name = match.group(1)
        default_value = match.group(2) if match.group(2) is not None else ""
        return os.getenv(var_name, default_value)

    return re.sub(pattern, replacer, content)


# Загружаем конфигурацию при импорте модуля
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
