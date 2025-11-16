from typing import Any, Optional
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer, AvroSerializer


class ConfluentAvroService:
    def __init__(self, schema_registry_url: str) -> None:
        self.schema_registry_client: SchemaRegistryClient = SchemaRegistryClient(
            {'url': schema_registry_url}
        )
        self.deserializer_cache: dict[str, AvroDeserializer] = {}
        self.serializer_cache: dict[str, AvroSerializer] = {}

    def get_deserializer(self, subject: str) -> AvroDeserializer:
        if subject not in self.deserializer_cache:
            self.deserializer_cache[subject] = AvroDeserializer(  # type: ignore[call-arg]
                schema_registry_client=self.schema_registry_client,
                schema_str=None,
                from_dict=None,
                return_record_name=False,
            )
        return self.deserializer_cache[subject]

    def get_serializer(self, subject: str) -> AvroSerializer:
        if subject not in self.serializer_cache:
            self.serializer_cache[subject] = AvroSerializer(  # type: ignore[call-arg]
                schema_registry_client=self.schema_registry_client,
                schema_str=None,
                to_dict=None,
            )
        return self.serializer_cache[subject]

    def deserialize(self, avro_bytes: bytes, subject: str) -> dict[str, Any]:
        deserializer = self.get_deserializer(subject)
        ctx = SerializationContext(subject, MessageField.VALUE)
        return deserializer(avro_bytes, ctx)

    def serialize(self, data: dict[str, Any], subject: str) -> bytes:
        serializer = self.get_serializer(subject)
        ctx = SerializationContext(subject, MessageField.VALUE)
        return serializer(data, ctx)
