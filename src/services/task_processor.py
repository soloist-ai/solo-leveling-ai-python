import logging
import random
from typing import List
from src.avro.enums.rarity import Rarity
from src.avro.enums.task_topic import TaskTopic
from src.models.generate_task_response import Task
from src.services.task_validator import TaskValidator

# Константы из workflow.py
TIME_BASED_TOPICS = {
    TaskTopic.PHYSICAL_ACTIVITY,
    TaskTopic.ADVENTURE,
    TaskTopic.READING,
    TaskTopic.MOTION,
}
logger = logging.getLogger(__name__)


class TaskProcessor:
    """Централизованная обработка числовой логики задач."""

    def __init__(self, validator: TaskValidator):
        self.validator = validator

    def apply_numeric_logic(
        self,
        task: Task,
        rarity: Rarity,
        topics: List[TaskTopic],
    ) -> Task:
        """
        Применяет все детерминистические правила:
        - experience & currency
        - нормализация атрибутов
        - проверка типа метрики
        """
        # 1. Experience & Currency
        task = self._calculate_rewards(task, rarity)

        # 2. Нормализация атрибутов
        task = self._normalize_attributes(task, rarity)

        # 3. Проверка типа метрики (логирование)
        self._validate_metric_type(task, topics)

        return task

    def _calculate_rewards(self, task: Task, rarity: Rarity) -> Task:
        """Детерминистический расчёт опыта и валюты."""
        exp_ranges = {
            Rarity.COMMON: (10, 20),
            Rarity.UNCOMMON: (40, 50),
            Rarity.RARE: (90, 100),
            Rarity.EPIC: (140, 160),
            Rarity.LEGENDARY: (220, 250),
        }

        exp_min, exp_max = exp_ranges[rarity]
        experience = random.randint(exp_min, exp_max)
        currency = experience // 2

        task.experience = experience
        task.currencyReward = currency

        logger.debug(f"Rewards calculated: exp={experience}, currency={currency}")
        return task

    def _normalize_attributes(self, task: Task, rarity: Rarity) -> Task:
        """Нормализует сумму атрибутов под лимит редкости."""
        rules = self.validator.RARITY_RULES.get(rarity)
        if not rules:
            return task

        max_limit = rules["max_attributes"]
        current_sum = task.agility + task.strength + task.intelligence

        if current_sum <= max_limit:
            return task

        # Пропорциональное уменьшение
        ratio = max_limit / current_sum
        new_agility = int(task.agility * ratio)
        new_strength = int(task.strength * ratio)
        new_intelligence = int(task.intelligence * ratio)

        # Остаток добавляем в доминирующий атрибут
        new_sum = new_agility + new_strength + new_intelligence
        remainder = max_limit - new_sum

        if remainder > 0:
            if new_strength >= max(new_agility, new_intelligence):
                new_strength += remainder
            elif new_agility >= max(new_strength, new_intelligence):
                new_agility += remainder
            else:
                new_intelligence += remainder

        task.agility = new_agility
        task.strength = new_strength
        task.intelligence = new_intelligence

        logger.info(f"⚙️ Attributes normalized: {current_sum} → {max_limit}")
        return task

    def _validate_metric_type(self, task: Task, topics: List[TaskTopic]) -> None:
        """Проверяет соответствие типа метрики (TIME vs COMPLEXITY)."""
        is_time_based = any(t in TIME_BASED_TOPICS for t in topics)
        desc_en = task.description.en.lower()
        desc_ru = task.description.ru.lower()

        time_markers_en = ["min", "minutes", "hour", "hours"]
        time_markers_ru = ["минут", "минуты", "час", "часа", "часов"]

        has_time = any(m in desc_en for m in time_markers_en) or any(
            m in desc_ru for m in time_markers_ru
        )

        if is_time_based and not has_time:
            logger.warning(
                f"⚠️ TIME-based topics but no duration in description. "
                f"Task: {task.title.en}"
            )
        elif not is_time_based and has_time:
            logger.warning(
                f"⚠️ COMPLEXITY-based topics but time mentioned. "
                f"Task: {task.title.en}"
            )
