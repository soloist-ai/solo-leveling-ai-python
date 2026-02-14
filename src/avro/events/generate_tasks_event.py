from dataclasses import dataclass
from typing import List, Optional


from src.avro.events.task import Task


@dataclass
class GenerateTasksEvent:
    txId: Optional[str] = None
    userId: Optional[int] = None
    tasks: Optional[List[Task]] = None

    def to_dict(self) -> dict:
        result = {
            "txId": self.txId,
            "userId": self.userId,
            "tasks": [task.to_dict() for task in self.tasks] if self.tasks else [],
        }
        return result

    @classmethod
    def from_dict(cls, data: dict) -> "GenerateTasksEvent":
        return cls(
            txId=data.get("txId"),
            userId=data.get("userId"),
            tasks=(
                [Task.from_dict(t) for t in data["tasks"]] if data.get("tasks") else []
            ),
        )
