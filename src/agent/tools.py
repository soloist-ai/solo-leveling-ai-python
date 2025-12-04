from typing import Annotated
from langchain_core.tools import tool
from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.rarity import Rarity
from src.prompt.topic_prompts import get_requirements


@tool
def get_task_requirements(
        topic: Annotated[TaskTopic, "The topic of the task to generate"],
        rarity: Annotated[Rarity, "The rarity/difficulty level of the task"]
) -> str:
    """
    Get specific requirements for a task based on topic and rarity.
    Returns detailed guidelines including duration/count, complexity, examples, and integration rules.

    ALWAYS call this tool FIRST before generating a task to get accurate requirements.
    """
    return get_requirements(topic, rarity)
