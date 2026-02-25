from typing import List, Optional

from pydantic import BaseModel

from src.avro.enums.localization_item import LocalizationItem
from src.avro.enums.rarity import Rarity
from src.avro.enums.task_topic import TaskTopic
from src.models.generate_task_response import Task as PydanticTask


class Task(BaseModel):
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

    def apply_generated(self, result_task: PydanticTask) -> None:
        self.title = LocalizationItem(en=result_task.title.en, ru=result_task.title.ru)
        self.description = LocalizationItem(
            en=result_task.description.en, ru=result_task.description.ru
        )
        self.experience = result_task.experience
        self.currencyReward = result_task.currencyReward
        self.agility = result_task.agility
        self.strength = result_task.strength
        self.intelligence = result_task.intelligence
