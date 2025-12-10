import logging
from typing import List, cast

from langchain_openai import ChatOpenAI

from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    before_sleep_log,
    after_log,
)

from src.models.generate_task_response import Task, TaskBatch
from src.services.prompt_service import PromptService
from src.agent.workflow import create_agent_graph
from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.rarity import Rarity

logger = logging.getLogger(__name__)


class TaskService:
    def __init__(self, llm: ChatOpenAI, prompt_service: PromptService):
        self.prompt_service = prompt_service
        self.agent_app = create_agent_graph(llm, prompt_service)
        self.llm = llm

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        before_sleep=before_sleep_log(logger, logging.WARNING),
        after=after_log(logger, logging.INFO),
    )
    def generate_task(self, topics: list[TaskTopic], rarity: Rarity) -> Task:
        """Генерирует одну задачу через agent workflow"""
        initial_state = {
            "topics": topics,
            "rarity": rarity,
            "attempt_count": 0,
            "critique_feedback": None,
            "current_task": None,
        }

        logger.info(
            f"Starting Agent Loop for topics: {[t.value for t in topics]}, rarity: {rarity.value}"
        )

        final_state = self.agent_app.invoke(initial_state)
        final_task = final_state["current_task"]

        if final_state.get("critique_feedback"):
            logger.warning(
                f"Task finalized with unresolved critique after {final_state['attempt_count']} attempts: "
                f"{final_state['critique_feedback']}"
            )

        logger.info(f"Task generation completed: {final_task.title.en}")
        return final_task

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        before_sleep=before_sleep_log(logger, logging.WARNING),
        after=after_log(logger, logging.INFO),
    )
    def generate_tasks_batch(
        self, count: int, topics: list[TaskTopic], rarity: Rarity
    ) -> List[Task]:
        """
        Генерирует несколько задач за один запрос к LLM.

        Args:
            count: Количество задач для генерации
            topics: Список тем задач
            rarity: Редкость задач

        Returns:
            Список сгенерированных задач
        """
        logger.info(
            f"Starting BATCH generation: count={count}, "
            f"topics={[t.value for t in topics]}, rarity={rarity.value}"
        )

        # Получаем промпт для batch-генерации
        batch_prompt = self.prompt_service.get_batch_system_prompt(count)
        batch_user_prompt = self.prompt_service.build_batch_user_prompt(
            count, topics, rarity
        )

        # Вызываем LLM с structured output
        structured_llm = self.llm.with_structured_output(TaskBatch)

        messages = [
            {"role": "system", "content": batch_prompt},
            {"role": "user", "content": batch_user_prompt},
        ]

        logger.info(f"Invoking LLM for batch generation of {count} tasks")
        result: TaskBatch = cast(TaskBatch, structured_llm.invoke(messages))

        # Валидация количества
        if len(result.tasks) != count:
            logger.warning(
                f"LLM returned {len(result.tasks)} tasks instead of {count}, adjusting..."
            )
            # Берем первые count задач или дополняем если меньше
            if len(result.tasks) > count:
                result.tasks = result.tasks[:count]
            elif len(result.tasks) < count:
                # Если задач меньше, генерируем недостающие по одной
                missing = count - len(result.tasks)
                logger.warning(f"Generating {missing} additional tasks individually")
                for _ in range(missing):
                    additional_task = self.generate_task(topics, rarity)
                    result.tasks.append(additional_task)

        logger.info(f"BATCH generation completed: {count} tasks generated successfully")
        logger.debug(f"Generated tasks: {[t.title.en for t in result.tasks]}")

        return result.tasks
