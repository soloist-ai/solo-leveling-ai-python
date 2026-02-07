# test_motion.py
import asyncio
from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.rarity import Rarity
from src.services.task_service import TaskService
from src.services.prompt_service import PromptService
from src.config.ai_config import create_llm

async def main():
    llm = create_llm()
    service = TaskService(llm, PromptService())
    task = service.generate_task([TaskTopic.MOTION], Rarity.COMMON)
    print(f"\n{task.title.en}\n{task.description.en}\n")

asyncio.run(main())