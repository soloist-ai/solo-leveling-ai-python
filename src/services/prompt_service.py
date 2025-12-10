import logging
import random
from typing import List

from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.rarity import Rarity
from src.prompt.topic_prompts import get_requirements, get_diversity_hints

logger = logging.getLogger(__name__)


STYLE_VARIATIONS = [
    "technical and precise",
    "motivational and energizing",
    "challenge-focused and competitive",
    "exploratory and experimental",
    "mindful and deliberate",
]


class PromptService:
    """
    Сервис для построения user prompts с diversity hints.

    Основные возможности:
    - Случайный выбор diversity hints для каждого топика
    - Вариативность стиля генерации
    - Поддержка single и multi-topic задач
    """

    def build_user_prompt(self, topics: List[TaskTopic], rarity: Rarity) -> str:

        topic_prompts = []
        for topic in topics:
            prompt = get_requirements(topic, rarity)
            if prompt:
                topic_prompts.append(prompt.strip())

        if not topic_prompts:
            raise ValueError(
                f"No prompts found for topics {topics} and rarity {rarity}"
            )

        diversity_instructions = []
        for topic in topics:
            hints = get_diversity_hints(topic)
            if hints:
                selected_hint = random.choice(hints)
                diversity_instructions.append(f"- {topic.value}: {selected_hint}")

        style = random.choice(STYLE_VARIATIONS)

        if len(topics) == 1:
            user_prompt = self._build_single_topic_prompt(
                topic_prompts[0], diversity_instructions, style
            )
        else:
            user_prompt = self._build_multi_topic_prompt(
                topic_prompts, topics, diversity_instructions, style
            )

        logger.info(f"Built prompt for {[t.value for t in topics]} ({rarity.value})")
        return user_prompt

    def _build_single_topic_prompt(
        self, topic_prompt: str, diversity_instructions: List[str], style: str
    ) -> str:

        diversity_block = (
            "\n".join(diversity_instructions) if diversity_instructions else ""
        )

        return f"""{topic_prompt}

DIVERSITY REQUIREMENTS:
{diversity_block}

Style: Generate task in a {style} tone.

Final requirements:
- Generate title and description in BOTH English and Russian
- Include concrete numbers (duration OR counts)
- Ensure uniqueness and variety
- Output ONLY valid JSON, no commentary
"""

    def _build_multi_topic_prompt(
        self,
        topic_prompts: List[str],
        topics: List[TaskTopic],
        diversity_instructions: List[str],
        style: str,
    ) -> str:

        requirements_blocks = []
        for i, prompt in enumerate(topic_prompts):
            requirements_blocks.append(f"Activity {i+1} requirements:\n{prompt}")

        requirements_text = "\n\n".join(requirements_blocks)

        diversity_block = (
            "\n".join(diversity_instructions) if diversity_instructions else ""
        )

        integration_examples = self._get_integration_examples(topics)

        return f"""Generate a combined task that integrates multiple activities:

{requirements_text}

DIVERSITY REQUIREMENTS:
{diversity_block}

Style: Generate task in a {style} tone.

CRITICAL INTEGRATION RULES:

FORBIDDEN patterns (task will be rejected):
- "Do X, then Y" or "Do X. Afterwards, Y"
- "First do X, followed by Y"
- Any description implying separate sequential phases

REQUIRED pattern (simultaneous execution):
- "Do X while Y"
- "Do X during Y"
- "Combine X and Y in one session"

{integration_examples}

Your task:
1. Create ONE action combining all activities naturally
2. Activities MUST happen simultaneously, NOT sequentially
3. Include concrete numbers for all activities
4. Generate title and description in BOTH English and Russian
5. Ensure uniqueness and variety
6. Output ONLY valid JSON, no commentary
"""

    def _get_integration_examples(self, topics: List[TaskTopic]) -> str:
        """Примеры интеграции для конкретных комбинаций топиков"""

        if TaskTopic.PHYSICAL_ACTIVITY in topics and TaskTopic.MUSIC in topics:
            return """Integration examples:
✓ Do 50-minute HIIT workout while listening to Portishead - Dummy album (11 tracks)
✓ Run for 45 minutes while full album plays in headphones
✗ Do workout for 30 minutes. Then listen to music for 45 minutes (WRONG)"""

        if TaskTopic.PHYSICAL_ACTIVITY in topics and TaskTopic.SOCIAL_SKILLS in topics:
            return """Integration examples:
✓ Partner workout 50 min: do squats and push-ups together while discussing philosophy between sets
✓ Group fitness class 60 min: exercises combined with social interaction with participants
✗ Do exercises for 45 minutes. Afterwards, have conversation (WRONG)"""

        if TaskTopic.READING in topics and TaskTopic.MUSIC in topics:
            return """Integration examples:
✓ Read 45-minute article while instrumental album plays in background
✓ Study 60-minute text accompanied by ambient music playlist
✗ Read for 30 minutes. Then listen to music for 45 minutes (WRONG)"""

        if TaskTopic.READING in topics and TaskTopic.SOCIAL_SKILLS in topics:
            return """Integration examples:
✓ Read article for 25 min, then have 30-min discussion with friend about the ideas
✓ Book club session: read chapter for 40 min, then discuss with group for 45 min
✗ Read alone for 30 minutes. Later talk to friend (WRONG)"""

        if TaskTopic.DEVELOPMENT in topics and TaskTopic.MUSIC in topics:
            return """Integration examples:
✓ Solve 2 medium algorithm problems while listening to ambient album in background
✓ Code for 90 minutes while instrumental music plays (Boards of Canada - MHTRTC)
✗ Solve coding problem. Then listen to music (WRONG)"""

        # Общий пример для остальных комбинаций
        return """Integration examples:
✓ Do activity A while activity B happens simultaneously
✓ Combine activities A and B in one continuous session
✗ Do A, then do B (WRONG)"""
