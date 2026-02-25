import logging
import random
from typing import List

from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.rarity import Rarity
from src.prompt.system_prompt import BATCH_SYSTEM_PROMPT
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
    - Batch-генерация для множественных задач
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

    def build_batch_user_prompt(
        self, count: int, topics: List[TaskTopic], rarity: Rarity
    ) -> str:
        """
        Строит user prompt для batch-генерации count задач.
        Использует те же diversity hints, но с акцентом на разнообразие внутри батча.
        """
        topic_prompts = []
        for topic in topics:
            prompt = get_requirements(topic, rarity)
            if prompt:
                topic_prompts.append(prompt.strip())

        if not topic_prompts:
            raise ValueError(
                f"No prompts found for topics {topics} and rarity {rarity}"
            )

        # Генерируем diversity hints для каждого топика
        diversity_instructions = []
        for topic in topics:
            hints = get_diversity_hints(topic)
            if hints:
                # Для batch берем несколько hints (если возможно)
                selected_hints = random.sample(hints, min(3, len(hints)))
                hints_str = ", ".join(selected_hints)
                diversity_instructions.append(
                    f"- {topic.value}: vary between {hints_str}"
                )

        style = random.choice(STYLE_VARIATIONS)

        if len(topics) == 1:
            user_prompt = self._build_batch_single_topic_prompt(
                count, topic_prompts[0], diversity_instructions, style
            )
        else:
            user_prompt = self._build_batch_multi_topic_prompt(
                count, topic_prompts, topics, diversity_instructions, style
            )

        logger.info(
            f"Built BATCH prompt for {count} tasks: {[t.value for t in topics]} ({rarity.value})"
        )
        return user_prompt

    def get_batch_system_prompt(self, count: int) -> str:
        """Возвращает system prompt для batch-генерации"""
        return BATCH_SYSTEM_PROMPT.format(count=count)

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
- Generate agility, strength, intelligence as integers (0-20)
- Include concrete numbers (duration OR counts)
- Ensure uniqueness and variety
- ALL fields are mandatory
- Output ONLY valid JSON, no commentary
"""

    def _build_batch_single_topic_prompt(
        self,
        count: int,
        topic_prompt: str,
        diversity_instructions: List[str],
        style: str,
    ) -> str:
        """User prompt для batch-генерации single-topic задач"""
        diversity_block = (
            "\n".join(diversity_instructions) if diversity_instructions else ""
        )

        return f"""Generate {count} DIVERSE tasks following these requirements:

{topic_prompt}

DIVERSITY REQUIREMENTS (apply VARIATION across all {count} tasks):
{diversity_block}

Style: Generate tasks in a {style} tone.

CRITICAL: All {count} tasks must be SIGNIFICANTLY DIFFERENT:
- Vary durations/counts across tasks
- Use different activities and approaches
- Avoid repetitive patterns
- Each task should feel unique and fresh

Final requirements for EACH task:
- Generate title and description in BOTH English and Russian
- Include concrete numbers (duration OR counts)
- Generate agility, strength, intelligence as integers (0-20)
- Ensure uniqueness within the batch
- ALL fields are mandatory
- Output ONLY valid JSON with "tasks" array containing {count} task objects
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

    def _build_batch_multi_topic_prompt(
        self,
        count: int,
        topic_prompts: List[str],
        topics: List[TaskTopic],
        diversity_instructions: List[str],
        style: str,
    ) -> str:
        """User prompt для batch-генерации multi-topic задач"""
        requirements_blocks = []
        for i, prompt in enumerate(topic_prompts):
            requirements_blocks.append(f"Activity {i+1} requirements:\n{prompt}")

        requirements_text = "\n\n".join(requirements_blocks)
        diversity_block = (
            "\n".join(diversity_instructions) if diversity_instructions else ""
        )

        integration_examples = self._get_integration_examples(topics)

        return f"""Generate {count} DIVERSE combined tasks that integrate multiple activities:

{requirements_text}

DIVERSITY REQUIREMENTS (apply VARIATION across all {count} tasks):
{diversity_block}

Style: Generate tasks in a {style} tone.

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

CRITICAL: All {count} tasks must be SIGNIFICANTLY DIFFERENT:
- Vary the way topics are combined across tasks
- Use different durations/counts
- Vary integration approaches (e.g., different types of music, different exercises)
- Avoid repetitive patterns
- Each task should feel unique and fresh

Your task:
1. Create {count} DIFFERENT combined actions, each naturally integrating all activities
2. In EACH task, activities MUST happen simultaneously, NOT sequentially
3. Include concrete numbers for all activities in each task
4. Generate title and description in BOTH English and Russian for each task
5. Ensure diversity within the batch
6. Output ONLY valid JSON with "tasks" array containing {count} task objects
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
✓ Read a play aloud with a friend for 45 minutes, each taking on different roles.
✓ Join a book club discussion for 60 minutes, analyzing a chapter you read together during the session.
✗ Read alone for 30 minutes. Later talk to a friend about it (WRONG)"""

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
