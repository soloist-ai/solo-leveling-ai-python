import logging
from typing import Optional, List, Tuple, Dict, Any
from faststream.kafka.message import KafkaMessage
from src.kafka.context import set_locale, get_locale, set_user_id, get_user_id, set_timezone, get_timezone

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
    def extract_user_id_from_headers(msg: KafkaMessage) -> Optional[int]:
        if not msg.headers:
            return None
        headers: Dict[str, Any] = msg.headers
        header_value = headers.get("x-user-id")
        if header_value is not None:
            try:
                if isinstance(header_value, bytes):
                    user_id = int(header_value.decode("utf-8"))
                else:
                    user_id = int(header_value)
                logger.debug(f"Extracted user_id from headers: {user_id}")
                return user_id
            except Exception as e:
                logger.warning(f"Failed to decode x-user-id header: {e}")
                return None
        return None

    @staticmethod
    def extract_timezone_from_headers(msg: KafkaMessage) -> Optional[str]:
        if not msg.headers:
            return None
        headers: Dict[str, Any] = msg.headers
        header_value = headers.get("x-timezone")
        if header_value is not None:
            try:
                if isinstance(header_value, bytes):
                    timezone = header_value.decode("utf-8")
                else:
                    timezone = str(header_value)
                logger.debug(f"Extracted timezone from headers: {timezone}")
                return timezone
            except Exception as e:
                logger.warning(f"Failed to decode x-timezone header: {e}")
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

        user_id = ConsumerLocaleInterceptor.extract_user_id_from_headers(msg)
        if user_id is not None:
            set_user_id(user_id)
            logger.debug(f"Set user_id context to: {user_id}")

        timezone = ConsumerLocaleInterceptor.extract_timezone_from_headers(msg)
        if timezone:
            set_timezone(timezone)
            logger.debug(f"Set timezone context to: {timezone}")


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

        has_user_id = any(key == "x-user-id" for key, _ in headers)
        if not has_user_id:
            user_id = get_user_id()
            if user_id is not None:
                headers.append(("x-user-id", str(user_id).encode("utf-8")))
                logger.debug(f"Injected x-user-id header: {user_id}")

        has_timezone = any(key == "x-timezone" for key, _ in headers)
        if not has_timezone:
            timezone = get_timezone()
            if timezone:
                headers.append(("x-timezone", timezone.encode("utf-8")))
                logger.debug(f"Injected x-timezone header: {timezone}")

        return headers
