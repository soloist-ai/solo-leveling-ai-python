from src.avro.enums.task_topic import TaskTopic

TOPIC_PROMPT_MAP: dict[TaskTopic, str] = {
    TaskTopic.PHYSICAL_ACTIVITY: """
⏱️ TIME-BASED: 5-10 min (COMMON) → 3-5 hours (LEGENDARY)
Focus: Bodyweight exercises, cardio, sports
Attributes: Agility (dominant 50-70%), Strength (30-40%), Intelligence 0-1
Max sum: 2 (COMMON) → 20 (LEGENDARY)
🎲 Vary activities: calisthenics, running, yoga, martial arts, swimming, cycling, HIIT
""",

    TaskTopic.MUSIC: """
📊 COMPLEXITY-BASED: 1-2 tracks (COMMON) → 5 albums (LEGENDARY)
Focus: Landmark albums across ALL genres
Attributes: Intelligence only (100%)
Max sum: 2 (COMMON) → 20 (LEGENDARY)
❌ NEVER mention listening time/duration
✅ Specify exact album/track count
🎲 Vary genres WIDELY: jazz (1960s-70s), krautrock, afrobeat, trip-hop, post-rock, IDM, noise, ambient, experimental hip-hop, avant-garde classical, shoegaze, dub techno
⚠️ FORBIDDEN albums (overused): Kind of Blue, Abbey Road, Dark Side of the Moon, OK Computer, Blonde on Blonde
Examples of variety:
- "Fela Kuti - Zombie (9 tracks)"
- "Can - Tago Mago (5 tracks)"
- "Burial - Untrue (13 tracks)"
- "Fishmans - Long Season (1 track, 35 min epic)"
""",

    TaskTopic.DEVELOPMENT: """
📊 COMPLEXITY-BASED: 1 easy (COMMON) → 3 hard problems (LEGENDARY)
Focus: Algorithms, refactoring, testing
Attributes: Intelligence only (100%)
Max sum: 2 (COMMON) → 20 (LEGENDARY)
🎲 Vary types: array manipulation, graphs, dynamic programming, greedy algorithms, backtracking, bit manipulation, trees, linked lists, strings, sorting
""",

    TaskTopic.CREATIVITY: """
📊 COMPLEXITY-BASED: 100 words (COMMON) → 5000 words (LEGENDARY)
Focus: Original content creation
Attributes: Intelligence (dominant 70-80%), Agility (20-30%)
Max sum: 2 (COMMON) → 20 (LEGENDARY)
🎲 Vary formats: short story, essay, design mockup, character sketch, world-building, dialogue scene, poetry, concept art description, brainstorm list
""",

    TaskTopic.SOCIAL_SKILLS: """
📊 COMPLEXITY-BASED: 1 interaction (COMMON) → Event organization (LEGENDARY)
Focus: Real-world face-to-face only
Attributes: Intelligence (dominant 60-80%), Agility (20-40%)
Max sum: 2 (COMMON) → 20 (LEGENDARY)
❌ No digital/online activities
🎲 Vary contexts: networking event, casual conversation, active listening practice, compliment giving, storytelling, group discussion, conflict resolution
""",

    TaskTopic.NUTRITION: """
📊 COMPLEXITY-BASED: 1 habit (COMMON) → 20 meal preps (LEGENDARY)
Focus: Cooking, meal planning
Attributes: Intelligence (dominant 60-80%), Strength (10-20%), Agility (10-20%)
Max sum: 2 (COMMON) → 20 (LEGENDARY)
🎲 Vary cuisines: Mediterranean, Asian, Mexican, Middle Eastern, Indian, fusion
🎲 Vary goals: high-protein, balanced macros, vegetarian, meal prep, hydration tracking
""",

    TaskTopic.PRODUCTIVITY: """
📊 COMPLEXITY-BASED: 1 task (COMMON) → 15 tasks (LEGENDARY)
Focus: Deep work, task batching
Attributes: Intelligence only (100%)
Max sum: 2 (COMMON) → 20 (LEGENDARY)
🎲 Vary methods: Pomodoro, time-blocking, Eisenhower matrix, task batching, GTD, eat-the-frog
""",

    TaskTopic.ADVENTURE: """
⏱️ TIME-BASED: 10-20 min (COMMON) → 5+ hours (LEGENDARY)
Focus: Local exploration, micro-tourism
Attributes: Agility (40-50%), Strength (20-30%), Intelligence (20-30%)
Max sum: 2 (COMMON) → 20 (LEGENDARY)
🎲 Vary locations: hidden alleys, rooftop views, historical markers, street art, local markets, parks, waterfronts, cultural districts
""",

    TaskTopic.BRAIN: """
📊 COMPLEXITY-BASED: 1 puzzle (COMMON) → 100 challenges (LEGENDARY)
Focus: Logic, pattern recognition
Attributes: Intelligence only (100%)
Max sum: 2 (COMMON) → 20 (LEGENDARY)
🎲 Vary types: Sudoku, chess puzzles, logic grids, riddles, math problems, memory games, spatial reasoning
""",

    TaskTopic.CYBERSPORT: """
📊 COMPLEXITY-BASED: 5 drills (COMMON) → 100 drills + 10 games (LEGENDARY)
Focus: Mechanical skill, aim training
Attributes: Agility (dominant 60-70%), Intelligence (30-40%)
Max sum: 2 (COMMON) → 20 (LEGENDARY)
❌ NEVER mention practice duration
✅ Specify drill count + match count
🎲 Vary drills: flick shots, tracking, spray control, crosshair placement, movement mechanics, utility lineups
""",

    TaskTopic.READING: """
⏱️ TIME-BASED: 10-15 min (COMMON) → 3-4 hours (LEGENDARY)
Focus: Books, long-form articles
Attributes: Intelligence only (100%)
Max sum: 2 (COMMON) → 20 (LEGENDARY)
✅ Use time/duration, not page count
🎲 Vary materials: non-fiction, literary fiction, technical docs, research papers, essays, biographies
""",

    TaskTopic.LANGUAGE_LEARNING: """
📊 COMPLEXITY-BASED: 5 words (COMMON) → 200 words (LEGENDARY)
Focus: Active learning, conversation
Attributes: Intelligence (dominant 70-80%), Agility (20-30%)
Max sum: 2 (COMMON) → 20 (LEGENDARY)
🎲 Vary activities: flashcards, sentence writing, conversation practice, grammar drills, listening comprehension, shadowing
""",
}

DEFAULT_TOPIC_PROMPT = "Generate specific, measurable task."
