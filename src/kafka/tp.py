import asyncio
import logging
from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.task_rarity import TaskRarity
from src.avro.events.generate_tasks_event import GenerateTask
from src.kafka.producer import send_task_request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def test_producer():
    task = GenerateTask(
        taskId="id001_test",
        version=0,
        rarity=TaskRarity.LEGENDARY,
        topics=[TaskTopic.MENTAL_HEALTH],
    )
    logger.info(f"📦 Sending Avro task: {task.to_dict()}")
    await send_task_request(task)


if __name__ == "__main__":
    asyncio.run(test_producer())
