from dataclasses import dataclass
from typing import List, Optional

from src.avro.enums.rarity import Rarity
from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.localization_item import LocalizationItem
from src.models.generate_task_response import Task as PydanticTask


@dataclass
class Task:
    id: Optional[str] = None
    version: Optional[int] = None
    title: Optional[LocalizationItem] = None
    description: Optional[LocalizationItem] = None
    experience: Optional[int] = None
    currencyReward: Optional[int] = None
    rarity: Optional[Rarity] = None
    topics: Optional[List[TaskTopic]] = None
    agility: Optional[int] = None
    strength: Optional[int] = None
    intelligence: Optional[int] = None

    def to_dict(self) -> dict:
        result = {
            "id": self.id,
            "version": self.version,
            "title": self.title.to_dict() if self.title else None,
            "description": self.description.to_dict() if self.description else None,
            "experience": self.experience,
            "currencyReward": self.currencyReward,
            "rarity": self.rarity.value if self.rarity else None,
            "topics": [t.value for t in self.topics] if self.topics else [],
            "agility": self.agility,
            "strength": self.strength,
            "intelligence": self.intelligence,
        }
        return result

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(
            id=data.get("id"),
            version=data.get("version"),
            title=(
                LocalizationItem.from_dict(data["title"]) if data.get("title") else None
            ),
            description=(
                LocalizationItem.from_dict(data["description"])
                if data.get("description")
                else None
            ),
            experience=data.get("experience"),
            currencyReward=data.get("currencyReward"),
            rarity=Rarity(data["rarity"]) if data.get("rarity") else None,
            topics=[TaskTopic(t) for t in data["topics"]] if data.get("topics") else [],
            agility=data.get("agility"),
            strength=data.get("strength"),
            intelligence=data.get("intelligence"),
        )

    @classmethod
    def from_generated(cls, task_data: "Task", result_task: PydanticTask) -> "Task":
        return cls(
            id=task_data.id,
            version=task_data.version,
            rarity=task_data.rarity,
            topics=task_data.topics if task_data.topics else [],
            title=LocalizationItem(en=result_task.title.en, ru=result_task.title.ru),
            description=LocalizationItem(
                en=result_task.description.en, ru=result_task.description.ru
            ),
            experience=result_task.experience,
            currencyReward=result_task.currencyReward,
            agility=result_task.agility,
            strength=result_task.strength,
            intelligence=result_task.intelligence,
        )
