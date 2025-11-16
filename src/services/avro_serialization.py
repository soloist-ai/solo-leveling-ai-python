import io
import logging
from typing import Any, TypeVar, Type, Protocol, cast

from fastavro import schemaless_writer, schemaless_reader

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
    Десериализует Avro binary в dict, используя сырую схему из Schema Registry.
    """
    try:
        schema, named_schemas = schema_registry_service.get_schema_with_references(
            subject
        )

        buffer = io.BytesIO(avro_bytes)
        data = schemaless_reader(buffer, schema, named_schemas)

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
