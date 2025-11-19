import logging
from aiokafka import AIOKafkaProducer
from src.avro.events.save_tasks_event import SaveTasksEvent
from src.config.config_loader import get_kafka_topics, get_schema_registry_url
from src.services.avro_serialization import ConfluentAvroService

topics = get_kafka_topics()
logger = logging.getLogger(__name__)

SAVE_TASKS_EVENT_SUBJECT = "com.sleepkqq.sololeveling.avro.task.SaveTasksEvent"
confluent_avro = ConfluentAvroService(schema_registry_url=get_schema_registry_url())


async def send_save_tasks_event(producer: AIOKafkaProducer, save_event: SaveTasksEvent):
    try:
        response_bytes = confluent_avro.serialize(
            save_event.to_dict(), SAVE_TASKS_EVENT_SUBJECT
        )
        await producer.send_and_wait(
            topics["task_responses"],
            value=response_bytes,
            key=str(save_event.playerId).encode() if save_event.playerId else None,
        )

        logger.info(f"Published SaveTasksEvent for player {save_event.playerId}")

    except Exception as e:
        logger.error(f"Failed to publish SaveTasksEvent: {e}")
        raise
