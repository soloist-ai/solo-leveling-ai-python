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

# ✅ ДОБАВЛЕНО: Явное разделение топиков по типу
TIME_BASED_TOPICS = {TaskTopic.PHYSICAL_ACTIVITY, TaskTopic.ADVENTURE, TaskTopic.READING}

COMPLEXITY_BASED_TOPICS = {
    TaskTopic.MUSIC, TaskTopic.DEVELOPMENT, TaskTopic.CREATIVITY,
    TaskTopic.SOCIAL_SKILLS, TaskTopic.NUTRITION, TaskTopic.PRODUCTIVITY,
    TaskTopic.BRAIN, TaskTopic.CYBERSPORT, TaskTopic.LANGUAGE_LEARNING
}

REQUIREMENTS_MAP = {
    TaskTopic.PHYSICAL_ACTIVITY: {
        Rarity.COMMON: "5-10 minutes",
        Rarity.UNCOMMON: "20-30 minutes",
        Rarity.RARE: "45-60 minutes",
        Rarity.EPIC: "1-2 hours",
        Rarity.LEGENDARY: "3-5 hours",
    },
    TaskTopic.ADVENTURE: {
        Rarity.COMMON: "10-20 minutes",
        Rarity.UNCOMMON: "30-60 minutes",
        Rarity.RARE: "1-2 hours",
        Rarity.EPIC: "3-4 hours",
        Rarity.LEGENDARY: "5+ hours",
    },
    TaskTopic.MUSIC: {
        Rarity.COMMON: "1-2 legendary tracks",
        Rarity.UNCOMMON: "1 mini-album/EP",
        Rarity.RARE: "1 famous album",
        Rarity.EPIC: "2-3 famous albums",
        Rarity.LEGENDARY: "5 famous albums",
    },
    TaskTopic.READING: {
        Rarity.COMMON: "10-15 minutes",
        Rarity.UNCOMMON: "20-30 minutes",
        Rarity.RARE: "45-60 minutes",
        Rarity.EPIC: "1.5-2 hours",
        Rarity.LEGENDARY: "3-4 hours",
    },
    TaskTopic.DEVELOPMENT: {
        Rarity.COMMON: "1 easy problem",
        Rarity.UNCOMMON: "1 medium problem",
        Rarity.RARE: "2 medium problems",
        Rarity.EPIC: "1 hard problem",
        Rarity.LEGENDARY: "3 hard problems",
    },
    TaskTopic.CREATIVITY: {
        Rarity.COMMON: "100 words / 3 concepts",
        Rarity.UNCOMMON: "500 words / 10 concepts",
        Rarity.RARE: "1000 words / 20 concepts",
        Rarity.EPIC: "2000 words / 50 concepts",
        Rarity.LEGENDARY: "5000 words / 100 concepts",
    },
    TaskTopic.SOCIAL_SKILLS: {
        Rarity.COMMON: "1 brief interaction",
        Rarity.UNCOMMON: "2-3 conversations",
        Rarity.RARE: "Deep/extended engagement",
        Rarity.EPIC: "Public speaking/presentation",
        Rarity.LEGENDARY: "Event organization",
    },
    TaskTopic.NUTRITION: {
        Rarity.COMMON: "1 healthy habit",
        Rarity.UNCOMMON: "2 balanced meals",
        Rarity.RARE: "3-day meal prep",
        Rarity.EPIC: "5-day meal plan",
        Rarity.LEGENDARY: "20+ meal prep sessions",
    },
    TaskTopic.PRODUCTIVITY: {
        Rarity.COMMON: "1 focused task",
        Rarity.UNCOMMON: "3 priority tasks",
        Rarity.RARE: "5 scheduled tasks",
        Rarity.EPIC: "8 deep work sessions",
        Rarity.LEGENDARY: "15 organized tasks",
    },
    TaskTopic.BRAIN: {
        Rarity.COMMON: "1 easy puzzle",
        Rarity.UNCOMMON: "5 medium puzzles",
        Rarity.RARE: "15 hard puzzles",
        Rarity.EPIC: "30 intensive problems",
        Rarity.LEGENDARY: "100 brain challenges",
    },
    TaskTopic.CYBERSPORT: {
        Rarity.COMMON: "5 aim drills",
        Rarity.UNCOMMON: "15 focused drills + 2 matches",
        Rarity.RARE: "30 drills + 3 ranked matches",
        Rarity.EPIC: "50 drills + 5 ranked games",
        Rarity.LEGENDARY: "100 drills + 10 ranked games",
    },
    TaskTopic.LANGUAGE_LEARNING: {
        Rarity.COMMON: "5 new words with pronunciation",
        Rarity.UNCOMMON: "20 words + 5 sentences written",
        Rarity.RARE: "50 words + 3 conversation topics practiced",
        Rarity.EPIC: "100 words + 5 dialogues role-played",
        Rarity.LEGENDARY: "200 words + 10 speaking exercises completed",
    },
}


def _get_topic_type(topics: list[TaskTopic]) -> str:
    """Определяет тип топика: TIME или COMPLEXITY"""
    if any(topic in TIME_BASED_TOPICS for topic in topics):
        return "TIME"
    return "COMPLEXITY"


def _get_metric_instruction(topic_type: str) -> str:
    """Возвращает инструкцию по метрике для типа топика"""
    if topic_type == "TIME":
        return "DURATION (minutes/hours)"
    return "OUTPUT COUNT (items/actions/numbers)"


def create_agent_graph(llm: ChatOpenAI, prompt_service: PromptService):
    validator = TaskValidator()

    def generator_node(state: AgentState) -> Dict[str, Any]:
        """Генерирует задачу на основе topics и rarity"""
        topics = state["topics"]
        rarity = state["rarity"]
        attempt_count = state["attempt_count"]

        # ✅ НОВОЕ: Определяем тип топика
        topic_type = _get_topic_type(topics)
        metric_instruction = _get_metric_instruction(topic_type)

        user_prompt = prompt_service.construct_user_prompt(topics, rarity)

        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=user_prompt),
        ]

        if state.get("critique_feedback"):
            # ✅ УЛУЧШЕНО: Добавлена явная инструкция по типу метрики
            feedback_msg = (
                f"⚠️ PREVIOUS ATTEMPT {attempt_count} WAS REJECTED.\n\n"
                f"**Critic's feedback:**\n{state['critique_feedback']}\n\n"
                f"**TOPIC TYPE: {topic_type}**\n"
                f"Task MUST specify {metric_instruction}\n\n"
                f"{'❌ FORBIDDEN: Mentioning time/duration' if topic_type == 'COMPLEXITY' else '❌ FORBIDDEN: Mentioning action counts'}\n"
                f"{'✅ REQUIRED: Specify exact counts/numbers' if topic_type == 'COMPLEXITY' else '✅ REQUIRED: Specify exact duration'}\n\n"
                f"**Common fixes:**\n"
                f"- Duration/amount wrong → adjust to rarity requirements\n"
                f"- Integration poor → create natural combination\n"
                f"- Not specific → add concrete numbers\n"
                f"- Not creative → entirely different activity\n"
                f"- Attributes too low → INCREASE to match rarity minimum\n\n"
                f"Create a COMPLETELY NEW task addressing the criticism."
            )
            messages.append(HumanMessage(content=feedback_msg))
            logger.info(f"🔄 Regenerating task (attempt {attempt_count + 1}/3)")

        generator_chain = llm.with_structured_output(Task)

        try:
            generated_task_raw = generator_chain.invoke(messages)
            generated_task = cast(Task, generated_task_raw)
        except Exception as e:
            logger.error(f"Generator LLM call failed: {e}", exc_info=True)
            return {
                "current_task": None,
                "attempt_count": state["attempt_count"] + 1,
                "critique_feedback": f"Technical Error: Generator failed. {str(e)[:100]}",
                "validation_failed": True,
            }

        logger.info(
            f"📝 Generated task (attempt {state['attempt_count'] + 1}/3): {generated_task.title.en}"
        )

        try:
            normalized_task = _normalize_attributes(generated_task, rarity, validator)

            # ✅ КРИТИЧЕСКАЯ ПРОВЕРКА
            hard_error = validator.validate_task(normalized_task, rarity)
            if hard_error:
                logger.error(f"❌ Hard validation failed: {hard_error}")
                return {
                    "current_task": normalized_task,
                    "attempt_count": state["attempt_count"] + 1,
                    "critique_feedback": f"Technical Error: {hard_error}",
                    "validation_failed": True,
                }

            # ✅ Валидация прошла - сбрасываем флаг
            return {
                "current_task": normalized_task,
                "attempt_count": state["attempt_count"] + 1,
                "validation_failed": False,
            }

        except Exception as e:
            logger.error(f"Task processing failed: {e}", exc_info=True)
            return {
                "current_task": None,
                "attempt_count": state["attempt_count"] + 1,
                "critique_feedback": f"Technical Error: Processing failed. {str(e)[:100]}",
                "validation_failed": True,
            }

    def critic_node(state: AgentState) -> Dict[str, Any]:
        """LLM critic focusing on SUBJECTIVE quality checks"""

        # ✅ ПЕРВАЯ ПРОВЕРКА: Если валидация уже провалилась - пропускаем LLM
        if state.get("validation_failed", False):
            logger.warning("⚠️ Critic skipped: validation already failed")
            return {
                "critique_feedback": state.get(
                    "critique_feedback", "Validation failed"
                ),
                "validation_failed": False,  # Сбрасываем для следующей попытки
            }

        current_task = state["current_task"]
        if current_task is None:
            logger.error("Current task is None in critic_node")
            return {
                "critique_feedback": "Technical Error: task was not generated",
                "validation_failed": False,
            }

        task: Task = current_task
        rarity = state["rarity"]
        topics = state["topics"]
        topics_str = ", ".join([t.value for t in topics])
        attempt_count = state["attempt_count"]

        # ✅ НОВОЕ: Определяем тип топика для критика
        topic_type = _get_topic_type(topics)
        metric_instruction = _get_metric_instruction(topic_type)

        topic_requirements = []
        for topic in topics:
            if topic in REQUIREMENTS_MAP:
                expected = REQUIREMENTS_MAP[topic].get(rarity, "")
                topic_requirements.append(f"  • {topic.value}: {expected}")

        requirements_text = (
            "\n".join(topic_requirements)
            if topic_requirements
            else "No strict time/amount constraints."
        )

        previous_feedback = state.get("critique_feedback", "")
        history_block = ""
        if previous_feedback and attempt_count > 1:
            history_block = f"""
**⚠️ PREVIOUS REJECTION (Attempt {attempt_count - 1}):**
{previous_feedback}
**IMPORTANT:** Verify the new task addresses this feedback.
"""

        # ✅ УЛУЧШЕНО: Критик теперь знает тип топика
        critic_prompt = f"""You are a Senior Game Designer reviewing task quality.

**Context:** Topics: {topics_str} | Rarity: {rarity.value} | Attempt: {attempt_count}/3
**TOPIC TYPE: {topic_type}** → Task MUST specify {metric_instruction}

{history_block}

**Generated Task:**
- EN: {task.title.en} | {task.description.en}
- RU: {task.title.ru} | {task.description.ru}

✅ **Technical checks passed** (experience, currency, attributes validated)

**Your job - verify SUBJECTIVE quality:**

**1. Metric Compliance ({topic_type}):**
Expected: {metric_instruction}
Requirements for this rarity:
{requirements_text}

{'❌ REJECT if task mentions time/duration (use counts/numbers only)' if topic_type == 'COMPLEXITY' else '❌ REJECT if task mentions action counts (use time/duration only)'}

**2. Topic Integration:** ONE natural action? (not "do X, then Y")

**3. Specificity:** Concrete numbers present?

**4. Realism:** Average person can complete?

**5. Creativity:** Not copying provided examples?

**6. Translation:** Natural? Same essence?

---

**Response:**
✅ All pass: **APPROVED**
❌ Any fail: **REJECTED: [specific reason with emphasis on metric type if violated]**

Be strict but fair. Metric type ({topic_type}) is critical.
"""

        critic_chain = llm.with_structured_output(CritiqueResult)

        try:
            result_raw = critic_chain.invoke(critic_prompt)
            result: CritiqueResult = cast(CritiqueResult, result_raw)
        except Exception as e:
            logger.error(f"Critic LLM call failed: {e}", exc_info=True)
            return {
                "critique_feedback": f"Technical Error: Critic failed. {str(e)[:100]}",
                "validation_failed": False,
            }

        if result.is_approved:
            logger.info(f"✅ Task approved by critic (attempt {attempt_count}/3)")
            return {"critique_feedback": None, "validation_failed": False}
        else:
            logger.warning(
                f"❌ Task rejected by critic (attempt {attempt_count}/3): {result.feedback}"
            )
            return {"critique_feedback": result.feedback, "validation_failed": False}

    def should_continue(state: AgentState) -> str:
        """Решает, продолжать или завершить"""
        if state["critique_feedback"] is None:
            logger.info("✅ Task finalized successfully")
            return END

        if state["attempt_count"] >= 3:
            logger.warning(
                f"⚠️ Max attempts (3/3). Last: {state['critique_feedback'][:100]}"
            )
            logger.warning("Returning last task despite rejection")
            return END

        logger.info(
            f"🔄 Retrying (attempt {state['attempt_count']}/3). "
            f"Reason: {state['critique_feedback'][:80]}..."
        )
        return "generator"

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
    """Нормализует атрибуты если превышают лимит"""
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

    logger.info(f"⚙️ Attributes normalized: {current_sum} -> {max_limit}")
    return task
