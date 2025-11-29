from contextvars import ContextVar
from typing import Optional

locale_context: ContextVar[Optional[str]] = ContextVar("locale", default="en")


def set_locale(locale: str) -> None:
    locale_context.set(locale)


def get_locale() -> str:
    value = locale_context.get()
    return value if value is not None else "en"
