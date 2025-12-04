from src.models.generate_task_response import Task
from src.avro.enums.rarity import Rarity
from typing import Optional, TypedDict


class TaskValidationError(Exception):
    pass


class RarityRule(TypedDict):
    experience_range: tuple[int, int]
    max_attributes: int
    min_attributes: int


class TaskValidator:
    RARITY_RULES: dict[Rarity, RarityRule] = {
        Rarity.COMMON: {
            "experience_range": (10, 20),
            "max_attributes": 2,
            "min_attributes": 2,
        },
        Rarity.UNCOMMON: {
            "experience_range": (40, 50),
            "max_attributes": 5,
            "min_attributes": 4,
        },
        Rarity.RARE: {
            "experience_range": (90, 100),
            "max_attributes": 10,
            "min_attributes": 8,
        },
        Rarity.EPIC: {
            "experience_range": (140, 160),
            "max_attributes": 15,
            "min_attributes": 12,
        },
        Rarity.LEGENDARY: {
            "experience_range": (220, 250),
            "max_attributes": 20,
            "min_attributes": 18,
        },
    }

    @classmethod
    def validate_task(cls, task: Task, rarity: Rarity) -> Optional[str]:
        rules = cls.RARITY_RULES.get(rarity)
        if not rules:
            return f"Unknown rarity: {rarity}"

        exp_min, exp_max = rules["experience_range"]
        if task.experience is None:
            return f"Experience is required for {rarity}"
        if not (exp_min <= task.experience <= exp_max):
            return (
                f"Experience {task.experience} out of range for {rarity}: "
                f"expected {exp_min}-{exp_max}"
            )

        if task.experience is None:
            return f"Experience is required for {rarity}"
        expected_reward = task.experience // 2
        if task.currencyReward != expected_reward:
            return (
                f"Currency reward {task.currencyReward} incorrect: "
                f"expected {expected_reward} (experience / 2)"
            )

        if task.agility is None or task.strength is None or task.intelligence is None:
            return "All attributes (agility, strength, intelligence) are required"
        total_attributes = task.agility + task.strength + task.intelligence
        max_attributes = rules["max_attributes"]
        if total_attributes > max_attributes:
            return (
                f"Total attributes {total_attributes} exceeds maximum "
                f"{max_attributes} for {rarity}"
            )

        min_attributes = rules["min_attributes"]
        if total_attributes < min_attributes:
            return (
                f"Total attributes {total_attributes} below minimum "
                f"{min_attributes} for {rarity}. "
                f"Higher rarity tasks should grant more attribute points."
            )

        for attr_name, attr_value in [
            ("agility", task.agility),
            ("strength", task.strength),
            ("intelligence", task.intelligence),
        ]:
            if not (0 <= attr_value <= 20):
                return f"{attr_name.capitalize()} {attr_value} out of range 0-20"

        if not task.title or not task.title.ru or not task.title.en:
            return "Title missing Russian or English localization"

        if not task.description or not task.description.ru or not task.description.en:
            return "Description missing Russian or English localization"

        return None
