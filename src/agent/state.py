from typing import TypedDict, Optional, List
from src.models.generate_task_response import Task
from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.rarity import Rarity

AgentState = TypedDict(
    "AgentState",
    {
        "topics": List[TaskTopic],
        "rarity": Rarity,
        "current_task": Optional[Task],
        "critique_feedback": Optional[str],
        "attempt_count": int,
    },
)
