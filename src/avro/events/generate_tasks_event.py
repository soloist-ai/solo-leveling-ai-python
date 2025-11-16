from dataclasses import dataclass
from typing import List, Optional

from src.avro.enums.rarity import Rarity
from src.avro.enums.task_topic import TaskTopic


@dataclass
class GenerateTask:
    taskId: str
    version: int = 0
    rarity: Optional[Rarity] = None
    topics: Optional[List[TaskTopic]] = None

    def to_dict(self) -> dict:
        result = {
            "taskId": self.taskId,
            "version": self.version,
            "rarity": self.rarity.value if self.rarity else None,
            "topics": [t.value for t in self.topics] if self.topics else [],
        }
        return result

    @classmethod
    def from_dict(cls, data: dict) -> "GenerateTask":
        return cls(
            taskId=data["taskId"],
            version=data.get("version", 0),
            rarity=Rarity(data["rarity"]) if data.get("rarity") else None,
            topics=[TaskTopic(t) for t in data["topics"]] if data.get("topics") else [],
        )


@dataclass
class GenerateTasksEvent:
    txId: Optional[str] = None
    playerId: Optional[int] = None
    inputs: Optional[List[GenerateTask]] = None

    def to_dict(self) -> dict:
        result = {
            "txId": self.txId,
            "playerId": self.playerId,
            "inputs": [task.to_dict() for task in self.inputs] if self.inputs else [],
        }
        return result

    @classmethod
    def from_dict(cls, data: dict) -> "GenerateTasksEvent":
        return cls(
            txId=data.get("txId"),
            playerId=data.get("playerId"),
            inputs=(
                [GenerateTask.from_dict(t) for t in data["inputs"]]
                if data.get("inputs")
                else []
            ),
        )
