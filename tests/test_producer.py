import asyncio
import logging
from aiokafka import AIOKafkaProducer

from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.rarity import Rarity
from src.avro.events.generate_tasks_event import GenerateTask
from src.kafka.producer import send_task_request
from src.config.config_loader import get_kafka_bootstrap_servers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def test_producer():
    """Тестирует отправку задачи в Kafka"""

    producer = AIOKafkaProducer(bootstrap_servers=get_kafka_bootstrap_servers())
    await producer.start()

    try:
        # Создаем тестовую задачу
        task = GenerateTask(
            taskId="id001_test",
            version=0,
            rarity=Rarity.EPIC,
            topics=[TaskTopic.PHYSICAL_ACTIVITY],
        )

        logger.info(f"📦 Sending Avro task: {task.to_dict()}")
        await send_task_request(producer, task)

    finally:
        await producer.stop()
        logger.info("👋 Producer disconnected")


if __name__ == "__main__":
    asyncio.run(test_producer())
