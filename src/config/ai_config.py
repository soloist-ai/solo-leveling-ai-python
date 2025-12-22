from typing import Optional

from langchain_openai import ChatOpenAI
from pydantic import SecretStr

from src.config.config_loader import config


def _build_llm(
    *,
    temperature: float,
    max_tokens: int,
    timeout: int,
) -> ChatOpenAI:
    model_config = config["ai"]

    api_key = model_config.get("api_key")
    api_key_secret = SecretStr(api_key) if api_key else None
    if not api_key_secret:
        raise ValueError("API key not found in configuration")

    return ChatOpenAI(
        model=model_config["name"],
        base_url=model_config["api_base"],
        temperature=temperature,
        max_completion_tokens=max_tokens,
        timeout=timeout,
        api_key=api_key_secret,
    )


def create_llm(temperature: Optional[float] = None) -> ChatOpenAI:
    """Backwards compatible factory (used for generation)."""
    model_config = config["ai"]
    temp = temperature if temperature is not None else float(model_config["temperature"])
    return _build_llm(
        temperature=temp,
        max_tokens=int(model_config.get("max_tokens", 1024)),
        timeout=int(model_config.get("timeout", 30)),
    )


def create_validation_text_llm() -> ChatOpenAI:
    """Deterministic text-only LLM for extracting requirements."""
    model_config = config["ai"]
    validation_cfg = model_config.get("validation", {}) or {}
    return _build_llm(
        temperature=float(validation_cfg.get("temperature_text", 0.0)),
        max_tokens=int(validation_cfg.get("max_tokens_text", model_config.get("max_tokens", 1024))),
        timeout=int(validation_cfg.get("timeout", model_config.get("timeout", 30))),
    )


def create_validation_vision_llm() -> ChatOpenAI:
    """Low-temperature VLM for image fact extraction + matching."""
    model_config = config["ai"]
    validation_cfg = model_config.get("validation", {}) or {}
    return _build_llm(
        temperature=float(validation_cfg.get("temperature_vision", 0.1)),
        max_tokens=int(validation_cfg.get("max_tokens_vision", model_config.get("max_tokens", 1024))),
        timeout=int(validation_cfg.get("timeout", model_config.get("timeout", 30))),
    )
