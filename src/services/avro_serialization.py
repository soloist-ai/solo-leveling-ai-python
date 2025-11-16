from typing import Any
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer, AvroSerializer


class ConfluentAvroService:
    def __init__(self, schema_registry_url: str) -> None:
        self.schema_registry_client = SchemaRegistryClient({"url": schema_registry_url})
        self.deserializer_cache: dict[str, AvroDeserializer] = {}
        self.serializer_cache: dict[str, AvroSerializer] = {}

    def get_deserializer(self, subject: str) -> AvroDeserializer:
        if subject not in self.deserializer_cache:
            self.deserializer_cache[subject] = AvroDeserializer(
                schema_registry_client=self.schema_registry_client,
                schema_str=None,  # type: ignore[arg-type]
                from_dict=None,
                return_record_name=False,
            )
        return self.deserializer_cache[subject]

    def get_serializer(self, subject: str) -> AvroSerializer:
        if subject not in self.serializer_cache:
            self.serializer_cache[subject] = AvroSerializer(
                schema_registry_client=self.schema_registry_client,
                schema_str=None,  # type: ignore[arg-type]
                to_dict=None,
            )
        return self.serializer_cache[subject]

    def deserialize(self, avro_bytes: bytes, subject: str) -> dict[str, Any]:
        deserializer = self.get_deserializer(subject)
        ctx = SerializationContext(subject, MessageField.VALUE)
        result = deserializer(avro_bytes, ctx)
        # deserializer может вернуть разные типы, но мы ожидаем dict
        if not isinstance(result, dict):
            raise TypeError(f"Expected dict, got {type(result)}")
        return result  # type: ignore[return-value]

    def serialize(self, data: dict[str, Any], subject: str) -> bytes:
        serializer = self.get_serializer(subject)
        ctx = SerializationContext(subject, MessageField.VALUE)
        result = serializer(data, ctx)
        if result is None:
            raise ValueError("Serialization returned None")
        return result
