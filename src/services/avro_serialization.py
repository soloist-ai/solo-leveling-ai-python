from typing import Any
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroDeserializer, AvroSerializer
from confluent_kafka.schema_registry import record_subject_name_strategy


class ConfluentAvroService:
    def __init__(self, schema_registry_url: str) -> None:
        self.schema_registry_client = SchemaRegistryClient({"url": schema_registry_url})
        self.deserializer_cache: dict[str, AvroDeserializer] = {}
        self.serializer_cache: dict[str, AvroSerializer] = {}

    def get_deserializer(self, subject: str) -> AvroDeserializer:
        if subject not in self.deserializer_cache:
            self.deserializer_cache[subject] = AvroDeserializer(
                schema_registry_client=self.schema_registry_client,
                schema_str=None,
                from_dict=None,
                return_record_name=False,
            )
        return self.deserializer_cache[subject]

    def get_serializer(self, subject: str) -> AvroSerializer:
        if subject not in self.serializer_cache:
            latest_version = self.schema_registry_client.get_latest_version(subject)
            schema_str = (
                latest_version.get("schema")
                if isinstance(latest_version, dict)
                else getattr(latest_version, "schema", None)
            )
            if not schema_str:
                raise ValueError(
                    f"Failed to obtain schema string for subject '{subject}'"
                )
            self.serializer_cache[subject] = AvroSerializer(
                schema_registry_client=self.schema_registry_client,
                schema_str=schema_str,
                to_dict=None,
                conf={
                    "auto.register.schemas": False,
                    "use.latest.version": True,
                    "subject.name.strategy": record_subject_name_strategy,
                },
            )
        return self.serializer_cache[subject]

    def deserialize(self, avro_bytes: bytes, subject: str) -> dict[str, Any]:
        deserializer = self.get_deserializer(subject)
        ctx = SerializationContext(subject, MessageField.VALUE)
        result = deserializer(avro_bytes, ctx)
        if not isinstance(result, dict):
            raise TypeError(f"Expected dict, got {type(result)}")
        return result

    def serialize(self, data: dict[str, Any], subject: str) -> bytes:
        serializer = self.get_serializer(subject)
        ctx = SerializationContext(subject, MessageField.VALUE)
        result = serializer(data, ctx)
        if result is None:
            raise ValueError("Serialization returned None")
        return result
