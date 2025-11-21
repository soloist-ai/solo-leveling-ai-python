import logging
from tenacity import (
    retry,
    stop_after_attempt,
    retry_if_exception_type,
    before_sleep_log,
    after_log,
)
from src.prompt.task_prompt import generate_task_user_prompt
from src.models.generate_task_response import Task
from src.services.task_validator import TaskValidator, TaskValidationError
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
        retry=retry_if_exception_type(TaskValidationError),
        before_sleep=before_sleep_log(logger, logging.WARNING),
        after=after_log(logger, logging.INFO),
    )
    def generate_task(self, topics: list[TaskTopic], rarity: Rarity) -> Task:
        user_input = generate_task_user_prompt(topics, rarity)
        task = self.chat_client.invoke(input=user_input)
        self.validator.validate_or_raise(task, rarity)
        return task
