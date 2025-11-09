import asyncio
import logging
from contextlib import asynccontextmanager
from faststream import FastStream
from dishka import make_async_container
from dishka.integrations.faststream import setup_dishka

from src.config.kafka_config import kafka_broker
from src.kafka.consumer import register_consumers
from src.config.logging_config import setup_logging
from src.config.config_loader import get_environment, is_production, is_feature_enabled
from src.services.schema_registry_service import schema_registry_service
from src.avro.events.generate_tasks_event import GenerateTask
from src.avro.events.save_tasks_event import SaveTask

# Импортируем providers
from src.di.providers import (
    ConfigProvider,
    LLMProvider,
    TaskServiceProvider,
    KafkaProvider,
)

setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan():
    env = get_environment()
    logger.info(f"Starting Solo Leveling AI in {env} environment")

    # Feature flags
    logger.info("Feature flags:")
    logger.info(f"  - Schema Registry: {is_feature_enabled('use_schema_registry')}")
    logger.info(f"  - Task Caching: {is_feature_enabled('enable_task_caching')}")
    logger.info(f"  - Metrics: {is_feature_enabled('enable_metrics')}")
    logger.info(f"  - Debug Logging: {is_feature_enabled('debug_logging')}")

    if is_production():
        logger.info("⚡ Running in PRODUCTION mode")

    if is_feature_enabled("use_schema_registry"):
        logger.info("Registering Avro schemas...")
        try:
            request_schema = GenerateTask.avro_schema_to_python()
            request_id = schema_registry_service.register_schema(
                "task.requests-value", request_schema
            )
            logger.info(f"GenerateTask schema registered (ID: {request_id})")

            response_schema = SaveTask.avro_schema_to_python()
            response_id = schema_registry_service.register_schema(
                "task.responses-value", response_schema
            )
            logger.info(f"SaveTask schema registered (ID: {response_id})")

        except Exception as e:
            logger.error(f"Failed to register schemas: {e}")
            if is_production():
                raise

    await kafka_broker.start()
    logger.info("Kafka broker connected")

    yield

    await kafka_broker.close()
    logger.info("Application shutdown complete")


container = make_async_container(
    ConfigProvider(),
    LLMProvider(),
    TaskServiceProvider(),
    KafkaProvider(),
)

app = FastStream(kafka_broker, lifespan=lifespan)

setup_dishka(container, app)

register_consumers(kafka_broker)

if __name__ == "__main__":
    logger.info("Consumer is running. Waiting for messages...")
    asyncio.run(app.run())
