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
        generated_task_raw = generator_chain.invoke(messages)
        generated_task = cast(Task, generated_task_raw)

        logger.info(
            f"Generated task (attempt {state['attempt_count'] + 1}): {generated_task.title.en}"
        )

        normalized_task = _normalize_attributes(generated_task, rarity, validator)

        return {
            "current_task": normalized_task,
            "attempt_count": state["attempt_count"] + 1,
        }

    def critic_node(state: AgentState) -> Dict[str, Any]:
        """Критик проверяет задачу на соответствие всем требованиям"""
        current_task = state["current_task"]

        if current_task is None:
            logger.error("Current task is None in critic_node; skipping validation")
            return {"critique_feedback": "Technical Error: task was not generated"}

        task: Task = current_task
        rarity = state["rarity"]
        topics = state["topics"]
        topics_str = ", ".join([t.value for t in topics])

        hard_error = validator.validate_task(task, rarity)
        if hard_error:
            logger.warning(f"Hard validation failed: {hard_error}")
            return {"critique_feedback": f"Technical Error: {hard_error}"}


        time_requirements_map = {
            TaskTopic.PHYSICAL_ACTIVITY: {
                Rarity.COMMON: "5-10 minutes",
                Rarity.UNCOMMON: "20-30 minutes",
                Rarity.RARE: "45-60 minutes",
                Rarity.EPIC: "1-2 hours",
                Rarity.LEGENDARY: "3-4 hours"
            },
            TaskTopic.ADVENTURE: {
                Rarity.COMMON: "10-20 minutes",
                Rarity.UNCOMMON: "30-60 minutes",
                Rarity.RARE: "1-2 hours",
                Rarity.EPIC: "3-4 hours",
                Rarity.LEGENDARY: "5+ hours"
            },
            TaskTopic.MUSIC: {
                Rarity.COMMON: "1-2 legendary tracks (not full album)",
                Rarity.UNCOMMON: "1 mini-album/EP",
                Rarity.RARE: "1 iconic album (full listen)",
                Rarity.EPIC: "2-3 cult albums by different artists/genres OR complete a discography of 1 key artist (up to 3 albums)",
                Rarity.LEGENDARY: "5 iconic albums of different genres or decades"
            }
        }

        topic_requirements = []
        for topic in topics:
            if topic in time_requirements_map:
                expected = time_requirements_map[topic].get(rarity, "")
                topic_requirements.append(f"- {topic.value} at {rarity.value} level MUST be: {expected}")

        requirements_text = "\n".join(
            topic_requirements) if topic_requirements else "No strict time/amount constraints for these topics."

        attribute_limits = {
            Rarity.COMMON: 2,
            Rarity.UNCOMMON: 4,
            Rarity.RARE: 6,
            Rarity.EPIC: 8,
            Rarity.LEGENDARY: 10
        }

        experience_ranges = {
            Rarity.COMMON: (10, 20),
            Rarity.UNCOMMON: (30, 40),
            Rarity.RARE: (50, 60),
            Rarity.EPIC: (70, 80),
            Rarity.LEGENDARY: (90, 100)
        }

        max_attrs = attribute_limits.get(rarity, 10)
        exp_min, exp_max = experience_ranges.get(rarity, (10, 100))
        actual_attr_sum = task.agility + task.strength + task.intelligence


        critic_prompt = f"""You are a strict Senior Game Designer. Your job is to verify that the generated task EXACTLY matches all requirements.
**YOUR VALIDATION PHILOSOPHY:**
    - Apply COMMON SENSE, not pedantic literal interpretation
    - Understand IMPLICIT meanings and widely-known facts
    - Focus on SUBSTANTIAL issues, not minor wording details

**WHAT WAS REQUESTED:**
- Topics: [{topics_str}]
- Rarity: {rarity.value}

**WHAT WAS GENERATED:**
- Title (EN): {task.title.en}
- Title (RU): {task.title.ru}
- Description (EN): {task.description.en}
- Description (RU): {task.description.ru}
- Experience: {task.experience}
- Currency Reward: {task.currencyReward}
- Attributes: Agility={task.agility}, Strength={task.strength}, Intelligence={task.intelligence} (sum={actual_attr_sum})

---

**YOUR TASK: Compare what was generated against these STRICT REQUIREMENTS:**

1. **EXPERIENCE VALIDATION:**
   - MUST be between {exp_min} and {exp_max} for {rarity.value}
   - MUST be a multiple of 10
   - Current value: {task.experience}
   - ✅ Valid? Check yourself.

2. **CURRENCY REWARD:**
   - MUST equal exactly experience ÷ 2
   - Expected: {task.experience // 2}, Actual: {task.currencyReward}
   - ✅ Valid? Check yourself.

3. **ATTRIBUTES:**
   - Sum (agility + strength + intelligence) MUST NOT exceed {max_attrs} for {rarity.value}
   - Current sum: {actual_attr_sum}
   - ✅ Valid? Check yourself.

4. **DURATION/AMOUNT REQUIREMENTS (CRITICAL!):**
{requirements_text}

   **Your analysis:**
   - Read the task description carefully (both EN and RU)
   - Identify what duration/amount is mentioned (e.g., "30 minutes", "30 минут", "1 album", "full album", "5km run")
   - Compare it against the requirements above
   - If task says "30 minutes" but {rarity.value} requires "5-10 minutes" → REJECT
   - If task says "full album" but {rarity.value} requires "1-2 tracks" → REJECT
   - If task says "1 hour jog" but {rarity.value} requires "5-10 minutes" → REJECT
   
   **DO NOT REJECT** if the task provides a value within the specified range.
    Only REJECT if the value is BELOW the minimum or ABOVE the maximum.

5. **COMPLEXITY/OUTPUT REQUIREMENTS FOR NON-TIME-BASED TOPICS:**
    
    For topics like NUTRITION, PRODUCTIVITY, CREATIVITY, SOCIAL_SKILLS, BRAIN, DEVELOPMENT, READING:
    - These scale by OUTPUT/COMPLEXITY, not just time
    - Check the RARITY SCALING section in topic prompts for required amounts

6. **TOPIC INTEGRATION:**
   - Task must naturally combine ALL topics: [{topics_str}]
   - Should be ONE coherent action, not "do X, then do Y"
   - The combination should feel organic and realistic
   - ✅ Does it integrate topics well? Check yourself.

7. **SPECIFICITY:**
   - Task must include concrete numbers (how many, how long, how much)
   - Should be actionable and measurable
   - Examples: "20 push-ups", "5 pages", "3 conversations", "10 minutes"
   - ✅ Is it specific enough? Check yourself.

8. **LOCALIZATION:**
   - Both title.en and title.ru must be non-empty
   - Both description.en and description.ru must be non-empty
   - Translations should be meaningful (not just literal word-for-word)
   - ✅ Is localization complete? Check yourself.

---

**RESPONSE FORMAT:**

If ALL checks pass: APPROVED
If ANY violation found: REJECTED: <specific reason>

**Examples of correct rejections:**
- "REJECTED: Task says '30 minutes' but COMMON for PHYSICAL_ACTIVITY requires 5-10 minutes"
- "REJECTED: Attributes sum to 8 but COMMON maximum is 2"
- "REJECTED: Experience is 25 but must be between 10-20 for COMMON"
- "REJECTED: Task mentions 'full album' but COMMON for MUSIC requires only 1-2 tracks"
- "REJECTED: Currency reward is 15 but should be 10 (experience 20 ÷ 2)"
- "REJECTED: Task describes two separate actions ('do push-ups, then read') instead of integrated activity"

**Be EXTREMELY strict. Your job is to catch ANY mismatch between requirements and generated content.**
**BE REASONABLE. Focus on substance, not pedantry.**

"""

        critic_chain = llm.with_structured_output(CritiqueResult)
        result_raw = critic_chain.invoke(critic_prompt)
        result: CritiqueResult = cast(CritiqueResult, result_raw)

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
            logger.error("Max attempts reached (3/3), returning last task despite critique")
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
        "critic",
        should_continue,
        {END: END, "generator": "generator"}
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


