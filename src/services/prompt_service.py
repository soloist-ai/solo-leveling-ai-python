"""
Сервис для построения промптов из готовых шаблонов.
Логика: получаем готовые промпты из хэшмапы, модель не знает о topics/rarity.
"""

import random
from typing import cast

from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.rarity import Rarity
from src.prompt.topic_scenarios import (
    TOPIC_SCENARIOS_MAP,
    SCENARIO_CONTEXT_MAP,
)
from src.prompt.topic_prompts import get_requirements


class PromptService:
    """Сервис для построения user prompts из готовых шаблонов."""

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

        if len(topics) == 1:
            scenarios = self._scenario_map.get(topics[0], ALL_SCENARIOS)
            return random.choice(scenarios)

        # Multiple topics - ищем пересечение сценариев
        common_scenarios = set(self._scenario_map.get(topics[0], ALL_SCENARIOS))
        for topic in topics[1:]:
            topic_scenarios = set(self._scenario_map.get(topic, ALL_SCENARIOS))
            common_scenarios &= topic_scenarios

        scenarios_to_choose = (
            list(common_scenarios) if common_scenarios else ALL_SCENARIOS
        )

        return random.choice(scenarios_to_choose)

    def get_scenario_info(self, scenario: str) -> dict:
        """Получить детальную информацию о сценарии."""
        return SCENARIO_CONTEXT_MAP.get(scenario, {})

    def build_user_prompt(self, topics: list[TaskTopic], rarity: Rarity) -> str:
        """
        Строит финальный user prompt из готовых шаблонов (хэшмапа).

        Модель НЕ получает информацию о topics/rarity как метаданные.
        Вместо этого она получает готовый промпт с конкретными инструкциями.

        Args:
            topics: Список топиков задачи
            rarity: Редкость задачи

        Returns:
            Готовый user prompt для отправки в LLM
        """
        # Получаем сценарий
        scenario = self.get_random_scenario(topics)
        scenario_info = self.get_scenario_info(scenario)

        # Получаем готовые промпты из хэшмапы
        topic_prompts = []
        for topic in topics:
            prompt = get_requirements(topic, rarity)
            if prompt:
                topic_prompts.append(prompt.strip())

        if not topic_prompts:
            raise ValueError(
                f"No prompts found for topics {topics} and rarity {rarity}"
            )

        # Single topic - простой случай
        if len(topics) == 1:
            user_prompt = self._build_single_topic_prompt(
                topic_prompts[0], scenario, scenario_info
            )
        # Multiple topics - объединяем с integration rules
        else:
            user_prompt = self._build_multi_topic_prompt(
                topic_prompts, topics, scenario, scenario_info
            )

        return user_prompt

    def _build_single_topic_prompt(
        self, topic_prompt: str, scenario: str, scenario_info: dict
    ) -> str:
        """Строит промпт для одного топика."""

        scenario_description = scenario_info.get("description", "")
        scenario_intensity = scenario_info.get("intensity", "flexible")

        scenario_block = ""
        if scenario_description:
            scenario_block = f"""
**Scenario: {scenario}**
{scenario_description}
Required intensity: {scenario_intensity}

"""

        user_prompt = f"""{scenario_block}{topic_prompt}

**Final requirements:**
- Generate title and description in BOTH English and Russian
- Include concrete numbers (duration OR counts)
- Match the scenario context and intensity
- Output ONLY valid JSON, no commentary
"""
        return user_prompt

    def _build_multi_topic_prompt(
        self,
        topic_prompts: list[str],
        topics: list[TaskTopic],
        scenario: str,
        scenario_info: dict,
    ) -> str:
        """Строит промпт для нескольких топиков с integration rules."""

        scenario_description = scenario_info.get("description", "")
        scenario_intensity = scenario_info.get("intensity", "flexible")
        scenario_context = cast(dict[str, str], scenario_info.get("context", {}))

        # Scenario block
        scenario_block = ""
        if scenario_description:
            scenario_hints = []
            for topic in topics:
                hint = scenario_context.get(topic.value) or scenario_context.get(
                    "general"
                )
                if hint:
                    scenario_hints.append(f"  • {topic.value}: {hint}")

            hints_text = (
                "\n".join(scenario_hints[:2])
                if scenario_hints
                else "General scenario applies"
            )

            scenario_block = f"""
**Scenario: {scenario}**
{scenario_description}
Intensity: {scenario_intensity}

{hints_text}

"""

        # Requirements для каждого топика
        requirements_blocks = []
        for i, prompt in enumerate(topic_prompts, 1):
            requirements_blocks.append(f"**Activity {i} requirements:**\n{prompt}")

        requirements_text = "\n\n".join(requirements_blocks)

        # Integration rules
        integration_examples = self._get_integration_examples(topics)

        user_prompt = f"""{scenario_block}Generate a combined task that integrates multiple activities:

{requirements_text}

**CRITICAL INTEGRATION RULES:**

❌ FORBIDDEN patterns (task will be rejected):
- "Do X, then Y" or "Do X. Afterwards, Y"
- "First do X, followed by Y"
- Any description implying separate sequential phases

✅ REQUIRED pattern (simultaneous execution):
- "Do X while Y"
- "Do X during Y"  
- "Combine X and Y in one session"

{integration_examples}

**Your task:**
1. Create ONE action combining all activities naturally
2. Activities MUST happen simultaneously, NOT sequentially
3. Include concrete numbers for all activities
4. Generate title and description in BOTH English and Russian
5. Output ONLY valid JSON, no commentary
"""
        return user_prompt

    def _get_integration_examples(self, topics: list[TaskTopic]) -> str:
        """Возвращает примеры интеграции для конкретной комбинации топиков."""

        # Проверяем специфические комбинации
        if TaskTopic.PHYSICAL_ACTIVITY in topics and TaskTopic.MUSIC in topics:
            return """
**Integration examples:**
- ✅ "Do 50-minute HIIT workout while listening to Portishead - Dummy album (11 tracks)"
- ✅ "Run for 45 minutes while full album plays in headphones"
- ❌ "Do workout for 30 minutes. Then listen to music for 45 minutes" ← WRONG
"""

        if TaskTopic.PHYSICAL_ACTIVITY in topics and TaskTopic.SOCIAL_SKILLS in topics:
            return """
**Integration examples:**
- ✅ "Partner workout 50 min: do squats and push-ups together while discussing philosophy between sets"
- ✅ "Group fitness class 60 min: exercises combined with social interaction with participants"
- ❌ "Do exercises for 45 minutes. Afterwards, have conversation" ← WRONG
"""

        if TaskTopic.READING in topics and TaskTopic.MUSIC in topics:
            return """
**Integration examples:**
- ✅ "Read 45-minute article while instrumental album plays in background"
- ✅ "Study 60-minute text accompanied by ambient music playlist"
- ❌ "Read for 30 minutes. Then listen to music for 45 minutes" ← WRONG
"""

        # Default для остальных комбинаций
        return """
**Integration examples:**
- ✅ "Do activity A while activity B happens simultaneously"
- ✅ "Combine activities A and B in one continuous session"
- ❌ "Do A, then do B" ← WRONG
"""
