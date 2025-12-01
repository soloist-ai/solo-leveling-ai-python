from src.avro.enums.task_topic import TaskTopic

TOPIC_PROMPT_MAP: dict[TaskTopic, str] = {

    # ========== PHYSICAL_ACTIVITY (С ВРЕМЕННЫМИ РАМКАМИ) ==========
    TaskTopic.PHYSICAL_ACTIVITY: """
**Focus:** Sports, bodyweight exercises, cardio, flexibility, outdoor activities.
**Equipment:** Minimal (bodyweight, resistance bands, jump rope, public spaces).
**Avoid:** Dangerous activities, gym-only workouts, equipment-heavy exercises.

**TIME-BASED RARITY SCALING (duration is mandatory):**
- COMMON: 5-10 minutes (quick warm-up, stretching, short walk)
- UNCOMMON: 20-30 minutes (moderate workout, jog, yoga session)
- RARE: 45-60 minutes (intensive workout, long run, full circuit training)
- EPIC: 1-2 hours (endurance training, sports practice, extensive session)
- LEGENDARY: 3-4 hours (marathon training, ultra-endurance, multi-sport session)

**GOOD EXAMPLES:**
✅ "Do 3 sets of 15 push-ups and 20 squats" (UNCOMMON)
✅ "Run 5 kilometers at moderate pace" (RARE)
✅ "Complete a full-body circuit: 50 push-ups, 100 squats, 30 burpees, 10 pull-ups" (EPIC)
✅ "Practice basketball drills for 45 minutes (dribbling, shooting, defense)" (RARE)
✅ "Go for a 2-hour hike in nature with 300m elevation gain" (EPIC)

**BAD EXAMPLES:**
❌ "Exercise" (too vague)
❌ "Lift 200kg deadlift" (equipment-heavy, dangerous)
❌ "Train hard" (no specifics)

**ATTRIBUTES:**
- Agility: 2-6 (cardio, flexibility, coordination, sports)
- Strength: 1-5 (resistance work, endurance)
- Intelligence: 0 (physical tasks don't improve cognition)

**TYPICAL MISTAKES:**
- Assigning Intelligence to pure physical tasks
- Not specifying duration (MUST include time)
- Suggesting dangerous or equipment-heavy activities

Always generate tasks that are unexpected, varied, and not similar to the provided examples in text or numbers.
""",

    # ========== CREATIVITY (СЛОЖНОСТЬ, НЕ ВРЕМЯ) ==========
    TaskTopic.CREATIVITY: """
**Focus:** Generate something new, interesting, unusual. Creative projects, art, writing, design, crafts, brainstorming.
**Outputs:** Drawings, stories, poems, designs, DIY projects, innovative ideas, prototypes.
**Avoid:** Passive consumption (watching art), low-effort tasks, plagiarism.

**COMPLEXITY-BASED RARITY SCALING (not time-bound):**
- COMMON: Small creative output (sketch 1 object, write 100 words, 3 creative ideas)
- UNCOMMON: Medium creative work (short story 500 words, detailed drawing, 10 unique ideas)
- RARE: Substantial creation (1000-word story, complete painting, design mockup, 20 ideas)
- EPIC: Large project (2000+ word story, multiple artworks, full design system, 50 ideas)
- LEGENDARY: Major creative achievement (5000+ words, art series, comprehensive creative portfolio)

**GOOD EXAMPLES:**
✅ "Sketch 5 objects from your room in different artistic styles" (UNCOMMON)
✅ "Write a 1200-word short story with an unexpected plot twist" (RARE)
✅ "Design a logo and brand identity for an imaginary startup" (EPIC)
✅ "Create a handmade origami sculpture with 30+ folds" (RARE)
✅ "Invent 15 creative solutions to a common daily problem" (UNCOMMON)

**BAD EXAMPLES:**
❌ "Be creative" (not actionable)
❌ "Look at Pinterest" (passive)
❌ "Think of something" (no output)

**ATTRIBUTES:**
- Agility: 1-3 (for physical crafts/art)
- Strength: 0-1 (minimal effort)
- Intelligence: 4-8 (creativity, problem-solving, design thinking, originality)

**TYPICAL MISTAKES:**
- Not specifying output quantity/word count
- Passive activities instead of creation
- Suggesting "copy this style" instead of original work

Always generate tasks that are unexpected, varied, and not similar to the provided examples in text or numbers.
""",

    # ========== SOCIAL_SKILLS (СЛОЖНОСТЬ, НЕ ВРЕМЯ) ==========
    TaskTopic.SOCIAL_SKILLS: """
**Focus:** Communication, conversations, networking, active listening, public speaking, building relationships.
**Settings:** Face-to-face interactions (café, phone calls, workplace, public spaces, events).
**Avoid:** Online texting, social media engagement, passive observation.

**COMPLEXITY-BASED RARITY SCALING:**
- COMMON: Simple interaction (compliment 1 person, ask 2 questions, short phone call)
- UNCOMMON: Meaningful conversation (start dialogue with stranger, 15-min discussion on topic)
- RARE: Deep engagement (have 30-min debate, practice active listening with 3 people, networking)
- EPIC: Public speaking/leadership (give presentation, lead group discussion, facilitate meeting)
- LEGENDARY: Major social challenge (organize event, speak to large audience, network with 20+ people)

**GOOD EXAMPLES:**
✅ "Approach a stranger and have a 5-minute conversation about their interests" (UNCOMMON)
✅ "Call 3 friends and ask them for honest feedback about your communication style" (RARE)
✅ "Give an impromptu 10-minute speech on a random topic to a small group" (EPIC)
✅ "Compliment 5 different people sincerely throughout the day" (COMMON)
✅ "Practice active listening: have a conversation without interrupting for 20 minutes" (RARE)

**BAD EXAMPLES:**
❌ "Talk to someone" (too vague)
❌ "Send DMs on Instagram" (not face-to-face)
❌ "Be more social" (not measurable)

**ATTRIBUTES:**
- Agility: 0-1 (minimal physical)
- Strength: 0 (no effort)
- Intelligence: 3-8 (communication, empathy, persuasion, emotional intelligence)

**TYPICAL MISTAKES:**
- Suggesting online communication instead of in-person
- Not specifying interaction count
- Vague tasks like "be friendly"

Always generate tasks that are unexpected, varied, and not similar to the provided examples in text or numbers.
""",

    # ========== NUTRITION (СЛОЖНОСТЬ, НЕ ВРЕМЯ) ==========
    TaskTopic.NUTRITION: """
**Focus:** Healthy eating habits, meal preparation, nutrition planning, hydration, mindful eating.
**Activities:** Cooking, meal prep, nutrition tracking, grocery planning, hydration discipline.
**Avoid:** Medical/diet advice, extreme restrictions, supplement recommendations, fasting.

**COMPLEXITY-BASED RARITY SCALING:**
- COMMON: Simple habit (drink 500ml water, eat 1 fruit, track 1 meal)
- UNCOMMON: Meal preparation (cook balanced meal, prep 2 snacks, plan tomorrow's meals)
- RARE: Structured nutrition (meal prep 3 days, create weekly plan, track all macros for day)
- EPIC: Extensive planning (meal prep for 5 days, detailed nutrition strategy, 15 recipes researched)
- LEGENDARY: Comprehensive nutrition system (20+ meals prepped, monthly plan, nutrition guide created)

**GOOD EXAMPLES:**
✅ "Drink 2 liters of water throughout the day and track it" (COMMON)
✅ "Prepare 3 balanced meals with protein, carbs, and vegetables" (RARE)
✅ "Research and create a weekly meal plan with calorie/macro breakdown" (EPIC)
✅ "Cook 10 healthy meals and freeze them for future use" (EPIC)
✅ "Track your nutrition for 3 days and identify 5 improvements" (RARE)

**BAD EXAMPLES:**
❌ "Eat healthy" (not specific)
❌ "Start keto diet" (medical advice)
❌ "Skip a meal" (potentially harmful)

**ATTRIBUTES:**
- Agility: 0-1 (minimal movement)
- Strength: 0-1 (light cooking)
- Intelligence: 2-6 (nutrition knowledge, planning, macro calculations)

**TYPICAL MISTAKES:**
- Recommending diets or supplements
- Not specifying quantities/portions
- Vague goals like "eat better"

Always generate tasks that are unexpected, varied, and not similar to the provided examples in text or numbers.
""",

    # ========== PRODUCTIVITY (СЛОЖНОСТЬ, НЕ ВРЕМЯ) ==========
    TaskTopic.PRODUCTIVITY: """
**Focus:** Deep work, task completion, time management, organization, focus techniques, planning.
**Methods:** Pomodoro, to-do lists, calendars, prioritization, workspace organization, batch processing.
**Avoid:** Passive activities, procrastination, "productivity theater" (looking busy without output).

**COMPLEXITY-BASED RARITY SCALING:**
- COMMON: Simple task (complete 1 to-do item, organize 5 files, plan next 3 tasks)
- UNCOMMON: Focused session (complete 3 tasks, Pomodoro deep work, organize full workspace)
- RARE: Major productivity push (complete project milestone, clear entire backlog, 5 tasks done)
- EPIC: Project completion (finish major deliverable, deep work on critical task, 8+ tasks)
- LEGENDARY: Massive output (complete entire project phase, 15+ tasks, quarterly planning session)

**GOOD EXAMPLES:**
✅ "Complete 3 high-priority tasks from your to-do list without distractions" (UNCOMMON)
✅ "Work on your most important project for 90 minutes using Pomodoro (no phone)" (RARE)
✅ "Organize your digital workspace: sort 100 files, clean desktop, archive old projects" (RARE)
✅ "Plan your entire week: schedule tasks, block time for deep work, set priorities" (UNCOMMON)
✅ "Complete a full project milestone: finish 8 tasks, review, and document results" (EPIC)

**BAD EXAMPLES:**
❌ "Be productive" (not measurable)
❌ "Check email" (reactive, not productive)
❌ "Think about work" (passive)

**ATTRIBUTES:**
- Agility: 0 (no physical)
- Strength: 0 (no effort)
- Intelligence: 4-9 (planning, focus, execution, prioritization, systems thinking)

**TYPICAL MISTAKES:**
- Passive activities disguised as work
- Not specifying task count or output
- Confusing "busy" with "productive"

Always generate tasks that are unexpected, varied, and not similar to the provided examples in text or numbers.
""",

    # ========== ADVENTURE (С ВРЕМЕННЫМИ РАМКАМИ) ==========
    TaskTopic.ADVENTURE: """
**Focus:** Exploration, visiting new places, micro-trips, local tourism, discovering experiences, outdoor activities.
**Activities:** Walking new routes, visiting landmarks/museums, urban exploration, day trips, photography walks.
**Avoid:** Expensive trips, dangerous activities, unrealistic travel (flights required).

**TIME-BASED RARITY SCALING:**
- COMMON: 10-20 minutes (explore new street, visit 1 local spot, short discovery walk)
- UNCOMMON: 30-60 minutes (visit museum/park, explore new neighborhood, urban photo walk)
- RARE: 1-2 hours (hike trail, visit 3 landmarks, explore entire district)
- EPIC: 3-4 hours (day trip to nearby town, extensive city exploration, adventure challenge)
- LEGENDARY: 5+ hours (full-day adventure: multiple locations, long hike, exploration marathon)

**GOOD EXAMPLES:**
✅ "Walk a route you've never taken and discover 3 interesting places" (UNCOMMON)
✅ "Visit a local museum and spend 1 hour exploring exhibits you've never seen" (RARE)
✅ "Take a day trip to a nearby town: visit 5 landmarks and try local food" (EPIC)
✅ "Hike a 8km trail and photograph 10 unique natural features" (EPIC)
✅ "Urban exploration: visit 10 places in your city you've never been to" (LEGENDARY)

**BAD EXAMPLES:**
❌ "Go somewhere" (too vague)
❌ "Fly to another country" (unrealistic)
❌ "Have an adventure" (not specific)

**ATTRIBUTES:**
- Agility: 2-5 (walking, hiking, climbing stairs)
- Strength: 1-4 (endurance, carrying gear)
- Intelligence: 1-4 (navigation, cultural learning, planning)

**TYPICAL MISTAKES:**
- Suggesting expensive/unrealistic travel
- Not specifying locations or distance
- Dangerous activities without preparation

Always generate tasks that are unexpected, varied, and not similar to the provided examples in text or numbers.
""",

    TaskTopic.MUSIC: """
    **Focus:** Discover and listen to cult, classic, landmark or genre-defining albums, tracks, or composers for musical and cultural expansion.
    **Goal:** Each task suggests a concrete album, artist, or set of tracks recognized as an iconic work in music history.
    **Landmark music categories (use as inspiration, always pick NEW works):**
    - Classic rock (60s-90s legends)
    - Hip-hop/rap (golden age and modern classics)
    - Jazz (bebop, cool jazz, fusion)
    - Electronic/techno/house (pioneers and innovators)
    - Alternative/indie (genre-defining albums)
    - Classical music (symphonies, concertos, chamber music)
    - World music (African, Latin, Asian traditions)
    - Soul/funk/R&B (Motown era to modern)
    - Russian/Soviet rock and pop (legends from USSR and post-Soviet era)

    
    **RARITY SCALING (amount/result, not time!):**
    - COMMON: 1-2 legendary tracks.
    - UNCOMMON: 1 mini-album/EP.
    - RARE: 1 iconic album (full listen).
    - EPIC: 2-3 cult albums by different artists/genres OR complete a discography of 1 key artist (up to 3 albums).
    - LEGENDARY: 5 iconic albums of different genres or decades.

    **GOOD EXAMPLES:**
    ✅ "Listen to the full album Deftones 'White Pony' and focus on the transitions between tracks."
    ✅ "Discover Wu-Tang Clan 'Enter the 36 Chambers' and Pink Floyd 'The Dark Side of the Moon'; reflect on how they changed their genres."
    ✅ "Listen to Radiohead 'OK Computer', Kendrick Lamar 'To Pimp a Butterfly', and Björk 'Homogenic', and note 3 things about each that made them famous."
    ✅ "Pick 10 essential jazz tracks from different artists and create a mini-list with notes for each."

    **BAD EXAMPLES:**
    ❌ "Listen to music" (not specific)
    ❌ "Play popular songs" (no focus on culture/history)
    ❌ "Play a Spotify playlist in the background" (not active listening, not landmark works)
    ❌ "Ask a friend for recommendations" (task must suggest album/track, not rely on others)

    **ATTRIBUTES:**
    - Agility: 0 (no movement)
    - Strength: 0 (no effort)
    - Intelligence: 5-8 (musical culture, analysis, attentive listening)

    **TYPICAL MISTAKES:**
    - Making the user choose the music instead of suggesting
    - Proposing random/unknown works (must be cult, classic, genre-defining)
    - Counting passive listening or mainstream pop as a result

    Always generate tasks that are unexpected, varied, and not similar to the provided examples in text or numbers.
    Do not repeat any album or artist mentioned in the prompt or examples. Always try to recommend new landmark albums and tracks from a wide range of genres, eras, and cultures.
    Diversify recommendations: use world music, jazz, rock, hip-hop, experimental music, classical, and iconic works from non-English-speaking countries.
    ach time generate new, unexpected, but canonical (historically significant or critically acclaimed) works. You can invent reasonable, realistic recommendations. Focus on unique albums and songs known for their innovation or cultural impact.
    """,

    # ========== BRAIN (СЛОЖНОСТЬ, НЕ ВРЕМЯ) ==========
    TaskTopic.BRAIN: """
**Focus:** Mental exercises, logic puzzles, memory training, riddles, crosswords, brain teasers, attention training.
**Activities:** Sudoku, chess, math problems, memory games, pattern recognition, critical thinking challenges.
**Avoid:** Passive activities (watching quiz shows), guessing without strategy.

**COMPLEXITY-BASED RARITY SCALING:**
- COMMON: Simple puzzles (1 easy Sudoku, 5 mental math problems, 3 riddles)
- UNCOMMON: Medium challenge (1 medium Sudoku, 10 math problems, 5 logic puzzles, 1 chess puzzle)
- RARE: Hard problems (1 hard Sudoku, 15 brain teasers, full chess game, 20 calculations)
- EPIC: Intensive training (3 hard puzzles, 5 chess games, 30 logic problems, memory techniques)
- LEGENDARY: Mental marathon (solve 10 hard puzzles, chess tournament, 100+ problems, master technique)

**GOOD EXAMPLES:**
✅ "Solve 1 medium-difficulty Sudoku puzzle completely" (UNCOMMON)
✅ "Solve 15 mental arithmetic problems (3-digit multiplication without calculator)" (RARE)
✅ "Play 3 chess games and analyze your mistakes afterwards" (EPIC)
✅ "Memorize a sequence of 20 random numbers and recall them in order" (RARE)
✅ "Solve 10 lateral thinking riddles (e.g., 'A man walks into a bar...')" (UNCOMMON)

**BAD EXAMPLES:**
❌ "Think hard" (not measurable)
❌ "Watch Jeopardy" (passive)
❌ "Do a puzzle" (no difficulty/quantity)

**ATTRIBUTES:**
- Agility: 0 (no physical)
- Strength: 0 (no effort)
- Intelligence: 5-10 (logic, memory, pattern recognition, strategy, problem-solving)

**TYPICAL MISTAKES:**
- Not specifying puzzle difficulty or count
- Passive observation instead of solving
- Vague tasks like "train your brain"

Always generate tasks that are unexpected, varied, and not similar to the provided examples in text or numbers.
""",

    # ========== CYBERSPORT (СЛОЖНОСТЬ, НЕ ВРЕМЯ) ==========
    TaskTopic.CYBERSPORT: """
**Focus:** Improve competitive gaming skills: aim, strategy, game sense, teamwork, replay analysis, mechanics.
**Games:** FPS (CS:GO, Valorant), MOBA (Dota, LoL), strategy, aim trainers, competitive titles.
**Avoid:** Casual play, playing for fun without improvement focus, toxic behavior, tilting.

**COMPLEXITY-BASED RARITY SCALING:**
- COMMON: Basic drill (5-min aim training, learn 2 callouts, watch 1 pro play clip)
- UNCOMMON: Focused practice (15-min aim routine, play 1 ranked match with focus, analyze 1 replay)
- RARE: Intensive training (30-min aim drill, play 3 ranked with strategy focus, VOD review)
- EPIC: Serious grind (play 5 ranked matches, complete advanced aim routine, analyze 3 replays)
- LEGENDARY: Pro-level session (10+ matches, master new character/agent, coach teammates, tournament prep)

**GOOD EXAMPLES:**
✅ "Complete 15 minutes of aim training (Kovaak's or Aim Lab) focusing on tracking" (UNCOMMON)
✅ "Play 2 ranked matches focusing ONLY on communication and teamwork" (RARE)
✅ "Watch your last 3 matches and write down 5 mistakes you made + solutions" (EPIC)
✅ "Practice one specific mechanic (e.g., spray control) for 20 minutes in practice range" (UNCOMMON)
✅ "Learn 10 new map callouts and use them in 2 ranked games" (RARE)

**BAD EXAMPLES:**
❌ "Play games" (casual, no focus)
❌ "Win a match" (outcome-based)
❌ "Rage at teammates" (toxic)

**ATTRIBUTES:**
- Agility: 3-7 (reaction time, hand-eye coordination, speed, precision)
- Strength: 0-1 (minimal)
- Intelligence: 3-6 (strategy, game sense, decision-making, analysis)

**TYPICAL MISTAKES:**
- Counting casual play as training
- Focusing on wins instead of improvement
- Not specifying drill type or match count

Always generate tasks that are unexpected, varied, and not similar to the provided examples in text or numbers.
""",

    # ========== DEVELOPMENT (СЛОЖНОСТЬ, НЕ ВРЕМЯ) ==========
    TaskTopic.DEVELOPMENT: """
**Focus:** Coding, software engineering, algorithms, system design, debugging, testing, clean code, refactoring.
**Activities:** LeetCode, refactoring, documentation, unit tests, code review, architecture, mini-projects.
**Avoid:** Passive learning (just watching tutorials), "tutorial hell", no hands-on practice.

**COMPLEXITY-BASED RARITY SCALING:**
- COMMON: Small task (solve 1 easy problem, write 1 test, refactor 10 lines, read 1 doc page)
- UNCOMMON: Medium work (solve 1 medium problem, write tests for 1 function, review 100 lines)
- RARE: Substantial coding (solve 2 medium problems, implement pattern, write full test suite)
- EPIC: Large project work (solve 1 hard problem, refactor module, design system architecture)
- LEGENDARY: Major achievement (build mini-project, solve 3 hard problems, complete coding challenge)

**GOOD EXAMPLES:**
✅ "Solve 1 medium LeetCode problem on binary trees and explain solution" (UNCOMMON)
✅ "Refactor 50 lines of code following SOLID principles" (RARE)
✅ "Design a URL shortener system (system design with diagrams)" (EPIC)
✅ "Write unit tests for 3 functions with edge cases and mocking" (RARE)
✅ "Solve 2 hard algorithm problems: dynamic programming + graph traversal" (EPIC)

**BAD EXAMPLES:**
❌ "Code something" (too vague)
❌ "Watch tutorial" (passive)
❌ "Fix bugs" (no quantity)

**ATTRIBUTES:**
- Agility: 0 (no physical)
- Strength: 0 (no effort)
- Intelligence: 5-10 (algorithms, logic, problem-solving, architecture, systems thinking)

**TYPICAL MISTAKES:**
- Watching tutorials instead of coding
- Not specifying problem difficulty
- Unrealistic scope (COMMON can't be "build full app")

Always generate tasks that are unexpected, varied, and not similar to the provided examples in text or numbers.
""",

    # ========== READING (СЛОЖНОСТЬ, НЕ ВРЕМЯ) ==========
    TaskTopic.READING: """
**Focus:** Books, articles, essays, technical documentation, research papers, educational content.
**Genres:** Fiction, non-fiction, technical docs, news analysis, academic papers, philosophy.
**Avoid:** Social media scrolling, clickbait articles, skimming without comprehension.

**COMPLEXITY-BASED RARITY SCALING:**
- COMMON: Short reading (5-10 pages, 1 article, 1 blog post)
- UNCOMMON: Medium reading (20-30 pages, 3 articles, 1 long-form essay, chapter summary)
- RARE: Substantial reading (50 pages, full chapter + notes, 1 research paper analyzed)
- EPIC: Extensive reading (100 pages, 3 chapters annotated, 2 technical papers summarized)
- LEGENDARY: Reading marathon (finish book 200+ pages, read 5 papers, comprehensive notes)

**GOOD EXAMPLES:**
✅ "Read 20 pages of a non-fiction book and summarize 5 key ideas" (UNCOMMON)
✅ "Read 1 technical article (3000+ words) and write a 300-word summary" (RARE)
✅ "Read 2 chapters of a philosophy book and write counterarguments" (EPIC)
✅ "Read a research paper and explain methodology in your own words" (RARE)
✅ "Read 50 pages of fiction and analyze character development" (RARE)

**BAD EXAMPLES:**
❌ "Read something" (no quantity)
❌ "Scroll through news" (passive)
❌ "Look at book" (not reading)

**ATTRIBUTES:**
- Agility: 0 (no movement)
- Strength: 0 (no effort)
- Intelligence: 3-8 (comprehension, retention, critical thinking, analysis)

**TYPICAL MISTAKES:**
- Not specifying page count
- Social media as "reading"
- Skimming instead of deep reading

Always generate tasks that are unexpected, varied, and not similar to the provided examples in text or numbers.
""",

    # ========== LANGUAGE_LEARNING (СЛОЖНОСТЬ, НЕ ВРЕМЯ) ==========
    TaskTopic.LANGUAGE_LEARNING: """
**Focus:** Vocabulary, grammar, pronunciation, conversation practice, writing, listening comprehension, cultural immersion.
**Methods:** Flashcards, apps, speaking practice, writing exercises, watching content, reading native materials.
**Avoid:** Passive listening, translation apps without learning, unmeasured "study time".

**COMPLEXITY-BASED RARITY SCALING:**
- COMMON: Small practice (learn 5 words, practice pronunciation 5 min, write 3 sentences)
- UNCOMMON: Focused session (learn 20 words, complete 1 lesson, 10-min speaking, write paragraph)
- RARE: Substantial work (50 words, 3 lessons, write 10 sentences with new grammar, 20-min conversation)
- EPIC: Intensive practice (100 words, full module, 30-min conversation, write 300-word essay)
- LEGENDARY: Immersion challenge (200+ words, 10 lessons, 60-min conversation, write 1000 words, watch movie)

**GOOD EXAMPLES:**
✅ "Learn 20 new vocabulary words and use each in a sentence" (UNCOMMON)
✅ "Watch a 15-minute video in Spanish with subtitles and summarize in 5 sentences" (RARE)
✅ "Have a 30-minute conversation in target language (use language exchange app)" (EPIC)
✅ "Write a 300-word essay in your target language about your daily routine" (EPIC)
✅ "Complete 3 grammar lessons and do all exercises without looking at answers" (RARE)

**BAD EXAMPLES:**
❌ "Study language" (no specifics)
❌ "Use Google Translate" (not learning)
❌ "Listen to music" (passive)

**ATTRIBUTES:**
- Agility: 0 (no physical)
- Strength: 0 (no effort)
- Intelligence: 4-9 (memory, pattern recognition, linguistic skills, cultural understanding)

**TYPICAL MISTAKES:**
- Passive listening without practice
- Not specifying word count or lesson units
- Using translation tools as crutch

Always generate tasks that are unexpected, varied, and not similar to the provided examples in text or numbers.
""",
}

# Default fallback
DEFAULT_TOPIC_PROMPT = """
Generate a self-improvement task suitable for daily routine.
Be specific, measurable, and realistic. Include exact numbers for quantities.
Always generate tasks that are unexpected, varied, and not similar to common examples.
"""
