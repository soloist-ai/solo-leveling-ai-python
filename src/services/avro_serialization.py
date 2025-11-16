import io
import logging
from typing import TypeVar, Protocol, Type

from fastavro import schemaless_writer, schemaless_reader

from src.services.schema_registry_service import schema_registry_service

logger = logging.getLogger(__name__)

T = TypeVar("T", bound="DataclassProtocol")


# Протокол для dataclass с методами to_dict() и from_dict()
class DataclassProtocol(Protocol):
    def to_dict(self) -> dict: ...

    @classmethod
    def from_dict(cls: Type[T], data: dict) -> T: ...


def avro_serialize(data: dict, subject: str) -> bytes:
    """
    Сериализует dict в Avro binary используя схему из Schema Registry

    Args:
        data: Данные для сериализации (dict)
        subject: Subject схемы в Schema Registry

    Returns:
        Avro binary data
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

    Args:
        avro_bytes: Avro binary data
        subject: Subject схемы в Schema Registry

    Returns:
        Десериализованные данные (dict)
    """
    try:
        # Получаем схему и references из Schema Registry
        schema, named_schemas = schema_registry_service.get_schema_with_references(
            subject
        )

        # Десериализуем через fastavro
        buffer = io.BytesIO(avro_bytes)
        data = schemaless_reader(buffer, schema, named_schemas)

        logger.debug(f"Deserialized {len(avro_bytes)} bytes for {subject}")
        return data

    except Exception as e:
        logger.error(f"Failed to deserialize data for {subject}: {e}")
        raise


# Convenience функции для прямой работы с dataclasses
def serialize_dataclass(obj: DataclassProtocol, subject: str) -> bytes:
    """
    Сериализует dataclass в Avro

    Args:
        obj: Dataclass instance с методом to_dict()
        subject: Subject схемы в Schema Registry
    """
    if not hasattr(obj, "to_dict"):
        raise TypeError(f"{type(obj).__name__} must have to_dict() method")

    data_dict = obj.to_dict()
    return avro_serialize(data_dict, subject)


def deserialize_to_dataclass(
    avro_bytes: bytes, subject: str, dataclass_type: Type[T]
) -> T:
    """
    Десериализует Avro в dataclass

    Args:
        avro_bytes: Avro binary data
        subject: Subject схемы в Schema Registry
        dataclass_type: Тип dataclass с методом from_dict()
    """
    if not hasattr(dataclass_type, "from_dict"):
        raise TypeError(f"{dataclass_type.__name__} must have from_dict() class method")

    data_dict = avro_deserialize(avro_bytes, subject)
    return dataclass_type.from_dict(data_dict)
