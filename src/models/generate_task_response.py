from pydantic import BaseModel
from src.avro.enums.localization_item import LocalizationItem


class Task(BaseModel):
    title: LocalizationItem
    description: LocalizationItem
    experience: int
    currencyReward: int
    agility: int
    strength: int
    intelligence: int
