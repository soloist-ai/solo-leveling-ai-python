import logging
from tenacity import (
    retry,
    stop_after_attempt,
    before_sleep_log,
    after_log,
    wait_exponential,
)
from src.prompt.task_prompt import generate_task_user_prompt
from src.models.generate_task_response import Task
from src.services.task_validator import TaskValidator
from langchain_core.runnables import Runnable
from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.rarity import Rarity

logger = logging.getLogger(__name__)


class TaskService:
    def __init__(self, chat_client: Runnable):
        self.chat_client = chat_client
        self.validator = TaskValidator()

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        before_sleep=before_sleep_log(logger, logging.WARNING),
        after=after_log(logger, logging.INFO),
    )
    def _normalize_attributes(self, task: Task, rarity: Rarity) -> Task:
        rules = TaskValidator.RARITY_RULES.get(rarity)
        if not rules:
            return task

        max_limit = rules["max_attributes"]

        current_sum = task.agility + task.strength + task.intelligence

        if current_sum <= max_limit:
            return task

        ratio = max_limit / current_sum

        new_agility = int(task.agility * ratio)
        new_strength = int(task.strength * ratio)
        new_intelligence = int(task.intelligence * ratio)

        new_sum = new_agility + new_strength + new_intelligence
        remainder = max_limit - new_sum

        if remainder > 0:
            if new_strength >= new_agility and new_strength >= new_intelligence:
                new_strength += remainder
            elif new_agility >= new_strength and new_agility >= new_intelligence:
                new_agility += remainder
            else:
                new_intelligence += remainder

        task.agility = new_agility
        task.strength = new_strength
        task.intelligence = new_intelligence

        logger.info(
            f"Attributes normalized for {rarity}: Old Sum={current_sum} -> New Sum={max_limit}"
        )
        return task

    def generate_task(self, topics: list[TaskTopic], rarity: Rarity) -> Task:
        user_input = generate_task_user_prompt(topics, rarity)
        task = self.chat_client.invoke(input=user_input)
        task = self._normalize_attributes(task, rarity)
        self.validator.validate_or_raise(task, rarity)
        return task
