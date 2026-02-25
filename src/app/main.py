import uvicorn
import logging
from contextlib import asynccontextmanager
from faststream import FastStream
from dishka import make_async_container
from dishka.integrations.faststream import setup_dishka
from faststream.asgi import AsgiFastStream, make_ping_asgi
from faststream.kafka import KafkaBroker
from src.kafka.consumer import register_consumers
from src.config.logging_config import setup_logging
from src.config.config_loader import (
    get_environment,
    is_production,
    is_feature_enabled,
    get_kafka_bootstrap_servers,
)
from src.services.schema_registry_service import schema_registry_service
from src.di.providers import (
    ConfigProvider,
    LLMProvider,
    TaskServiceProvider,
    ProducerProvider,
)

kafka_broker = KafkaBroker(get_kafka_bootstrap_servers())
setup_logging()
logger = logging.getLogger(__name__)
SCHEMA_SUBJECTS = [
    "com.soloist.avro.task.GenerateTasksEvent",
    "com.soloist.avro.task.SaveTasksEvent",
]


@asynccontextmanager
async def lifespan():
    env = get_environment()
    logger.info(f"Starting Soloist AI in {env} environment")
    logger.info("Feature flags:")
    logger.info(f"  - Schema Registry: {is_feature_enabled('use_schema_registry')}")
    logger.info(f"  - Task Caching: {is_feature_enabled('enable_task_caching')}")
    logger.info(f"  - Metrics: {is_feature_enabled('enable_metrics')}")
    logger.info(f"  - Debug Logging: {is_feature_enabled('debug_logging')}")

    if is_production():
        logger.info("Running in PRODUCTION mode")

    if is_feature_enabled("use_schema_registry"):
        logger.info("Loading schemas from Schema Registry...")
        try:
            for subject in SCHEMA_SUBJECTS:
                schema_data = schema_registry_service.get_schema_metadata(subject)
                logger.info(
                    f"{subject}: version={schema_data['version']}, id={schema_data['id']}"
                )
        except Exception as e:
            logger.error(f"Failed to load schemas from Schema Registry: {e}")
            if is_production():
                raise
            logger.warning("Continuing without Schema Registry validation")

    await kafka_broker.start()
    logger.info("Kafka broker connected")

    yield

    await kafka_broker.stop()
    logger.info("Application shutdown complete")


container = make_async_container(
    ConfigProvider(),
    LLMProvider(),
    TaskServiceProvider(),
    ProducerProvider(),
)

faststream_app = FastStream(kafka_broker, lifespan=lifespan)
register_consumers(kafka_broker)
setup_dishka(container, faststream_app, auto_inject=True)

app = AsgiFastStream(
    kafka_broker,
    lifespan=lifespan,
    asgi_routes=[
        (
            "/health",
            make_ping_asgi(kafka_broker, timeout=5.0),
        ),
    ],
)

if __name__ == "__main__":
    logger.info("Starting application with health check endpoint...")
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080,
        log_level="info",
    )
