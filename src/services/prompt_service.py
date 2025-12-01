import random
from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.rarity import Rarity
from src.prompt.topic_prompts import TOPIC_PROMPT_MAP, DEFAULT_TOPIC_PROMPT
from src.prompt.topic_scenarios import TOPIC_SCENARIOS_MAP, ALL_SCENARIOS


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
        if not topics:
            return random.choice(ALL_SCENARIOS)

        if len(topics) == 1:
            scenarios = self._scenario_map.get(topics[0], ALL_SCENARIOS)
            return random.choice(scenarios)

        # Пересечение сценариев для множества топиков
        common_scenarios = set(self._scenario_map.get(topics[0], ALL_SCENARIOS))
        for topic in topics[1:]:
            topic_scenarios = set(self._scenario_map.get(topic, ALL_SCENARIOS))
            common_scenarios &= topic_scenarios

        scenarios_to_choose = list(common_scenarios) if common_scenarios else ALL_SCENARIOS
        return random.choice(scenarios_to_choose)

    def _merge_topic_contexts(self, topics: list[TaskTopic]) -> str:
        """
        Объединяет промпты нескольких топиков в единую связную инструкцию.
        """
        if len(topics) == 1:
            return self._get_topic_instruction(topics[0])

        # Получаем полные промпты для каждого топика
        topic_prompts = {topic: self._get_topic_instruction(topic) for topic in topics}

        # Формируем объединённую инструкцию
        merged_context = f"""**COMBINED TASK GENERATION ({len(topics)} topics)**

    You must generate a SINGLE task that naturally integrates ALL of these topics:
    {', '.join([t.value for t in topics])}

    """

        # Добавляем краткую выжимку из каждого топика
        for i, (topic, prompt) in enumerate(topic_prompts.items(), 1):
            focus = self._extract_section(prompt, "**Focus:**")
            rarity_info = self._extract_section(prompt, "**RARITY SCALING")
            attributes = self._extract_section(prompt, "**ATTRIBUTES:**")
            good_examples = self._extract_section(prompt, "**GOOD EXAMPLES:**")

            merged_context += f"""
    **Topic {i}: {topic.value}**
    {focus if focus else ""}

    {rarity_info if rarity_info else ""}

    {attributes if attributes else ""}

    {good_examples if good_examples else ""}
    """

        # Добавляем правила для комбинированных задач
        merged_context += f"""

    **CRITICAL RULES FOR COMBINED TASKS:**

    1. **Integration, not separation:**
       - DO NOT create separate sub-tasks (e.g., "do 20 push-ups AND read 5 pages")
       - Instead, create ONE action that naturally requires both topics
       - Example (GOOD): "Listen to a podcast about nutrition while doing a 30-minute walk"
       - Example (BAD): "Do 10 squats. Then read an article." (two separate actions)

    2. **Natural combination:**
       - The task should feel organic, not forced
       - Topics should complement each other in a realistic scenario
       - Example: PHYSICAL_ACTIVITY + SOCIAL_SKILLS → "Play basketball with 3 friends for 45 minutes"
       - Example: READING + LANGUAGE_LEARNING → "Read 10 pages of a book in your target language"

    3. **Attributes distribution:**
       - Distribute attributes based on BOTH topics' contributions
       - If combining PHYSICAL + BRAIN: assign both Agility/Strength AND Intelligence
       - Total attribute sum must still respect rarity limits

    4. **Complexity scaling:**
       - For topics with TIME constraints (PHYSICAL_ACTIVITY, ADVENTURE, MUSIC): respect time ranges
       - For topics with COMPLEXITY constraints (DEVELOPMENT, READING): scale difficulty, not time
       - Combined tasks should match the complexity/duration of BOTH topics at the given rarity

    5. **Scenario compatibility:**
       - The selected scenario applies to the ENTIRE combined task
       - Ensure the combination makes sense in the given scenario context

    6. **Examples of good combinations:**
       - PHYSICAL_ACTIVITY + MUSIC: "Go for a 5km run while listening to an iconic funk album by James Brown"
       - SOCIAL_SKILLS + ADVENTURE: "Explore a new neighborhood and start conversations with 3 locals"
       - DEVELOPMENT + BRAIN: "Solve 2 LeetCode problems requiring complex algorithm logic"
       - PRODUCTIVITY + READING: "Complete 3 work tasks and read one industry article to learn new approach"
       - NUTRITION + CREATIVITY: "Invent and cook 2 new healthy recipes from scratch"

    **CRITICAL: DO NOT REPEAT ANY SPECIFIC EXAMPLES FROM THE PROMPTS ABOVE.**
    - If MUSIC topic: DO NOT suggest albums explicitly mentioned (Radiohead, Wu-Tang, etc.). Choose OTHER landmark albums.
    - If DEVELOPMENT topic: DO NOT repeat exact problem descriptions from examples.
    - If READING topic: DO NOT mention the same books/articles from examples.
    - ALWAYS generate fresh, unique, varied content that is different from all provided examples.

    Always generate unique, creative combined tasks that feel natural and achievable.
    """

        return merged_context

    def _extract_section(self, text: str, section_marker: str) -> str:
        """Извлекает секцию из промпта топика (от маркера до следующего **...**)"""
        if section_marker not in text:
            return ""

        start_idx = text.find(section_marker)
        # Ищем следующую секцию или конец текста
        next_section_idx = text.find("\n**", start_idx + len(section_marker))

        if next_section_idx == -1:
            # Если это последняя секция
            section_text = text[start_idx:].strip()
        else:
            section_text = text[start_idx:next_section_idx].strip()

        # Ограничиваем длину (первые 3 строки)
        lines = section_text.split('\n')
        return '\n'.join(lines[:8]) if len(lines) > 8 else section_text

    def construct_user_prompt(self, topics: list[TaskTopic], rarity: Rarity) -> str:
        """
        Динамически собирает USER PROMPT
        """
        # 1. Выбираем случайный сценарий
        scenario = self._get_random_scenario(topics)

        # 2. Объединяем контексты топиков
        topic_context = self._merge_topic_contexts(topics)
        rarity_reminders = {
            Rarity.COMMON: """
        **THIS IS A COMMON (LOWEST LEVEL) TASK!**
        - Keep it MINIMAL: smallest amounts, shortest durations, simplest actions
        - Think: "baby steps", "quick taste", "light intro"
        - For time-based topics: use MINIMUM from the range (e.g., 5 min, not 10)
        - For complexity topics: use SMALLEST amounts (e.g., 1 item, 3 ideas, 5 pages)
        - Should feel EFFORTLESS and accessible to complete beginners
        - Avoid words: "intensive", "complete", "full", "extensive", "thorough"
        - Use words: "quick", "light", "brief", "simple", "easy", "short"
        """,

            Rarity.UNCOMMON: """
        **THIS IS AN UNCOMMON TASK - MODERATE LEVEL**
        - Moderate amounts and reasonable effort
        - Think: "solid practice session", "meaningful progress"
        - For time-based topics: use MIDDLE of the range (e.g., 20-30 min)
        - For complexity topics: use MEDIUM amounts (e.g., 3-5 items, 10-15 ideas, 20-30 pages)
        - Should feel achievable but require focus
        - Balance between accessibility and challenge
        """,

            Rarity.RARE: """
        **THIS IS A RARE TASK - SUBSTANTIAL LEVEL**
        - Significant amounts and focused dedication required
        - Think: "deep work session", "major milestone"
        - For time-based topics: use UPPER range (e.g., 45-60 min)
        - For complexity topics: use LARGE amounts (e.g., 5-10 items, 20+ ideas, 50+ pages)
        - Should feel like a real achievement when completed
        - Requires commitment and sustained effort
        """,

            Rarity.EPIC: """
        **THIS IS AN EPIC TASK - LARGE-SCALE CHALLENGE**
        - Extensive amounts and high commitment required
        - Think: "intensive project", "advanced achievement"
        - For time-based topics: use EXTENDED durations (e.g., 1-2 hours)
        - For complexity topics: use VERY LARGE amounts (e.g., 10-20 items, multiple outputs, 100+ pages)
        - Should feel impressive and challenging
        - Requires expert-level focus and dedication
        """,

            Rarity.LEGENDARY: """
        **THIS IS A LEGENDARY TASK - MAXIMUM LEVEL EPIC UNDERTAKING**
        - MASSIVE amounts and extraordinary dedication required
        - Think: "marathon effort", "master achievement", "extreme challenge"
        - For time-based topics: use MAXIMUM durations (e.g., 3-4+ hours)
        - For complexity topics: use EXCEPTIONAL amounts (e.g., 20+ items, comprehensive outputs, 200+ pages)
        - Should feel like an extraordinary accomplishment
        - Requires ultimate commitment and stamina
        """
        }

        rarity_reminder = rarity_reminders.get(rarity, "")

        # 3. Собираем финальный USER PROMPT
        user_prompt = f"""You are generating a task for a gamification system.

        {rarity_reminder}

        **Required Parameters:**
        - Topics: {[t.value for t in topics]}
        - Rarity: {rarity.value}
        - Context/Scenario: {scenario}

        {topic_context}
        

    **Task Requirements:**
    - The task MUST fit the scenario "{scenario}" — adapt the task to match the time, place, and energy level
    - Include specific numbers (quantities, durations, counts) where applicable
    - Make the task realistic and achievable in the given scenario
    - Output ONLY valid JSON matching the schema

    **MANDATORY UNIQUENESS RULE:**
    Never copy or closely paraphrase any specific examples from the instructions above (album names, book titles, exercise descriptions, etc.). 
    Always generate fresh, creative, and varied content that is inspired by but NOT identical to the examples.
    If suggesting music albums, choose landmarks NOT mentioned in the prompt. If suggesting exercises, use different numbers and formats.

    Generate a unique, creative task that perfectly integrates all topics into the scenario context.
    """
        return user_prompt
