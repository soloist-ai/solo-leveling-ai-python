import io
import logging
from typing import Any, TypeVar, Type, Protocol, cast

from fastavro import schemaless_writer, schemaless_reader, parse_schema

from src.services.schema_registry_service import schema_registry_service

logger = logging.getLogger(__name__)


class FromDictProtocol(Protocol):
    """Протокол для классов с classmethod from_dict()."""

    @classmethod
    def from_dict(cls, data: dict) -> "FromDictProtocol": ...


T = TypeVar("T", bound=FromDictProtocol)


def avro_serialize(data: dict, subject: str) -> bytes:
    """
    Сериализует dict в Avro binary используя схему из Schema Registry
    """
    try:
        schema, named_schemas = schema_registry_service.get_schema_with_references(
            subject
        )

        # Создаём общий словарь для fastavro
        fastavro_named_schemas: dict[str, Any] = {}

        # Парсим все reference-схемы
        for name, ref_schema in named_schemas.items():
            parse_schema(ref_schema, fastavro_named_schemas, _write_hint=False)

        # Парсим основную схему
        parsed_schema = parse_schema(schema, fastavro_named_schemas, _write_hint=False)

        buffer = io.BytesIO()
        schemaless_writer(buffer, parsed_schema, data)
        avro_bytes = buffer.getvalue()

        logger.debug(f"Serialized {len(avro_bytes)} bytes for {subject}")
        return avro_bytes

    except Exception as e:
        logger.error(f"Failed to serialize data for {subject}: {e}")
        logger.debug(f"Data: {data}")
        raise


def avro_deserialize(avro_bytes: bytes, subject: str) -> dict:
    try:
        schema, named_schemas = schema_registry_service.get_schema_with_references(
            subject
        )
        logger.info(f"[DEBUG] Deserializing {subject}")
        logger.info(f"[DEBUG] named_schemas keys: {list(named_schemas.keys())}")

        buffer = io.BytesIO(avro_bytes)
        fastavro_named_schemas: dict[str, Any] = {}

        # Фиксированный порядок: Rarity (enum) перед TaskTopic
        ref_order = [
            "com.sleepkqq.sololeveling.avro.player.Rarity",
            "com.sleepkqq.sololeveling.avro.task.TaskTopic",
        ]
        for name in ref_order:
            if name in named_schemas:
                ref_schema = named_schemas[name]
                logger.info(f"[DEBUG] Parsing named schema: {name}")
                # Убрали write_hint, добавили expand для референсов (если нужно)
                parsed_ref = parse_schema(
                    ref_schema, named_schemas=fastavro_named_schemas, expand=False
                )
                fastavro_named_schemas[name] = parsed_ref
                logger.debug(f"[DEBUG] Parsed {name}: {parsed_ref}")  # Для отладки

        # Основная схема: expand=True для полного разрешения ссылок (Rarity в полях)
        parsed_main_schema = parse_schema(
            schema, named_schemas=fastavro_named_schemas, expand=True
        )
        logger.debug(f"[DEBUG] Main schema resolved: {parsed_main_schema}")

        data = schemaless_reader(buffer, parsed_main_schema)
        logger.debug(f"Deserialized {len(avro_bytes)} bytes for {subject}")
        return data
    except Exception as e:
        logger.error(f"Failed to deserialize data for {subject}: {e}")
        raise


def serialize_dataclass(obj: Any, subject: str) -> bytes:
    """
    Сериализует dataclass в Avro
    """
    if not hasattr(obj, "to_dict") or not callable(getattr(obj, "to_dict")):
        raise TypeError(f"{type(obj).__name__} must have callable to_dict() method")

    data_dict = obj.to_dict()
    return avro_serialize(data_dict, subject)


def deserialize_to_dataclass(
    avro_bytes: bytes, subject: str, dataclass_type: Type[T]
) -> T:
    """
    Десериализует Avro в dataclass
    """
    if not hasattr(dataclass_type, "from_dict") or not callable(
        getattr(dataclass_type, "from_dict")
    ):
        raise TypeError(
            f"{dataclass_type.__name__} must have callable from_dict() class method"
        )

    data_dict = avro_deserialize(avro_bytes, subject)
    result = dataclass_type.from_dict(data_dict)
    return cast(T, result)
