import random
from typing import cast

from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.rarity import Rarity
from src.prompt.topic_prompts import TOPIC_PROMPT_MAP, DEFAULT_TOPIC_PROMPT
from src.prompt.topic_scenarios import (
    TOPIC_SCENARIOS_MAP,
    SCENARIO_CONTEXT_MAP,
    add_diversity_hint,
)


class PromptService:
    def __init__(self):
        self._topic_map = TOPIC_PROMPT_MAP
        self._scenario_map = TOPIC_SCENARIOS_MAP

    def _get_topic_instruction(self, topic: TaskTopic) -> str:
        """Получить инструкцию для конкретного топика"""
        return self._topic_map.get(topic, DEFAULT_TOPIC_PROMPT)

    def _get_random_scenario(self, topics: list[TaskTopic]) -> str:
        """
        Получить случайный сценарий, подходящий для всех указанных топиков.
        Если топиков несколько - берём пересечение сценариев.
        """
        ALL_SCENARIOS = list(SCENARIO_CONTEXT_MAP.keys())
        if not topics:
            return random.choice(ALL_SCENARIOS)

        if len(topics) == 1:
            scenarios = self._scenario_map.get(topics[0], ALL_SCENARIOS)
            return random.choice(scenarios)

        common_scenarios = set(self._scenario_map.get(topics[0], ALL_SCENARIOS))
        for topic in topics[1:]:
            topic_scenarios = set(self._scenario_map.get(topic, ALL_SCENARIOS))
            common_scenarios &= topic_scenarios

        scenarios_to_choose = (
            list(common_scenarios) if common_scenarios else ALL_SCENARIOS
        )
        return random.choice(scenarios_to_choose)

    def _merge_topic_contexts(self, topics: list[TaskTopic]) -> str:
        """Объединяет промпты нескольких топиков в единую инструкцию"""
        if len(topics) == 1:
            return self._get_topic_instruction(topics[0])

        topic_instructions = [
            f"**{topic.value}:**\n{self._get_topic_instruction(topic)}"
            for topic in topics
        ]

        merged_context = f"""**COMBINED TASK ({len(topics)} topics): {', '.join([t.value for t in topics])}**

{chr(10).join(topic_instructions)}

**Integration Rules:**
- Create ONE action combining all topics naturally (not "do X, then Y")
- Distribute attributes based on both topics' contributions
- Match scenario context
- Never copy provided examples (vary albums, numbers, activities)
"""
        return merged_context

    def _extract_section(self, text: str, section_marker: str) -> str:
        """Извлекает секцию из промпта топика (от маркера до следующего **...)"""
        if section_marker not in text:
            return ""

        start_idx = text.find(section_marker)

        next_section_idx = text.find("\n**", start_idx + len(section_marker))
        if next_section_idx == -1:
            section_text = text[start_idx:].strip()
        else:
            section_text = text[start_idx:next_section_idx].strip()

        lines = section_text.split("\n")
        return "\n".join(lines[:8]) if len(lines) > 8 else section_text

    def construct_user_prompt(self, topics: list[TaskTopic], rarity: Rarity) -> str:
        """
        Динамически собирает USER PROMPT
        """
        scenario = self._get_random_scenario(topics)

        topic_context = self._merge_topic_contexts(topics)
        diversity_hint = add_diversity_hint(topics[0]) if topics else ""
        scenario_info = SCENARIO_CONTEXT_MAP.get(scenario, {})
        scenario_description = scenario_info.get("description", "")
        scenario_intensity = scenario_info.get("intensity", "")
        scenario_context = cast(dict[str, str], scenario_info.get("context", {}))
        topic_scenario_hints: list[str] = []
        for topic in topics:
            if topic in scenario_context:
                topic_scenario_hints.append(
                    f"  • {topic.value}: {scenario_context[topic]}"
                )
            elif "general" in scenario_context:
                topic_scenario_hints.append(f"  • {scenario_context['general']}")

        scenario_block = ""
        if scenario_description or topic_scenario_hints:
            scenario_block = f"""
                **SCENARIO CONTEXT: {scenario}**
                Description: {scenario_description}
                Required intensity/energy: {scenario_intensity}
                
                **How this scenario applies to your topics:**
                {chr(10).join(topic_scenario_hints[:2]) if topic_scenario_hints else "General scenario context applies."}
                
                ⚠️ YOU MUST adapt the task to match this scenario's intensity and context.
                """

        user_prompt = f"""You are generating a task for a gamification system.


{scenario_block}

**Required Parameters:**
- Topics: {[t.value for t in topics]}
- Rarity: {rarity.value}

{topic_context}
{diversity_hint}

**Task Requirements:**
- Include specific numbers (quantities, durations, counts) where applicable
- Make the task realistic and achievable in the given scenario
- Output ONLY valid JSON matching the schema


Generate a unique, creative task that perfectly integrates all topics into the scenario context.
"""

        return user_prompt
