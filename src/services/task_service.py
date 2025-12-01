import logging

from langchain_openai import ChatOpenAI
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    before_sleep_log,
    after_log,
)

from src.models.generate_task_response import Task
from src.services.prompt_service import PromptService
from src.agent.workflow import create_agent_graph
from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.rarity import Rarity

logger = logging.getLogger(__name__)


class TaskService:
    def __init__(self, llm: ChatOpenAI, prompt_service: PromptService):
        self.prompt_service = prompt_service
        self.agent_app = create_agent_graph(llm, prompt_service)

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        before_sleep=before_sleep_log(logger, logging.WARNING),
        after=after_log(logger, logging.INFO),
    )
    def generate_task(self, topics: list[TaskTopic], rarity: Rarity) -> Task:
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
