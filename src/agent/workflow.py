import logging
from typing import Dict, Any, cast
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, SystemMessage
from src.agent.state import AgentState
from src.avro.enums.rarity import Rarity
from src.avro.enums.task_topic import TaskTopic
from src.models.generate_task_response import Task
from src.agent.critique import CritiqueResult
from src.services.prompt_service import PromptService
from src.services.task_validator import TaskValidator
from src.prompt.system_prompt import SYSTEM_PROMPT

logger = logging.getLogger(__name__)


def create_agent_graph(llm: ChatOpenAI, prompt_service: PromptService):
    validator = TaskValidator()

    def generator_node(state: AgentState) -> Dict[str, Any]:
        """Генерирует задачу на основе topics и rarity"""
        topics = state["topics"]
        rarity = state["rarity"]

        user_prompt = prompt_service.construct_user_prompt(topics, rarity)

        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=user_prompt),
        ]
        if state.get("critique_feedback"):
            feedback_msg = (
                f"PREVIOUS ATTEMPT WAS REJECTED.\n"
                f"Critic's feedback: {state['critique_feedback']}\n\n"
                f"Generate a NEW task that fixes these issues. "
                f"Pay special attention to the rarity requirements and duration/amount constraints."
            )
            messages.append(HumanMessage(content=feedback_msg))

        generator_chain = llm.with_structured_output(Task)
        try:
            generated_task_raw = generator_chain.invoke(messages)
            generated_task = cast(Task, generated_task_raw)

        except Exception as e:
            logger.error(f"Generator LLM call failed: {e}", exc_info=True)

            return {
                "current_task": None,
                "attempt_count": state["attempt_count"] + 1,
                "critique_feedback": (
                    f"Technical Error: Generator model failed. "
                    f"Error: {str(e)[:100]}. Retrying."
                ),
            }

        logger.info(
            f"Generated task (attempt {state['attempt_count'] + 1}): {generated_task.title.en}"
        )
        try:
            normalized_task = _normalize_attributes(generated_task, rarity, validator)
            hard_error = validator.validate_task(normalized_task, rarity)
            if hard_error:
                logger.warning(f"Generated task failed hard validation: {hard_error}")
                return {
                    "current_task": normalized_task,
                    "attempt_count": state["attempt_count"] + 1,
                    "critique_feedback": f"Technical Error: {hard_error}",
                }

            return {
                "current_task": normalized_task,
                "attempt_count": state["attempt_count"] + 1,
            }

        except Exception as e:
            logger.error(f"Task normalization/validation failed: {e}", exc_info=True)
            return {
                "current_task": None,
                "attempt_count": state["attempt_count"] + 1,
                "critique_feedback": (
                    f"Technical Error: Task processing failed. "
                    f"Error: {str(e)[:100]}. Retrying."
                ),
            }

    def critic_node(state: AgentState) -> Dict[str, Any]:
        """
        LLM-based critic that focuses on SUBJECTIVE quality checks only.
        All deterministic validation is already done by TaskValidator.
        """
        current_task = state["current_task"]
        if current_task is None:
            logger.error("Current task is None in critic_node; skipping validation")
            return {"critique_feedback": "Technical Error: task was not generated"}

        task: Task = current_task
        rarity = state["rarity"]
        topics = state["topics"]
        topics_str = ", ".join([t.value for t in topics])
        time_requirements_map = {
            TaskTopic.PHYSICAL_ACTIVITY: {
                Rarity.COMMON: "5-10 minutes",
                Rarity.UNCOMMON: "20-30 minutes",
                Rarity.RARE: "45-60 minutes",
                Rarity.EPIC: "1-2 hours",
                Rarity.LEGENDARY: "3-4 hours",
            },
            TaskTopic.ADVENTURE: {
                Rarity.COMMON: "5-10 minutes",
                Rarity.UNCOMMON: "20-30 minutes",
                Rarity.RARE: "45-60 minutes",
                Rarity.EPIC: "1-2 hours",
                Rarity.LEGENDARY: "3-4 hours",
            },
            TaskTopic.MUSIC: {
                Rarity.COMMON: "1-2 legendary tracks (not full album)",
                Rarity.UNCOMMON: "1 mini-album/EP",
                Rarity.RARE: "1 iconic album (full listen)",
                Rarity.EPIC: "2-3 cult albums by different artists/genres OR complete a discography of 1 key artist (up to 3 albums)",
                Rarity.LEGENDARY: "5 iconic albums of different genres or decades",
            },
        }

        topic_requirements = []
        for topic in topics:
            if topic in time_requirements_map:
                expected = time_requirements_map[topic].get(rarity, "")
                topic_requirements.append(f"  • {topic.value}: {expected}")

        requirements_text = (
            "\n".join(topic_requirements)
            if topic_requirements
            else "No strict time/amount constraints for these topics."
        )

        critic_prompt = f"""You are a Senior Game Designer reviewing task quality.

    **CONTEXT:**
    - Topics: {topics_str}
    - Rarity: {rarity.value}

    **GENERATED TASK:**
    - Title (EN): {task.title.en}
    - Title (RU): {task.title.ru}
    - Description (EN): {task.description.en}
    - Description (RU): {task.description.ru}

    ---

    ✅ **TECHNICAL CHECKS ALREADY PASSED:**
    - Experience, currency, and attributes are validated
    - All fields are non-empty and properly localized

    **YOUR JOB: Focus ONLY on these SUBJECTIVE quality checks:**

    **1. DURATION/AMOUNT REQUIREMENTS:**
    Does the task description match the required scope for {rarity.value}?

    {requirements_text}

    **Analysis:**
    - Read both EN and RU descriptions carefully
    - Identify mentioned duration/amount (e.g., "30 minutes", "1 album", "5km run")
    - Verify it matches the requirements above
    - ⚠️ REJECT if duration/amount is BELOW minimum or ABOVE maximum
    - ✅ APPROVE if within the specified range

    **2. TOPIC INTEGRATION:**
    - Does the task naturally combine ALL topics: {topics_str}?
    - Is it ONE coherent action (not "do X, then do Y")?
    - Does the combination feel organic and realistic?
    - ⚠️ REJECT if topics are separated or integration feels forced

    **3. SPECIFICITY & MEASURABILITY:**
    - Does the task include concrete numbers (quantities, durations, counts)?
    - Is it actionable and measurable?
    - Examples of good specificity: "20 push-ups", "5 pages", "3 conversations", "45 minutes"
    - ⚠️ REJECT if too vague or missing specific measurements

    **4. REALISM & ACHIEVABILITY:**
    - Can an average person realistically complete this task?
    - Is it appropriate for the given rarity level?
    - Are the activities safe and practical?
    - ⚠️ REJECT if unrealistic, dangerous, or requires impossible resources

    **5. CREATIVE QUALITY:**
    - Is the task interesting and varied?
    - Does it avoid being a direct copy of provided examples?
    - Is it appropriate for the rarity difficulty?
    - ⚠️ REJECT if it's too generic or clearly plagiarized from examples

    **6. TRANSLATION QUALITY:**
    - Are both English and Russian descriptions meaningful?
    - Are translations natural (not literal word-for-word)?
    - Do they convey the same task essence?
    - ⚠️ REJECT if translations are awkward or mismatched

    ---

    **VALIDATION PHILOSOPHY:**
    - Apply COMMON SENSE, not pedantic interpretation
    - Understand IMPLICIT meanings and widely-known facts
    - Focus on SUBSTANTIAL issues, not minor wording details
    - Be reasonable but maintain quality standards

    **RESPONSE FORMAT:**
    If ALL subjective checks pass: **APPROVED**

    If ANY issue found: **REJECTED: [specific reason]**

    **Examples of good rejections:**
    - "REJECTED: Task says '30 minutes' but COMMON for PHYSICAL_ACTIVITY requires 5-10 minutes"
    - "REJECTED: Task mentions 'full album' but COMMON for MUSIC requires only 1-2 tracks"
    - "REJECTED: Task describes two separate actions ('do 20 push-ups, then read 5 pages') instead of integrated activity"
    - "REJECTED: Task is too vague - no specific numbers for measurements"
    - "REJECTED: Task requires access to specialized equipment not available to average person"

    Be strict but fair. Your job is to ensure quality, not to nitpick minor details.
    """

        critic_chain = llm.with_structured_output(CritiqueResult)
        try:
            result_raw = critic_chain.invoke(critic_prompt)
            result: CritiqueResult = cast(CritiqueResult, result_raw)

        except Exception as e:
            logger.error(f"Critic LLM call failed: {e}", exc_info=True)

            return {
                "critique_feedback": (
                    f"Technical Error: Critic model failed to respond. "
                    f"Error: {str(e)[:100]}. Retrying generation."
                )
            }

        if result.is_approved:
            logger.info("Task approved by critic")
            return {"critique_feedback": None}
        else:
            logger.warning(f"Task rejected by critic: {result.feedback}")
            return {"critique_feedback": result.feedback}

    def should_continue(state: AgentState) -> str:
        """Решает, продолжать генерацию или завершить"""
        if state["critique_feedback"] is None:
            logger.info("Task finalized successfully")
            return END

        if state["attempt_count"] >= 3:
            logger.error(
                "Max attempts reached (3/3), returning last task despite critique"
            )
            return END

        logger.info(f"Retrying generation (attempt {state['attempt_count'] + 1}/3)")
        return "generator"

    # Сборка графа
    workflow = StateGraph(AgentState)
    workflow.add_node("generator", generator_node)
    workflow.add_node("critic", critic_node)

    workflow.set_entry_point("generator")
    workflow.add_edge("generator", "critic")
    workflow.add_conditional_edges(
        "critic", should_continue, {END: END, "generator": "generator"}
    )

    return workflow.compile()


def _normalize_attributes(task: Task, rarity: Rarity, validator: TaskValidator) -> Task:
    """Нормализует атрибуты если их сумма превышает лимит для rarity"""
    rules = validator.RARITY_RULES.get(rarity)
    if not rules:
        return task

    max_limit = rules["max_attributes"]
    current_sum = task.agility + task.strength + task.intelligence

    if current_sum <= max_limit:
        return task

    ratio = max_limit / current_sum
    new_agility = int(task.agility * ratio)
    new_strength = int(task.strength * ratio)
    new_intelligence = int(task.intelligence * ratio)

    new_sum = new_agility + new_strength + new_intelligence
    remainder = max_limit - new_sum

    if remainder > 0:
        if new_strength >= new_agility and new_strength >= new_intelligence:
            new_strength += remainder
        elif new_agility >= new_strength and new_agility >= new_intelligence:
            new_agility += remainder
        else:
            new_intelligence += remainder

    task.agility = new_agility
    task.strength = new_strength
    task.intelligence = new_intelligence

    logger.info(f"Attributes normalized for {rarity}: {current_sum} -> {max_limit}")
    return task
