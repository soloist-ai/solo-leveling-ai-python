import logging
from aiokafka import AIOKafkaProducer
from src.avro.events.save_tasks_event import SaveTasksEvent
from src.config.config_loader import get_kafka_topics, get_schema_registry_url
from src.kafka.interceptors import ProducerLocaleInterceptor
from src.services.avro_serialization import ConfluentAvroService

topics = get_kafka_topics()
logger = logging.getLogger(__name__)

SAVE_TASKS_EVENT_SUBJECT = "com.sleepkqq.sololeveling.avro.task.SaveTasksEvent"
confluent_avro = ConfluentAvroService(schema_registry_url=get_schema_registry_url())


async def send_save_tasks_event(
    producer: AIOKafkaProducer, save_event: SaveTasksEvent
) -> bool:
    try:
        response_bytes = confluent_avro.serialize(
            save_event.to_dict(), SAVE_TASKS_EVENT_SUBJECT
        )
        headers = ProducerLocaleInterceptor.inject_locale_header()
        await producer.send_and_wait(
            topics["task_responses"],
            value=response_bytes,
            key=str(save_event.txId).encode() if save_event.txId else None,
            headers=headers,
        )

        logger.info(f"Published SaveTasksEvent for player {save_event.userId}")
        return True
    except Exception as e:
        logger.error(
            f"Failed to publish SaveTasksEvent for player {save_event.userId}: {e}",
            exc_info=True,
        )
        return False
