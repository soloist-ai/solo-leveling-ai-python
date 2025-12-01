from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from src.config.config_loader import config


def create_llm() -> ChatOpenAI:
    model_config = config["ai"]
    api_key = model_config.get("api_key")
    api_key_secret = SecretStr(api_key) if api_key else None

    if not api_key_secret:
        raise ValueError("API key not found in configuration")

    llm = ChatOpenAI(
        model=model_config["name"],
        base_url=model_config["api_base"],
        temperature=model_config["temperature"],
        max_completion_tokens=model_config.get("max_tokens", 1024),
        timeout=model_config.get("timeout", 30),
        api_key=api_key_secret,
    )
    return llm
