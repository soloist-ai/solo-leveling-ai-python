from aiokafka import AIOKafkaProducer
from src.avro.events.generate_tasks_event import GenerateTask
from src.services.avro_serialization import avro_serialize
from src.config.kafka_config import topics


async def send_task_request(producer: AIOKafkaProducer, task: GenerateTask):
    """Отправляет запрос на генерацию задачи в Kafka"""
    try:
        schema = GenerateTask.avro_schema_to_python()
        data = avro_serialize(task.to_dict(), schema)
        await producer.send_and_wait(topics["task_requests"], data)
    except Exception:
        raise
