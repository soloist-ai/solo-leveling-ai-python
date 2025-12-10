from unittest.mock import Mock, MagicMock
from langchain_openai import ChatOpenAI

from src.services.task_service import TaskService
from src.services.prompt_service import PromptService
from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.rarity import Rarity
from src.models.generate_task_response import Task, TaskBatch
from src.avro.enums.localization_item import LocalizationItem


def test_generate_tasks_batch():
    """Тест batch-генерации задач"""

    # Мокаем LLM
    mock_llm = Mock(spec=ChatOpenAI)
    mock_prompt_service = Mock(spec=PromptService)

    # Создаем TaskService
    task_service = TaskService(mock_llm, mock_prompt_service)

    # Настраиваем мок-ответ
    mock_batch = TaskBatch(
        tasks=[
            Task(
                title=LocalizationItem(en="Task 1", ru="Задача 1"),
                description=LocalizationItem(en="Desc 1", ru="Описание 1"),
                agility=10,
                strength=5,
                intelligence=3,
            ),
            Task(
                title=LocalizationItem(en="Task 2", ru="Задача 2"),
                description=LocalizationItem(en="Desc 2", ru="Описание 2"),
                agility=8,
                strength=7,
                intelligence=5,
            ),
            Task(
                title=LocalizationItem(en="Task 3", ru="Задача 3"),
                description=LocalizationItem(en="Desc 3", ru="Описание 3"),
                agility=12,
                strength=6,
                intelligence=4,
            ),
        ]
    )

    mock_structured_llm = MagicMock()
    mock_structured_llm.invoke.return_value = mock_batch
    mock_llm.with_structured_output.return_value = mock_structured_llm

    mock_prompt_service.get_batch_system_prompt.return_value = "batch prompt"
    mock_prompt_service.build_batch_user_prompt.return_value = "user prompt"

    # Вызываем batch-генерацию
    topics = [TaskTopic.PHYSICAL_ACTIVITY, TaskTopic.MUSIC]
    rarity = Rarity.COMMON
    count = 3

    results = task_service.generate_tasks_batch(count, topics, rarity)

    # Проверки
    assert len(results) == 3
    assert results[0].title.en == "Task 1"
    assert results[1].title.en == "Task 2"
    assert results[2].title.en == "Task 3"

    # Проверяем, что LLM вызван ОДИН раз
    mock_structured_llm.invoke.assert_called_once()

    print("✅ Batch generation test passed!")


def test_group_tasks_by_params():
    """Тест группировки задач"""
    from src.kafka.consumer import group_tasks_by_params
    from src.avro.events.generate_tasks_event import GenerateTask

    # Создаем тестовые задачи
    tasks = [
        GenerateTask(
            taskId="1",
            topics=[TaskTopic.PHYSICAL_ACTIVITY, TaskTopic.MUSIC],
            rarity=Rarity.COMMON,
        ),
        GenerateTask(
            taskId="2",
            topics=[TaskTopic.PHYSICAL_ACTIVITY, TaskTopic.MUSIC],
            rarity=Rarity.COMMON,
        ),
        GenerateTask(
            taskId="3",
            topics=[TaskTopic.READING],
            rarity=Rarity.RARE,
        ),
        GenerateTask(
            taskId="4",
            topics=[TaskTopic.PHYSICAL_ACTIVITY, TaskTopic.MUSIC],
            rarity=Rarity.COMMON,
        ),
    ]

    # Группируем
    groups = group_tasks_by_params(tasks)

    # Проверки
    assert len(groups) == 2  # Две группы: (PA+MUSIC, COMMON) и (READING, RARE)

    # Первая группа должна содержать 3 задачи
    group1_key = (
        tuple(
            sorted(
                [TaskTopic.PHYSICAL_ACTIVITY, TaskTopic.MUSIC], key=lambda t: t.value
            )
        ),
        Rarity.COMMON,
    )
    assert len(groups[group1_key]) == 3

    # Вторая группа - 1 задачу
    group2_key = ((TaskTopic.READING,), Rarity.RARE)
    assert len(groups[group2_key]) == 1

    print("✅ Grouping test passed!")


if __name__ == "__main__":
    test_generate_tasks_batch()
    test_group_tasks_by_params()
