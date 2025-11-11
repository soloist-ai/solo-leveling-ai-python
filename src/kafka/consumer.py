import asyncio
import logging
from faststream.kafka import KafkaBroker
from dishka.integrations.faststream import inject, FromDishka

from src.services.task_service import TaskService
from src.avro.events.generate_tasks_event import GenerateTask
from src.avro.events.save_tasks_event import SaveTask
from src.services.avro_serialization import avro_deserialize, avro_serialize
from src.config.kafka_config import topics
from src.config.config_loader import config, is_feature_enabled

logger = logging.getLogger(__name__)


def register_consumers(broker: KafkaBroker):
    kafka_config = config["kafka"]

    @broker.subscriber(
        topics["task_requests"],
        group_id=kafka_config["consumer"]["group_id"],
        auto_offset_reset=kafka_config["consumer"]["auto_offset_reset"],
    )
    @inject
    async def handle_task_request(
        message: bytes,
        task_service: FromDishka[TaskService],
    ):
        try:
            schema = GenerateTask.avro_schema_to_python()
            obj = avro_deserialize(message, schema)
            task_data = GenerateTask(**obj)

            logger.info(f"Received task request: taskId={task_data.taskId}")

            if is_feature_enabled("debug_logging"):
                logger.debug(f"Full task data: {task_data}")

            result_task = await asyncio.to_thread(
                task_service.generate_task,
                topics=task_data.topics,
                rarity=task_data.rarity,
            )

            logger.info(f"Generated task: {result_task}")

            save_task = SaveTask.from_generated(task_data, result_task)
            response_schema = SaveTask.avro_schema_to_python()
            response_bytes = avro_serialize(save_task.to_dict(), response_schema)

            await broker.publish(response_bytes, topic=topics["task_responses"])
            logger.info(f"Published response to {topics['task_responses']}")

        except Exception as e:
            logger.error(f"Error processing task request: {e}", exc_info=True)

            error_response = {
                "error": str(e),
                "original_request": str(obj) if "obj" in locals() else "N/A",
                "status": "failed",
            }

    #          await broker.publish(
    #             str(error_response).encode(), topic=topics["task_errors"]
    #        )
    #       logger.error(f"Sent error to {topics['task_errors']}")

    logger.info(f"Consumer registered for topic: {topics['task_requests']}")
    logger.info(f"Group ID: {kafka_config['consumer']['group_id']}")
