from typing import Any
from confluent_kafka.serialization import SerializationContext, MessageField
from confluent_kafka.schema_registry import SchemaRegistryClient, Schema
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
                schema_str=None,  # Writer schema будет автоматически получена
                from_dict=None,
                return_record_name=False,
            )
        return self.deserializer_cache[subject]

    def get_serializer(self, subject: str) -> AvroSerializer:
        if subject not in self.serializer_cache:
            # Получаем RegisteredSchema, который содержит Schema с references
            latest_version = self.schema_registry_client.get_latest_version(subject)

            # Создаем объект Schema (не строку!), который содержит references
            schema = Schema(
                schema_str=latest_version.schema.schema_str,
                schema_type=latest_version.schema.schema_type,
                references=latest_version.schema.references,  # ✅ Передаем references
            )

            self.serializer_cache[subject] = AvroSerializer(
                schema_registry_client=self.schema_registry_client,
                schema_str=schema,  # ✅ Передаем Schema объект, не строку
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
