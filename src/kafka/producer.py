from aiokafka import AIOKafkaProducer

from src.kafka.consumer import confluent_avro
from src.avro.events.save_tasks_event import SaveTasksEvent
from src.config.kafka_config import topics
import logging

logger = logging.getLogger(__name__)

SAVE_TASKS_EVENT_SUBJECT = "com.sleepkqq.sololeveling.avro.task.SaveTasksEvent"


async def send_save_tasks_event(producer: AIOKafkaProducer, event: SaveTasksEvent):
    """
    Отправляет событие SaveTasksEvent в Kafka

    Args:
        producer: Kafka producer
        event: SaveTasksEvent dataclass
    """
    try:
        # Сериализуем dataclass через Schema Registry
        avro_bytes = confluent_avro.serialize(event.to_dict(), SAVE_TASKS_EVENT_SUBJECT)

        # Отправляем в Kafka
        await producer.send_and_wait(
            topics["task_save"],
            value=avro_bytes,
            key=str(event.playerId).encode() if event.playerId else None,
        )

        logger.info(f"✅ Published SaveTasksEvent for player {event.playerId}")

    except Exception as e:
        logger.error(f"Failed to publish SaveTasksEvent: {e}")
        raise
