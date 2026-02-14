import asyncio
import logging
from typing import List, Dict, Tuple
from collections import defaultdict

from aiokafka import AIOKafkaProducer
from dishka import FromDishka
from faststream import Context
from faststream.kafka import KafkaBroker
from faststream.kafka.message import KafkaMessage

from src.kafka.interceptors import ConsumerLocaleInterceptor
from src.kafka.producer import send_save_tasks_event
from src.services.task_service import TaskService
from src.services.avro_serialization import ConfluentAvroService
from src.avro.events.save_tasks_event import SaveTasksEvent
from src.avro.events.generate_tasks_event import GenerateTasksEvent
from src.avro.events.task import Task
from src.avro.enums.rarity import Rarity
from src.avro.enums.task_topic import TaskTopic
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
    async def handle_task_request(
        task_service: FromDishka[TaskService],
        producer: FromDishka[AIOKafkaProducer],
        msg: KafkaMessage = Context("message"),
    ):
        try:
            message = msg.body
            ConsumerLocaleInterceptor.process_message(msg)

            event_dict = confluent_avro.deserialize(
                message, SUBJECTS["generate_tasks_event"]
            )

            event = GenerateTasksEvent.from_dict(event_dict)

            if not event.tasks:
                logger.warning(
                    f"Received empty task list for player {event.userId}, txId={event.txId}"
                )
                return

            logger.info(
                f"Received GenerateTasksEvent: userId={event.userId}, "
                f"txId={event.txId}, tasks_count={len(event.tasks)}"
            )

            if is_feature_enabled("debug_logging"):
                logger.debug(f"Full event data: {event}")

            # Группируем задачи по (topics, rarity) для batch-обработки
            task_groups = group_tasks_by_params(event.tasks)

            logger.info(
                f"Grouped {len(event.tasks)} tasks into {len(task_groups)} batch groups"
            )

            # Обрабатываем каждую группу батчем
            save_tasks: List[Task] = []

            # В handle_task_request(), после группировки:

            for group_key, group_tasks in task_groups.items():
                topics_tuple, rarity = group_key
                topics_list = list(topics_tuple)

                logger.info(
                    f"Processing batch: {len(group_tasks)} tasks with "
                    f"topics={[t.value for t in topics_list]}, rarity={rarity.value}"
                )

                if len(group_tasks) == 1:
                    logger.info(
                        "Single task detected, using agent workflow with critique"
                    )

                    generated_task = await asyncio.to_thread(
                        task_service.generate_task,  # Старый метод с critic
                        topics=topics_list,
                        rarity=rarity,
                    )

                    task_input = group_tasks[0]
                    save_task = Task.from_generated(task_input, generated_task)
                    save_tasks.append(save_task)

                    logger.info(
                        f"Generated single task '{generated_task.title.en}' -> taskId={task_input.id}"
                    )
                else:
                    # Batch-генерация для 2+ задач
                    logger.info("Multiple tasks detected, using batch generation")

                    generated_tasks = await asyncio.to_thread(
                        task_service.generate_tasks_batch,
                        count=len(group_tasks),
                        topics=topics_list,
                        rarity=rarity,
                    )

                    # Мапим сгенерированные задачи на исходные taskId
                    for task_input, generated_task in zip(group_tasks, generated_tasks):
                        save_task = Task.from_generated(task_input, generated_task)
                        save_tasks.append(save_task)

                        logger.info(
                            f"Mapped generated task '{generated_task.title.en}' -> taskId={task_input.id}"
                        )

            logger.info(
                f"Successfully generated {len(save_tasks)} tasks in {len(task_groups)} batch(es)"
            )

            # Отправляем результат
            save_event = SaveTasksEvent(
                txId=event.txId, userId=event.userId, tasks=save_tasks
            )

            await send_save_tasks_event(producer, save_event)

            logger.info(
                f"Published SaveTasksEvent: userId={event.userId}, "
                f"txId={event.txId}, tasks_count={len(save_tasks)}"
            )

        except Exception as e:
            logger.error(f"Error processing task request: {e}", exc_info=True)

    logger.info(f"Consumer registered for topic: {topics['task_requests']}")


def group_tasks_by_params(
    tasks: List[Task],
) -> Dict[Tuple[Tuple[TaskTopic, ...], Rarity], List[Task]]:
    """
    Группирует задачи по (topics, rarity) для batch-обработки.

    Args:
        tasks: Список входящих задач

    Returns:
        Словарь {(topics_tuple, rarity): [список задач с этими параметрами]}
    """
    groups: Dict[Tuple[Tuple[TaskTopic, ...], Rarity], List[Task]] = defaultdict(list)

    for task_input in tasks:
        # Создаем ключ для группировки
        topics_tuple = tuple(sorted(task_input.topics or [], key=lambda t: t.value))
        rarity = task_input.rarity if task_input.rarity is not None else Rarity.COMMON

        group_key = (topics_tuple, rarity)
        groups[group_key].append(task_input)

    return dict(groups)
