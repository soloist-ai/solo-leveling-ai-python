from aiokafka import AIOKafkaProducer
from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.task_rarity import TaskRarity
from src.avro.events.generate_tasks_event import GenerateTask
from src.services.avro_serialization import avro_serialize

async def send_task_request(task: GenerateTask):
    producer = AIOKafkaProducer(
        bootstrap_servers="localhost:29092",
    )
    await producer.start()
    try:
        schema = GenerateTask.avro_schema_to_python()
        data = avro_serialize(task.to_dict(), schema)
        await producer.send_and_wait("task.requests", data)
    finally:
        await producer.stop()
