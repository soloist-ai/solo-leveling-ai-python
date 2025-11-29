import logging
from typing import Optional, List, Tuple, Dict, Any
from faststream.kafka.message import KafkaMessage
from src.kafka.context import set_locale, clear_locale, get_locale

logger = logging.getLogger(__name__)


class ConsumerLocaleInterceptor:
    @staticmethod
    def extract_locale_from_headers(msg: KafkaMessage) -> Optional[str]:
        if not msg.headers:
            return None

        headers: Dict[str, Any] = msg.headers
        header_value = headers.get("x-locale")

        if header_value is not None:
            try:
                if isinstance(header_value, bytes):
                    locale = header_value.decode("utf-8")
                else:
                    locale = str(header_value)

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
            logger.debug("No locale header found, using default: en")


class ProducerLocaleInterceptor:
    @staticmethod
    def inject_locale_header(
        existing_headers: Optional[List[Tuple[str, bytes]]] = None,
    ) -> List[Tuple[str, bytes]]:
        headers: List[Tuple[str, bytes]] = (
            existing_headers if existing_headers is not None else []
        )

        has_locale = any(key == "x-locale" for key, _ in headers)

        if not has_locale:
            locale = get_locale()
            headers.append(("x-locale", locale.encode("utf-8")))
            logger.debug(f"Injected x-locale header: {locale}")

        return headers
