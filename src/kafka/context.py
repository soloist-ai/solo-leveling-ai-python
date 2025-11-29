from contextvars import ContextVar
from typing import Optional

locale_context: ContextVar[Optional[str]] = ContextVar('locale', default='en')

def set_locale(locale: str) -> None:
    locale_context.set(locale)

def get_locale() -> str:
    return locale_context.get()

def clear_locale() -> None:
    locale_context.set('en')
