import asyncio
import logging
from typing import List
from aiokafka import AIOKafkaProducer
from dishka import FromDishka
from dishka.integrations.faststream import inject
from faststream.kafka import KafkaBroker
from faststream.kafka.message import KafkaMessage
from src.kafka.interceptors import ConsumerLocaleInterceptor
from src.kafka.producer import send_save_tasks_event
from src.services.task_service import TaskService
from src.services.avro_serialization import ConfluentAvroService
from src.avro.events.save_tasks_event import SaveTask, SaveTasksEvent
from src.avro.events.generate_tasks_event import GenerateTask, GenerateTasksEvent
from src.avro.enums.rarity import Rarity
from src.config.config_loader import (
    config,
    is_feature_enabled,
    get_schema_registry_url,
    get_kafka_topics,
)

logger = logging.getLogger(__name__)

topics = get_kafka_topics()
SUBJECTS = {
    "generate_tasks_event": "com.sleepkqq.sololeveling.avro.task.GenerateTasksEvent",
    "save_tasks_event": "com.sleepkqq.sololeveling.avro.task.SaveTasksEvent",
}

confluent_avro = ConfluentAvroService(schema_registry_url=get_schema_registry_url())


def register_consumers(broker: KafkaBroker):
    kafka_config = config["kafka"]

    @broker.subscriber(
        topics["task_requests"],
        group_id=kafka_config["consumer"]["group_id"],
        auto_offset_reset=kafka_config["consumer"]["auto_offset_reset"],
        max_workers=kafka_config["consumer"]["max_workers"],
    )
    @inject
    async def handle_task_request(
        body: bytes,
        msg: KafkaMessage,
        task_service: FromDishka[TaskService],
        producer: FromDishka[AIOKafkaProducer],
    ):
        try:
            message = body
            ConsumerLocaleInterceptor.process_message(msg)
            event_dict = confluent_avro.deserialize(
                message, SUBJECTS["generate_tasks_event"]
            )
            event = GenerateTasksEvent.from_dict(event_dict)

            if not event.inputs:
                logger.warning(
                    f"Received empty task list for player {event.playerId}, txId={event.txId}"
                )
                return

            logger.info(
                f"Received GenerateTasksEvent: playerId={event.playerId}, "
                f"txId={event.txId}, tasks_count={len(event.inputs)}"
            )

            if is_feature_enabled("debug_logging"):
                logger.debug(f"Full event data: {event}")

            async def process_single_task(task_input: GenerateTask) -> SaveTask:
                logger.info(f"Processing task: taskId={task_input.taskId}")
                task_rarity = (
                    task_input.rarity
                    if task_input.rarity is not None
                    else Rarity.COMMON
                )

                result_task = await asyncio.to_thread(
                    task_service.generate_task,
                    topics=task_input.topics if task_input.topics else [],
                    rarity=task_rarity,
                )

                logger.info(
                    f"Generated task: {result_task.title.en} (taskId={task_input.taskId})"
                )
                return SaveTask.from_generated(task_input, result_task)

            save_tasks: List[SaveTask] = await asyncio.gather(
                *[process_single_task(task) for task in event.inputs]
            )
            logger.info(f"Successfully generated {len(save_tasks)} tasks")
            save_event = SaveTasksEvent(
                txId=event.txId, playerId=event.playerId, tasks=save_tasks
            )

            await send_save_tasks_event(producer, save_event)

            logger.info(
                f"Published SaveTasksEvent: playerId={event.playerId}, "
                f"txId={event.txId}, tasks_count={len(save_tasks)}"
            )

        except Exception as e:
            logger.error(f"Error processing task request: {e}", exc_info=True)

    logger.info(f"Consumer registered for topic: {topics['task_requests']}")
