from contextvars import ContextVar
from typing import Optional

locale_context: ContextVar[Optional[str]] = ContextVar("locale", default="en")
user_id_context: ContextVar[Optional[int]] = ContextVar("user_id", default=None)
timezone_context: ContextVar[Optional[str]] = ContextVar("timezone", default=None)


def set_locale(locale: str) -> None:
    locale_context.set(locale)


def get_locale() -> str:
    value = locale_context.get()
    return value if value is not None else "en"


def set_user_id(user_id: int) -> None:
    user_id_context.set(user_id)


def get_user_id() -> Optional[int]:
    return user_id_context.get()


def set_timezone(timezone: str) -> None:
    timezone_context.set(timezone)


def get_timezone() -> Optional[str]:
    return timezone_context.get()
