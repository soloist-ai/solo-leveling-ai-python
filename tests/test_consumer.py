import asyncio
import logging
from contextlib import asynccontextmanager
from faststream import FastStream
from faststream.kafka import KafkaBroker

from src.avro.events.save_tasks_event import SaveTask
from src.services.avro_serialization import avro_deserialize
from src.config.kafka_config import topics
from src.config.config_loader import get_kafka_bootstrap_servers, config

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Создаём отдельный broker для test_consumer
test_broker = KafkaBroker(get_kafka_bootstrap_servers())


@asynccontextmanager
async def lifespan():
    """Управление жизненным циклом test consumer"""
    await test_broker.start()
    logger.info(f"✅ Test consumer listening to: {topics['task_responses']}")
    yield
    await test_broker.close()


# Регистрируем consumer для task.responses
@test_broker.subscriber(
    topics["task_responses"],
    group_id="test-consumer-group",
    auto_offset_reset=config["kafka"]["consumer"]["auto_offset_reset"],
)
async def handle_task_response(message: bytes):
    """Получает сгенерированные задачи"""
    try:
        schema = SaveTask.avro_schema_to_python()
        obj = avro_deserialize(message, schema)
        task = SaveTask(**obj)

        logger.info(f"Generated task: {task}")

    except Exception as e:
        logger.error(f"Error processing task response: {e}")


# Создаём FastStream приложение
app = FastStream(test_broker, lifespan=lifespan)

if __name__ == "__main__":
    asyncio.run(app.run())
