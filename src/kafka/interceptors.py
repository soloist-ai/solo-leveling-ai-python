import logging
from typing import Optional, List, Tuple
from faststream.kafka.message import KafkaMessage
from src.kafka.context import set_locale, clear_locale, get_locale

logger = logging.getLogger(__name__)


class ConsumerLocaleInterceptor:
    @staticmethod
    def extract_locale_from_headers(msg: KafkaMessage) -> Optional[str]:
        if not msg.headers:
            return None

        for header_key, header_value in msg.headers:
            if header_key == 'x-locale':
                try:
                    locale = header_value.decode('utf-8') if isinstance(header_value, bytes) else header_value
                    logger.debug(f"Extracted locale from headers: {locale}")
                    return locale
                except Exception as e:
                    logger.warning(f"Failed to decode x-locale header: {e}")
                    return None

        return None

    @staticmethod
    def process_message(msg: KafkaMessage) -> None:
        locale = ConsumerLocaleInterceptor.extract_locale_from_headers(msg)

        if locale:
            set_locale(locale)
            logger.debug(f"Set locale context to: {locale}")
        else:
            clear_locale()
            logger.debug("No locale header found, using default: en")


class ProducerLocaleInterceptor:
    @staticmethod
    def inject_locale_header(
            existing_headers: Optional[List[Tuple[str, bytes]]] = None
    ) -> List[Tuple[str, bytes]]:
        headers = existing_headers or []

        has_locale = any(key == 'x-locale' for key, _ in headers)

        if not has_locale:
            locale = get_locale()
            headers.append(('x-locale', locale.encode('utf-8')))
            logger.debug(f"Injected x-locale header: {locale}")

        return headers
