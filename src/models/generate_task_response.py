from typing import Optional
from pydantic import BaseModel, Field

from src.avro.enums.localization_item import LocalizationItem


class Task(BaseModel):
    title: LocalizationItem
    description: LocalizationItem
    experience: Optional[int] = None
    currencyReward: Optional[int] = None
    agility: int
    strength: int
    intelligence: int


class TaskBatch(BaseModel):
    """Модель для batch-генерации нескольких задач"""

    tasks: list[Task] = Field(..., min_length=1, description="List of generated tasks")
