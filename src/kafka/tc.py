import asyncio
import logging
from faststream.kafka import KafkaBroker
from dishka import make_async_container
from dishka.integrations.faststream import setup_dishka
from src.kafka.consumer import register_consumers
from src.di.providers import (
    ConfigProvider,
    LLMProvider,
    TaskServiceProvider,
    FastStreamProvider,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def consume_task_requests():
    # Создаём асинхронный контейнер зависимостей
    container_factory = make_async_container(
        ConfigProvider(),
        LLMProvider(),
        TaskServiceProvider(),
        FastStreamProvider(),
    )

    async with container_factory() as container:
        # Получаем KafkaBroker через DI
        broker = await container.get(KafkaBroker)
        setup_dishka(container=container, broker=broker, auto_inject=True)

        # Регистрируем консьюмеры
        register_consumers(broker)

        # Запускаем брокер
        await broker.start()
        logger.info("✅ Consumer is running. Waiting for messages...")

        try:
            await asyncio.sleep(60)
        finally:
            await broker.stop()
            await container.close()


if __name__ == "__main__":
    asyncio.run(consume_task_requests())
