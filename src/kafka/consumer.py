import asyncio
import logging
from faststream.kafka import KafkaBroker
from dishka.integrations.faststream import inject, FromDishka
from src.services.task_service import TaskService
from src.avro.events.generate_tasks_event import GenerateTask
from src.avro.events.save_tasks_event import SaveTask
from src.services.avro_serialization import avro_deserialize, avro_serialize

logger = logging.getLogger(__name__)

def register_consumers(broker: KafkaBroker):
    @broker.subscriber("task.requests")
    @inject
    async def handle_task_request(
        message: bytes,
        task_service: FromDishka[TaskService],
    ):
        try:

            schema = GenerateTask.avro_schema_to_python()
            obj = avro_deserialize(message, schema)
            task_data = GenerateTask(**obj)
            logger.info(f"Received task request: {task_data}")
            result_task = await asyncio.to_thread(
                task_service.generate_task,
                topics=task_data.topics,
                rarity=task_data.rarity
            )
            logger.info(f"Generated task: {result_task}")
            save_task = SaveTask(
                taskId=task_data.taskId,
                version=task_data.version,
                rarity=task_data.rarity,
                topics=task_data.topics,
                title=result_task.title,
                description=result_task.description,
                experience=result_task.experience,
                currencyReward=result_task.currencyReward,
                agility=result_task.agility,
                strength=result_task.strength,
                intelligence=result_task.intelligence,
            )
            response_schema = SaveTask.avro_schema_to_python()
            response_bytes = avro_serialize(save_task.to_dict(), response_schema)
            await broker.publish(response_bytes, topic="task.responses")
        except Exception as e:
            logger.error(f"Error processing task request: {e}")
            error_response = {
                "error": str(e),
                "original_request": str(obj),
                "status": "failed",
            }
            await broker.publish(str(error_response).encode(), topic="task.errors")
            logger.error("Sent error to topic: task.errors")

    logger.info("Consumer registered for topic 'task.requests'")
