from dishka import Provider, provide, Scope
from src.config.ai_config import create_chat_client
from src.config.config_loader import config
from faststream.kafka import KafkaBroker
from src.services.task_service import TaskService
from langchain_core.runnables import Runnable
from src.config.kafka_config import kafka_broker


class ConfigProvider(Provider):
    @provide(scope=Scope.APP)
    def get_config(self) -> dict:
        return config


class LLMProvider(Provider):
    @provide(scope=Scope.APP)
    def get_chat_client(self) -> Runnable:
        return create_chat_client()


class TaskServiceProvider(Provider):
    @provide(scope=Scope.APP)
    def get_task_service(self, chat_client: Runnable) -> TaskService:
        return TaskService(chat_client)


class KafkaProvider(Provider):
    @provide(scope=Scope.APP)
    def get_kafka_broker(self) -> KafkaBroker:
        return kafka_broker
