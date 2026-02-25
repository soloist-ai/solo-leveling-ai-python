import asyncio
from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.rarity import Rarity
from src.services.task_service import TaskService
from src.services.prompt_service import PromptService
from src.config.ai_config import create_llm


async def main():
    llm = create_llm()
    service = TaskService(llm, PromptService())
    task = service.generate_task([TaskTopic.ADVENTURE], Rarity.EPIC)

    # Полный вывод всех полей
    print("\n✅ ЗАДАЧА СГЕНЕРИРОВАНА")
    print("=" * 70)
    print(f"Title:      {task.title.en}/{task.title.ru}")
    print(f"Description:{task.description.en}/{task.description.ru}")
    print(
        f"Stats:      AGI={task.agility} | STR={task.strength} | INT={task.intelligence}"
    )
    print(f"Rewards:    EXP={task.experience} | CUR={task.currencyReward}")
    print("=" * 70 + "\n")


asyncio.run(main())
