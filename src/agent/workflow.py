import logging
from typing import Dict, Any, cast

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, SystemMessage

from src.agent.state import AgentState
from src.avro.enums.task_topic import TaskTopic
from src.exceptions.exceptions import TaskGenerationError
from src.models.generate_task_response import Task
from src.agent.critique import CritiqueResult
from src.services.prompt_service import PromptService
from src.services.task_processor import TaskProcessor
from src.services.task_validator import TaskValidator
from src.prompt.system_prompt import SYSTEM_PROMPT

logger = logging.getLogger(__name__)

TIME_BASED_TOPICS = {
    TaskTopic.PHYSICAL_ACTIVITY,
    TaskTopic.ADVENTURE,
    TaskTopic.READING,
}

COMPLEXITY_BASED_TOPICS = {
    TaskTopic.MUSIC,
    TaskTopic.DEVELOPMENT,
    TaskTopic.CREATIVITY,
    TaskTopic.SOCIAL_SKILLS,
    TaskTopic.NUTRITION,
    TaskTopic.PRODUCTIVITY,
    TaskTopic.BRAIN,
    TaskTopic.CYBERSPORT,
    TaskTopic.LANGUAGE_LEARNING,
}


def create_agent_graph(llm: ChatOpenAI, prompt_service: PromptService):
    validator = TaskValidator()
    processor = TaskProcessor(validator)

    def generator_node(state: AgentState) -> Dict[str, Any]:
        topics = state["topics"]
        rarity = state["rarity"]
        attempt_count = state["attempt_count"]

        user_prompt = prompt_service.build_user_prompt(topics, rarity)

        messages = [
            SystemMessage(content=SYSTEM_PROMPT, cache_control={"type": "ephemeral"}),
            HumanMessage(content=user_prompt),
        ]

        if state.get("critique_feedback"):
            feedback = state["critique_feedback"]
            messages.append(
                HumanMessage(
                    content=f"❌ Previous attempt rejected: {feedback}\n\nFix this issue and regenerate."
                )
            )
            logger.info(f"🔄 Regenerating task (attempt {attempt_count + 1}/3)")

        try:
            generator_chain = llm.with_structured_output(Task)
            generated_task_raw = generator_chain.invoke(messages)

            if not isinstance(generated_task_raw, Task):
                raise ValueError(f"Expected Task, got {type(generated_task_raw)}")

            generated_task: Task = generated_task_raw

        except Exception as e:
            logger.error(f"Generator LLM call failed: {e}", exc_info=True)
            return {
                "current_task": None,
                "attempt_count": state["attempt_count"] + 1,
                "critique_feedback": f"Technical Error: {str(e)[:100]}",
                "validation_failed": True,
            }

        logger.info(
            f"📝 Generated task (attempt {attempt_count + 1}/3): {generated_task.title.en}"
        )

        try:
            processed_task = processor.apply_numeric_logic(
                generated_task, rarity, topics
            )

            hard_error = validator.validate_task(processed_task, rarity)

            if hard_error:
                logger.error(f"❌ Hard validation failed: {hard_error}")
                return {
                    "current_task": None,
                    "attempt_count": state["attempt_count"] + 1,
                    "critique_feedback": f"Technical Error: {hard_error}",
                    "validation_failed": True,
                }

            return {
                "current_task": processed_task,
                "attempt_count": state["attempt_count"] + 1,
                "validation_failed": False,
            }

        except Exception as e:
            logger.error(f"Task processing failed: {e}", exc_info=True)
            return {
                "current_task": None,
                "attempt_count": state["attempt_count"] + 1,
                "critique_feedback": f"Technical Error: {str(e)[:100]}",
                "validation_failed": True,
            }

    def critic_node(state: AgentState) -> Dict[str, Any]:
        """
        LLM critic для субъективных проверок качества.

        Критические проверки:
        1. Интеграция топиков (simultaneous vs sequential)
        2. Конкретность (наличие чисел)
        3. Качество локализации (EN vs RU)

        При одобрении - сохраняет задачу в diversity tracker.

        Returns:
            Updated state с critique_feedback (None если approved)
        """
        # Если жёсткая валидация провалилась - пропускаем критика
        if state.get("validation_failed", False):
            logger.warning("⚠️ Critic skipped: validation already failed")
            return {
                "critique_feedback": state.get(
                    "critique_feedback", "Validation failed"
                ),
                "validation_failed": False,
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

        critic_prompt = f"""
You are a Senior Game Designer reviewing a self-improvement task.

**Context:**
- topics: {topics_str}
- rarity: {rarity.value}
- attempt: {attempt_count}/3

**Task:**
- EN: {task.title.en} | {task.description.en}
- RU: {task.title.ru} | {task.description.ru}

**Code has ALREADY validated:**
- All numeric constraints (experience, currency, attributes)
- JSON schema correctness
- Metric type requirements

**Your subjective review (CRITICAL CHECKS):**

1. **Topic integration (MOST IMPORTANT)**:
   ❌ REJECT if description has two separate phases:
      - Words like "afterwards", "then", "later", "followed by" indicate separate phases
      - "Do X for N minutes. Then do Y for M minutes" is WRONG
      - "Do X. Afterwards, do Y" is WRONG

   ✅ APPROVE only if topics happen SIMULTANEOUSLY:
      - "Do X while Y"
      - "Do X during Y"
      - "Combine X and Y"

   Example for PHYSICAL + MUSIC:
   - ❌ BAD: "Jog 30 min. Afterwards, listen to album 45 min"
   - ✅ GOOD: "Jog 50 min while listening to album (11 tracks)"

2. **Specificity**: Does description include concrete numbers?

3. **Localization quality**: Do EN and RU describe the same action naturally?

4. **Diversity check**: Does the task feel fresh and different from typical patterns?

Return JSON:
- is_approved: true/false
- feedback: brief reason if rejected (max 2 sentences, mention specific issue)
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
        """
        Routing logic для workflow.

        Решения:
        - critique_feedback = None -> END (успех)
        - attempt_count >= 3 -> END (макс попытки, возвращаем последнее)
        - иначе -> "generator" (retry)

        Returns:
            "generator" для retry или END для финализации
        """
        if state["critique_feedback"] is None:
            logger.info("✅ Task finalized successfully")
            return END

        if state["attempt_count"] >= 3:
            if state.get("current_task") is None:
                logger.error("❌ Failed to generate valid task after 3 attempts")
                raise TaskGenerationError(
                    f"All attempts failed: {state['critique_feedback']}"
                )
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
