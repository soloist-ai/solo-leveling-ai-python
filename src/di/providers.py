from aiokafka import AIOKafkaProducer
from dishka import Provider, provide, Scope
from langchain_openai import ChatOpenAI
from src.config.ai_config import create_llm
from src.config.config_loader import config, get_kafka_bootstrap_servers
from src.services.prompt_service import PromptService
from src.services.task_service import TaskService
from typing import AsyncIterator


class ConfigProvider(Provider):
    @provide(scope=Scope.APP)
    def get_config(self) -> dict:
        return config


class LLMProvider(Provider):
    @provide(scope=Scope.APP)
    def get_llm(self) -> ChatOpenAI:
        return create_llm()


class TaskServiceProvider(Provider):
    @provide(scope=Scope.APP)
    def get_prompt_service(self) -> PromptService:
        return PromptService()

    @provide(scope=Scope.APP)
    def get_task_service(
        self, llm: ChatOpenAI, prompt_service: PromptService
    ) -> TaskService:
        return TaskService(llm, prompt_service)


class ProducerProvider(Provider):
    @provide(scope=Scope.APP)
    async def get_kafka_producer(self) -> AsyncIterator[AIOKafkaProducer]:
        producer = AIOKafkaProducer(bootstrap_servers=get_kafka_bootstrap_servers())
        await producer.start()
        try:
            yield producer
        finally:
            await producer.stop()
