from typing import Optional

from pydantic import BaseModel
from src.avro.enums.localization_item import LocalizationItem


class Task(BaseModel):
    title: LocalizationItem
    description: LocalizationItem
    experience: Optional[int] = None
    currencyReward: Optional[int] = None
    agility: int
    strength: int
    intelligence: int
