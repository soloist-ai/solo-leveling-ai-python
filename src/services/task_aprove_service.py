import logging
from typing import cast, Optional, List

from langchain_core.messages import HumanMessage, SystemMessage

from src.avro.enums.localization_item import LocalizationItem
from src.avro.enums.task_topic import TaskTopic
from src.config.ai_config import create_validation_text_llm, create_validation_vision_llm
from src.models.aprove_task_response import TaskValidationResponse
from src.models.task_validation_internal import (
    TaskRequirements,
    VisualFacts,
    TaskValidationDecision,
)
from src.prompt.aprove_prompt import (
    REQUIREMENTS_SYSTEM_PROMPT_TEMPLATE,
    FACTS_SYSTEM_PROMPT,
    MATCH_SYSTEM_PROMPT,
)

logger = logging.getLogger(__name__)

# Минимальный порог уверенности для подтверждения задачи
# Если модель говорит VALID, но confidence < 0.6, мы считаем это ошибкой/галлюцинацией
MIN_CONFIDENCE_THRESHOLD = 0.6

# Правила валидации для каждого топика
TOPIC_VALIDATION_RULES = {
    # HARD PROOF (Result-based)
    TaskTopic.NUTRITION: "HARD: Requires photo of the PREPARED DISH/MEAL.",
    TaskTopic.DEVELOPMENT: "HARD: Requires screenshot of CODE/IDE or Problem Solved screen.",
    TaskTopic.CREATIVITY: "HARD: Requires photo of the CREATED WORK (sketch, text, design).",
    TaskTopic.PRODUCTIVITY: "HARD: Requires photo of the PLAN/LIST/Schedule/Workspace.",
    TaskTopic.ADVENTURE: "HARD: Requires photo of the LOCATION/VIEW/Street.",

    # SOFT PROOF (Process-based)
    TaskTopic.PHYSICAL_ACTIVITY: "SOFT: Requires CONTEXT (Gym, Sweat, Gear). Do NOT require video/witness.",
    TaskTopic.READING: "SOFT: Requires CONTEXT (Book, Kindle). Do NOT require timer proof.",
    TaskTopic.MUSIC: "SOFT: Requires CONTEXT (Headphones, App UI, Album Art). Do NOT require duration proof.",
    TaskTopic.BRAIN: "SOFT: Requires CONTEXT (Puzzle, Chess board, App).",
    TaskTopic.CYBERSPORT: "SOFT: Requires CONTEXT (Game UI, Lobby, Scoreboard).",
    TaskTopic.SOCIAL_SKILLS: "SOFT: Requires CONTEXT (Selfie, Event, Group). Partial/blurred photo accepted for privacy.",
    TaskTopic.LANGUAGE_LEARNING: "SOFT: Requires CONTEXT (Notes, Flashcards, App).",
}

DEFAULT_RULE = "SOFT: Requires visual context consistent with the task description."


class TaskValidationService:
    """Сервис для валидации выполнения задач по фото с помощью Vision LLM"""

    def __init__(self):
        self.text_llm = create_validation_text_llm()
        self.vision_llm = create_validation_vision_llm()
        logger.info("TaskValidationService initialized")

    def validate_task_completion(
        self,
        task_title: LocalizationItem,
        task_description: LocalizationItem,
        image_base64: str,
        *,
        topic: Optional[TaskTopic] = None,
        topic_hints: Optional[List[str]] = None,
        rarity: Optional[str] = None,
    ) -> TaskValidationResponse:
        """
        Проверяет выполнение задачи по фотографии (3 этапа: requirements -> facts -> match)
        """
        logger.info(f"Validating task: {task_title.en}")

        image_url = f"data:image/jpeg;base64,{image_base64}"

        # 1. Извлекаем требования из текста
        requirements = self._extract_requirements(
            task_title=task_title,
            task_description=task_description,
            topic_hints=topic_hints,
            topic=topic,
            rarity=rarity,
        )

        # 2. Извлекаем факты из фото
        facts = self._extract_visual_facts(image_url=image_url)

        # 3. Сопоставляем (решает LLM)
        decision = self._match_requirements_to_facts(
            requirements=requirements,
            facts=facts,
            task_title=task_title,
            task_description=task_description,
        )

        # 4. GUARDRAIL: Пост-валидация на уровне кода
        final_is_valid = decision.is_valid
        final_feedback = decision.feedback

        # Если LLM подтвердила, но уверенность низкая — реджектим
        if decision.is_valid and decision.confidence < MIN_CONFIDENCE_THRESHOLD:
            logger.warning(
                f"LLM approved task but confidence {decision.confidence:.2f} "
                f"is below threshold {MIN_CONFIDENCE_THRESHOLD}. Overriding to INVALID."
            )
            final_is_valid = False
            # Заменяем фидбек на более осторожный, так как доказательства слабые
            final_feedback = LocalizationItem(
                en="The evidence provided is ambiguous or unclear. Please provide a clearer photo strictly following the requirements.",
                ru="Предоставленные доказательства неоднозначны или нечетки. Пожалуйста, сделайте более понятное фото, строго следуя требованиям.",
            )

        result = TaskValidationResponse(
            is_valid=final_is_valid,
            confidence=decision.confidence,
            feedback=final_feedback,
        )

        logger.info(
            "Validation result: valid=%s (original=%s), confidence=%.2f",
            result.is_valid,
            decision.is_valid,
            result.confidence,
        )
        return result

    def _extract_requirements(
            self,
            *,
            task_title: LocalizationItem,
            task_description: LocalizationItem,
            topic: Optional[TaskTopic],
            topic_hints: Optional[List[str]],
            rarity: Optional[str],
    ) -> TaskRequirements:
        validation_rule = TOPIC_VALIDATION_RULES.get(topic, DEFAULT_RULE) if topic else DEFAULT_RULE
        system_prompt_content = REQUIREMENTS_SYSTEM_PROMPT_TEMPLATE.format(
            validation_rule=validation_rule
        )

        user_text = self._build_requirements_prompt(
            task_title=task_title,
            task_description=task_description,
            topic_hints=topic_hints,
            rarity=rarity,
        )

        messages = [
            SystemMessage(content=system_prompt_content, cache_control={"type": "ephemeral"}),
            HumanMessage(content=user_text),
        ]

        structured = self.text_llm.with_structured_output(TaskRequirements)
        return cast(TaskRequirements, structured.invoke(messages))

    def _extract_visual_facts(self, *, image_url: str) -> VisualFacts:
        messages = [
            SystemMessage(content=FACTS_SYSTEM_PROMPT, cache_control={"type": "ephemeral"}),
            HumanMessage(
                content=[
                    {"type": "text", "text": "Extract observable facts from the image."},
                    {"type": "image_url", "image_url": {"url": image_url, "detail": "high"}},
                ]
            ),
        ]

        structured = self.vision_llm.with_structured_output(VisualFacts)
        return cast(VisualFacts, structured.invoke(messages))

    def _match_requirements_to_facts(
        self,
        *,
        requirements: TaskRequirements,
        facts: VisualFacts,
        task_title: LocalizationItem,
        task_description: LocalizationItem,
    ) -> TaskValidationDecision:
        user_text = self._build_match_prompt(
            task_title=task_title,
            task_description=task_description,
            requirements=requirements,
            facts=facts,
        )

        messages = [
            SystemMessage(content=MATCH_SYSTEM_PROMPT, cache_control={"type": "ephemeral"}),
            HumanMessage(content=user_text),
        ]

        structured = self.vision_llm.with_structured_output(TaskValidationDecision)
        return cast(TaskValidationDecision, structured.invoke(messages))

    def _build_requirements_prompt(
        self,
        *,
        task_title: LocalizationItem,
        task_description: LocalizationItem,
        topic_hints: Optional[List[str]],
        rarity: Optional[str],
    ) -> str:
        hints_block = ""
        if topic_hints:
            hints_joined = "\n".join(f"- {h}" for h in topic_hints[:8])
            hints_block = f"\nTopic hints (may help interpret evidence types):\n{hints_joined}\n"

        rarity_block = f"\nRarity: {rarity}\n" if rarity else ""

        return f"""Task title:
EN: {task_title.en}
RU: {task_title.ru}

Task description:
EN: {task_description.en}
RU: {task_description.ru}
{rarity_block}{hints_block}
Convert the task into an explicit checklist of requirements.
"""

    def _build_match_prompt(
        self,
        *,
        task_title: LocalizationItem,
        task_description: LocalizationItem,
        requirements: TaskRequirements,
        facts: VisualFacts,
    ) -> str:
        return f"""Task title:
EN: {task_title.en}
RU: {task_title.ru}

Task description:
EN: {task_description.en}
RU: {task_description.ru}

Requirements JSON:
{requirements.model_dump_json()}

Visual facts JSON:
{facts.model_dump_json()}

Match requirements to facts, then return decision JSON.
"""
