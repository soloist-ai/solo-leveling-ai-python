import io
import logging
from typing import Any, TypeVar, Type, cast, Protocol

from fastavro import schemaless_writer, schemaless_reader, parse_schema

from src.services.schema_registry_service import schema_registry_service

logger = logging.getLogger(__name__)


class FromDictProtocol(Protocol):
    """Протокол для классов, у которых есть classmethod from_dict()."""

    @classmethod
    def from_dict(cls, data: dict) -> "FromDictProtocol": ...


T = TypeVar("T", bound=FromDictProtocol)


def avro_serialize(data: dict, subject: str) -> bytes:
    """
    Сериализует dict в Avro binary используя схему из Schema Registry
    """
    try:
        # Получаем схему и references из Schema Registry
        schema, named_schemas = schema_registry_service.get_schema_with_references(
            subject
        )

        # Сериализуем через fastavro
        buffer = io.BytesIO()
        schemaless_writer(buffer, schema, data, named_schemas)
        avro_bytes = buffer.getvalue()

        logger.debug(f"Serialized {len(avro_bytes)} bytes for {subject}")
        return avro_bytes
    except Exception as e:
        logger.error(f"Failed to serialize data for {subject}: {e}")
        logger.debug(f"Data: {data}")
        raise


def avro_deserialize(avro_bytes: bytes, subject: str) -> dict:
    """
    Десериализует Avro binary в dict используя схему из Schema Registry
    """
    try:
        # Получаем схему и references из Schema Registry
        schema, named_schemas = schema_registry_service.get_schema_with_references(
            subject
        )

        logger.debug(
            f"Deserializing {subject} with named_schemas: {list(named_schemas.keys())}"
        )

        # Явно парсим схему с учётом named_schemas через публичный API fastavro
        parsed_schema = parse_schema(schema, named_schemas)

        # Десериализуем через fastavro
        buffer = io.BytesIO(avro_bytes)
        data = schemaless_reader(buffer, parsed_schema, named_schemas)

        logger.debug(f"Deserialized {len(avro_bytes)} bytes for {subject}")
        return data
    except Exception as e:
        logger.error(f"Failed to deserialize data for {subject}: {e}")
        raise


def serialize_dataclass(obj: Any, subject: str) -> bytes:
    """
    Сериализует dataclass в Avro

    obj: dataclass с методом to_dict()
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

    dataclass_type: класс с classmethod from_dict()
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
