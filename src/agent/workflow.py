import logging
from typing import Dict, Any, cast

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

from src.agent.state import AgentState
from src.agent.tools import get_task_requirements
from src.avro.enums.rarity import Rarity
from src.avro.enums.task_topic import TaskTopic
from src.models.generate_task_response import Task
from src.agent.critique import CritiqueResult
from src.prompt.topic_prompts import get_requirements
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

    llm_with_tools = llm.bind_tools([get_task_requirements])

    def generator_node(state: AgentState) -> Dict[str, Any]:
        topics = state["topics"]
        rarity = state["rarity"]
        attempt_count = state["attempt_count"]
        tool_cache = {}
        scenario = prompt_service.get_random_scenario(topics)
        scenario_info = prompt_service.get_scenario_info(scenario)
        scenario_hints = prompt_service.get_scenario_hints_for_topics(scenario, topics)
        user_prompt = f"""
        Generate a self-improvement task for gamification system.

        **Parameters:**
        - topics: {[t.value for t in topics]}
        - rarity: {rarity.value}

        **Scenario: {scenario}**
        - Description: {scenario_info.get('description', 'N/A')}
        - Intensity: {scenario_info.get('intensity', 'flexible')}
        {chr(10).join(scenario_hints) if scenario_hints else ''}

        **Instructions:**
        1. FIRST: Call get_task_requirements tool for EACH topic to understand requirements:
           - Call get_task_requirements(topic="{topics[0].value}", rarity="{rarity.value}")
           {'- Call get_task_requirements(topic="' + topics[1].value + '", rarity="' + rarity.value + '")' if len(topics) > 1 else ''}

        2. THEN: Generate ONE combined task following all requirements
        3. ⚠️ CRITICAL for multiple topics:
           - ALL topics MUST be executed SIMULTANEOUSLY (at the same time)
           - ❌ FORBIDDEN: "do X, then Y" or "afterwards" or "followed by"
           - ✅ REQUIRED: "do X while Y" or "do X during Y"
           
           Example for PHYSICAL_ACTIVITY + MUSIC:
           - ❌ WRONG: "Jog for 30 minutes. Afterwards, listen to album for 45 minutes."
           - ✅ CORRECT: "Jog for 50 minutes while listening to Portishead - Dummy (11 tracks)."
        
        4. Include concrete numbers in description (duration OR counts)
        
        Output valid JSON only.
        """

        messages = [
            SystemMessage(content=SYSTEM_PROMPT, cache_control={"type": "ephemeral"}),
            HumanMessage(content=user_prompt),
        ]

        if state.get("critique_feedback"):
            feedback_msg = f"Issue: {state['critique_feedback']}\nFix this and regenerate."
            messages.append(HumanMessage(content=feedback_msg))
            logger.info(f"🔄 Regenerating task (attempt {attempt_count + 1}/3)")

        try:
            response = llm_with_tools.invoke(messages)

            while response.tool_calls:
                logger.info(f"🔧 LLM called {len(response.tool_calls)} tool(s)")

                # Выполняем tool calls
                for tool_call in response.tool_calls:
                    tool_name = tool_call["name"]
                    tool_args = tool_call["args"]

                    if tool_name == "get_task_requirements":
                        topic = TaskTopic(tool_args["topic"])
                        rarity_arg = Rarity(tool_args["rarity"])
                        cache_key = (topic, rarity_arg)
                        if cache_key not in tool_cache:
                            result = get_requirements(topic, rarity_arg)
                            tool_cache[cache_key] = result
                            logger.info(f"📋 Tool returned requirements for {topic.value}/{rarity_arg.value}")
                        else:
                            result = tool_cache[cache_key]
                            logger.info(f"💾 Tool result from cache for {topic.value}/{rarity_arg.value}")

                        messages.append(response)
                        messages.append(ToolMessage(
                            content=result,
                            tool_call_id=tool_call["id"]
                        ))

                # Следующий вызов LLM с результатами tools
                response = llm_with_tools.invoke(messages)

            # Теперь генерируем финальную задачу
            generator_chain = llm.with_structured_output(Task)
            generated_task = generator_chain.invoke(messages)

        except Exception as e:
            logger.error(f"Generator LLM call failed: {e}", exc_info=True)
            return {
                "current_task": None,
                "attempt_count": state["attempt_count"] + 1,
                "critique_feedback": f"Technical Error: Generator failed. {str(e)[:100]}",
                "validation_failed": True,
            }

        # Остальная логика processing без изменений...
        logger.info(f"📝 Generated task (attempt {state['attempt_count'] + 1}/3): {generated_task.title.en}")

        try:
            processed_task = processor.apply_numeric_logic(generated_task, rarity, topics)
            hard_error = validator.validate_task(processed_task, rarity)

            if hard_error:
                logger.error(f"❌ Hard validation failed: {hard_error}")
                return {
                    "current_task": processed_task,
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
                "critique_feedback": f"Technical Error: Processing failed. {str(e)[:100]}",
                "validation_failed": True,
            }

    def critic_node(state: AgentState) -> Dict[str, Any]:
        """LLM critic focusing on SUBJECTIVE quality checks."""

        # Если жёсткая валидация уже провалилась — критика не вызываем
        if state.get("validation_failed", False):
            logger.warning("⚠️ Critic skipped: validation already failed")
            return {
                "critique_feedback": state.get("critique_feedback", "Validation failed"),
                "validation_failed": False,  # сбрасываем флаг для следующей попытки
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
        if rarity in {Rarity.COMMON, Rarity.UNCOMMON}:
            logger.info("ℹ️ Critic skipped for low rarity task")
            return {"critique_feedback": None, "validation_failed": False}

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
        """Решает, продолжать или завершить."""
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
    workflow.add_conditional_edges("critic", should_continue, {END: END, "generator": "generator"})

    return workflow.compile()

