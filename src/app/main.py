import asyncio
import logging
import json

from faststream import FastStream
from faststream.kafka import KafkaBroker
from dishka import make_async_container
from dishka.integrations.faststream import setup_dishka
from src.kafka.consumer import register_consumers
from src.di.providers import (
    ConfigProvider,
    LLMProvider,
    TaskServiceProvider,
    FastStreamProvider,
)
from src.services.schema_registry import register_schema
from src.avro.events.generate_tasks_event import GenerateTask

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    logger.info("🚀 Starting Task Generator Microservice...")

    # --- Регистрация схемы Avro через REST API Schema Registry (один раз при старте) ---
    try:
        avro_schema = json.dumps(GenerateTask.avro_schema_to_python())
        schema_reg_result = register_schema("task.requests-value", avro_schema)
        logger.info(f"Avro schema registered: {schema_reg_result}")
    except Exception as ex:
        logger.error(f"Failed to register Avro schema: {ex}")

    container_factory = make_async_container(
        ConfigProvider(),
        LLMProvider(),
        TaskServiceProvider(),
        FastStreamProvider(),
    )
    async with container_factory() as container:
        broker = await container.get(KafkaBroker)
        logger.info("Kafka broker obtained from DI")

        setup_dishka(container=container, broker=broker, auto_inject=True)
        logger.info("Dishka integration configured")

        register_consumers(broker)
        logger.info("Consumers registered")

        app = FastStream(broker)
        logger.info("Microservice ready! Listening for task requests...")

        await app.run()


if __name__ == "__main__":
    asyncio.run(main())
