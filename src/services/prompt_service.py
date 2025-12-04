import random
from typing import cast

from src.avro.enums.task_topic import TaskTopic
from src.prompt.topic_scenarios import (
    TOPIC_SCENARIOS_MAP,
    SCENARIO_CONTEXT_MAP,
)


class PromptService:
    """Упрощённый сервис - работает только со сценариями."""

    def __init__(self):
        self._scenario_map = TOPIC_SCENARIOS_MAP

    def get_random_scenario(self, topics: list[TaskTopic]) -> str:
        """
        Получить случайный сценарий, подходящий для всех указанных топиков.
        При multiple topics берём пересечение доступных сценариев.
        """
        ALL_SCENARIOS = list(SCENARIO_CONTEXT_MAP.keys())

        if not topics:
            return random.choice(ALL_SCENARIOS)

        # Single topic - берём любой подходящий сценарий
        if len(topics) == 1:
            scenarios = self._scenario_map.get(topics[0], ALL_SCENARIOS)
            return random.choice(scenarios)

        # Multiple topics - ищем пересечение сценариев
        common_scenarios = set(self._scenario_map.get(topics[0], ALL_SCENARIOS))
        for topic in topics[1:]:
            topic_scenarios = set(self._scenario_map.get(topic, ALL_SCENARIOS))
            common_scenarios &= topic_scenarios

        # Если нет общих сценариев, берём из всех доступных
        scenarios_to_choose = (
            list(common_scenarios) if common_scenarios else ALL_SCENARIOS
        )

        return random.choice(scenarios_to_choose)

    def get_scenario_info(self, scenario: str) -> dict:
        """Получить детальную информацию о сценарии."""
        return SCENARIO_CONTEXT_MAP.get(scenario, {})

    def get_scenario_hints_for_topics(
            self,
            scenario: str,
            topics: list[TaskTopic]
    ) -> list[str]:
        """
        Получить scenario-specific hints для конкретных топиков.
        Используется для дополнительного контекста в user prompt.
        """
        scenario_info = self.get_scenario_info(scenario)
        scenario_context = cast(dict[str, str], scenario_info.get("context", {}))

        topic_hints: list[str] = []
        for topic in topics:
            if topic.value in scenario_context:
                hint = scenario_context[topic.value]
                topic_hints.append(f"- {topic.value}: {hint}")

        # Если нет специфичных hints, добавляем general
        if not topic_hints and "general" in scenario_context:
            topic_hints.append(f"- General: {scenario_context['general']}")

        return topic_hints
