from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.rarity import Rarity

# ============================================================================
# СТРУКТУРА: {(topic, rarity): "детальные требования"}
# ============================================================================

TOPIC_RARITY_REQUIREMENTS: dict[tuple[TaskTopic, Rarity], str] = {

    # ========================================================================
    # PHYSICAL_ACTIVITY (TIME-BASED)
    # ========================================================================

    (TaskTopic.PHYSICAL_ACTIVITY, Rarity.COMMON): """
**Metric Type:** TIME-BASED
**Duration:** 5-10 minutes
**Exercises:** 1-2 basic movements ONLY
**Intensity:** Light, beginner-friendly, anyone can do
**Pattern:** Single exercise OR simple pair

**ALLOWED exercises ONLY:**
- Push-ups (standard, wide, close grip)
- Squats (bodyweight, jump squats)
- Planks (standard, side)
- Lunges (forward, reverse)
- Burpees
- Running/Jogging
- Jumping jacks
- Sit-ups/Crunches

**FORBIDDEN:** 
- NO animal movements (bear crawls, crab walks, frog jumps, spider-man)
- NO yoga, sports, dancing, martial arts
- NO creative or fancy movements
- NO "flow" exercises

**Examples:**
- "Do 30 push-ups for 8 minutes"
- "Perform squats for 10 minutes"
- "Plank hold and rest cycles for 7 minutes"

**Integration:**
- With MUSIC: "Do push-ups for 8 min while listening to [2 tracks]"
- With ADVENTURE: Not typical for COMMON
""",

    (TaskTopic.PHYSICAL_ACTIVITY, Rarity.UNCOMMON): """
**Metric Type:** TIME-BASED
**Duration:** 20-30 minutes
**Exercises:** 2-3 basic movements combined
**Intensity:** Moderate, some variation in reps/sets
**Pattern:** Simple circuit or alternating exercises

**ALLOWED exercises ONLY:**
- Push-ups (standard, wide, close, decline, incline)
- Squats (bodyweight, jump, single-leg)
- Planks (standard, side)
- Lunges (forward, reverse, walking)
- Burpees
- Pull-ups/Chin-ups (if bar available)
- Dips (if bars available)
- Running/Jogging
- Jumping jacks
- Sit-ups/Crunches

**FORBIDDEN:**
- NO animal movements
- NO yoga, sports, dancing, martial arts
- NO creative exercises

**Examples:**
- "Circuit: push-ups, squats, planks for 25 minutes"
- "Alternate lunges and burpees for 28 minutes"
- "Run and do bodyweight exercises for 22 minutes"

**Integration:**
- With MUSIC: "Do circuit workout for 25 min while listening to [EP or 5-6 tracks]"
- With SOCIAL: "Workout for 30 min while friend counts reps"
""",

    (TaskTopic.PHYSICAL_ACTIVITY, Rarity.RARE): """
**Metric Type:** TIME-BASED
**Duration:** 45-60 minutes
**Exercises:** 3-4 basic movements, structured workout
**Intensity:** Challenging but sustainable, multiple sets/rounds
**Pattern:** Full workout session with variety

**ALLOWED exercises ONLY:**
- Push-ups (all variations)
- Squats (all variations)
- Planks (all variations)
- Lunges (all variations)
- Burpees
- Pull-ups/Chin-ups
- Dips
- Running/Jogging
- Jumping jacks
- Sit-ups/Crunches

**FORBIDDEN:**
- NO animal movements whatsoever
- NO yoga, sports, dancing, martial arts
- NO creative or fancy exercises

**Examples:**
- "Complete workout: push-ups, squats, lunges, planks for 50 minutes"
- "Circuit training: 5 exercises rotated for 55 minutes"
- "Run 20 min + bodyweight circuit 30 min"

**Integration:**
- With MUSIC: "Do 50-min workout while listening to [1 full album, 10-15 tracks]"
- With SOCIAL: "45-min partner workout with friend spotting"
- With ADVENTURE: "Run through new routes for 50 minutes"
""",

    (TaskTopic.PHYSICAL_ACTIVITY, Rarity.EPIC): """
**Metric Type:** TIME-BASED
**Duration:** 1-2 hours (60-120 minutes)
**Exercises:** 4-5+ basic movements, comprehensive training
**Intensity:** High volume, multiple rounds, rest periods included
**Pattern:** Serious training session with structure

**ALLOWED exercises ONLY:**
- All basic exercises: push-ups, squats, pull-ups, lunges, planks, burpees, dips, running, jumping jacks, sit-ups

**FORBIDDEN:**
- NO animal movements
- NO yoga, sports, dancing, martial arts

**Examples:**
- "2-hour training: multiple circuits of push-ups, squats, pull-ups, lunges with rest"
- "90-minute session: running + full bodyweight workout"
- "Complete 10 rounds of 5-exercise circuit over 100 minutes"

**Integration:**
- With MUSIC: "Train for 90 min while listening to [2-3 albums, 25-35 tracks]"
- With NUTRITION: "2-hour workout + post-workout meal prep"
""",

    (TaskTopic.PHYSICAL_ACTIVITY, Rarity.LEGENDARY): """
**Metric Type:** TIME-BASED
**Duration:** 3-5 hours
**Exercises:** All basic movements, marathon-style session
**Intensity:** Extreme endurance challenge, multiple phases
**Pattern:** Epic physical feat, not for average person

**ALLOWED exercises ONLY:**
- All basic exercises across full duration

**FORBIDDEN:**
- NO animal movements, yoga, sports, dancing, martial arts

**Examples:**
- "4-hour epic session: multiple circuits, long runs, max reps across all exercises"
- "3.5-hour endurance challenge: rotating through all basic movements"
- "5-hour training marathon with structured rest periods"

**Integration:**
- With MUSIC: "Train for 4 hours while listening to [4-5 albums, 50+ tracks]"
- With SOCIAL: "3-hour group workout challenge with friends"
""",

    # ========================================================================
    # ADVENTURE (TIME-BASED)
    # ========================================================================

    (TaskTopic.ADVENTURE, Rarity.COMMON): """
**Metric Type:** TIME-BASED
**Duration:** 10-20 minutes
**Focus:** Short walk, light exploration
**Scope:** Universal - anyone, anywhere
**Pattern:** Simple timed walk with basic observation

**FORBIDDEN:**
- NO specific landmarks ("Pushkin monument", "Tretyakov Gallery")
- NO location-dependent activities
- NO extreme exploration

**ALLOWED:**
- Timed walks
- Observation tasks
- New route exploration
- Photo documentation

**Examples:**
- "Walk for 15 minutes observing surroundings"
- "Take 12-minute walk on new route"
- "Explore neighborhood for 18 minutes"

**Integration:**
- With MUSIC: "Walk for 15 min while listening to [2-3 tracks]"
- With BRAIN: "Walk for 18 min while solving mental riddles"
""",

    (TaskTopic.ADVENTURE, Rarity.UNCOMMON): """
**Metric Type:** TIME-BASED
**Duration:** 30-60 minutes
**Focus:** Extended walk, active exploration
**Scope:** Universal, more engagement
**Pattern:** Structured exploration or purposeful walk

**FORBIDDEN:**
- NO specific landmarks
- NO location-dependent activities

**ALLOWED:**
- Extended walks with goals
- Photo hunts
- Route discovery
- Observation challenges

**Examples:**
- "Walk for 45 minutes taking only new routes"
- "Explore for 35 minutes documenting interesting findings"
- "Take 50-minute walk with observation tasks"

**Integration:**
- With MUSIC: "Walk for 45 min while listening to [mini-album, 5-8 tracks]"
- With READING: "Walk for 40 min, then read related article for 15 min"
- With SOCIAL: "Take 50-min walk with friend discussing topics"
""",

    (TaskTopic.ADVENTURE, Rarity.RARE): """
**Metric Type:** TIME-BASED
**Duration:** 1-2 hours
**Focus:** Substantial exploration, discovery session
**Scope:** Universal, significant engagement
**Pattern:** Long exploration with purpose

**FORBIDDEN:**
- NO specific landmarks
- NO location-dependent activities

**ALLOWED:**
- Long exploration walks
- Extensive photo documentation
- Multiple new routes
- Detailed observation tasks

**Examples:**
- "Explore for 90 minutes taking entirely new routes"
- "Take 1-hour exploration walk with comprehensive photo documentation"
- "Walk for 75 minutes focusing on urban/nature observation"

**Integration:**
- With MUSIC: "Walk for 1 hour while listening to [full album, 10-15 tracks]"
- With READING: "Walk 45 min + read outdoor for 30 min"
- With SOCIAL: "Take 90-min walk with friend having philosophical discussion"
- With BRAIN: "Walk for 1 hour while solving 10 mental puzzles"
""",

    (TaskTopic.ADVENTURE, Rarity.EPIC): """
**Metric Type:** TIME-BASED
**Duration:** 3-4 hours
**Focus:** Extended adventure, major exploration
**Scope:** Universal, serious time commitment
**Pattern:** Half-day exploration mission

**FORBIDDEN:**
- NO specific landmarks
- NO location-dependent activities

**ALLOWED:**
- Multi-hour exploration
- Extensive documentation
- Multiple objectives
- Comprehensive observation

**Examples:**
- "Take 3-hour exploration walk discovering entirely new areas"
- "Spend 3.5 hours walking and documenting observations"
- "Complete 4-hour adventure walk with multiple objectives"

**Integration:**
- With MUSIC: "Walk for 3 hours while listening to [2-3 albums, 25-35 tracks]"
- With CREATIVITY: "3-hour walk while noting creative ideas for later writing"
- With SOCIAL: "3.5-hour adventure walk with friend"
""",

    (TaskTopic.ADVENTURE, Rarity.LEGENDARY): """
**Metric Type:** TIME-BASED
**Duration:** 5+ hours
**Focus:** Epic day-long adventure
**Scope:** Universal, marathon exploration
**Pattern:** Full-day expedition

**FORBIDDEN:**
- NO specific landmarks
- NO location-dependent activities

**ALLOWED:**
- All-day exploration
- Extensive goals
- Multi-phase adventure
- Comprehensive documentation

**Examples:**
- "Take 5-hour epic exploration walk discovering new territories"
- "Spend 6 hours walking and documenting urban/nature exploration"
- "Complete full-day 7-hour adventure walk with multiple phases"

**Integration:**
- With MUSIC: "Walk for 5 hours while listening to [4-5 albums, 50+ tracks]"
- With SOCIAL: "5-hour group adventure with friends"
- With CREATIVITY: "6-hour walk gathering material for extensive writing"
""",

    # ========================================================================
    # READING (TIME-BASED)
    # ========================================================================

    (TaskTopic.READING, Rarity.COMMON): """
**Metric Type:** TIME-BASED
**Duration:** 10-15 minutes
**Material:** Short article, blog post, single chapter
**Focus:** Brief reading session, accessible content
**Pattern:** Quick focused reading

**CRITICAL:** Use DURATION only, NEVER page count!

**Examples:**
- "Read article on philosophy for 12 minutes"
- "Read one chapter for 15 minutes"
- "Read blog post for 10 minutes"

**Integration:**
- With NUTRITION: "Read for 12 min while eating healthy breakfast"
- With MUSIC: Less common, reading needs focus
""",

    (TaskTopic.READING, Rarity.UNCOMMON): """
**Metric Type:** TIME-BASED
**Duration:** 20-30 minutes
**Material:** Long article, multiple chapters, essay
**Focus:** Moderate reading session
**Pattern:** Focused reading period

**CRITICAL:** Use DURATION only, NEVER page count!

**Examples:**
- "Read for 25 minutes (book or long article)"
- "Read 2-3 chapters for 30 minutes"
- "Read long-form essay for 22 minutes"

**Integration:**
- With SOCIAL: "Read article for 25 min, then discuss with friend for 20 min"
- With NUTRITION: "Read for 30 min during meal"
""",

    (TaskTopic.READING, Rarity.RARE): """
**Metric Type:** TIME-BASED
**Duration:** 45-60 minutes
**Material:** Multiple chapters, substantial reading
**Focus:** Deep reading session
**Pattern:** Extended focused reading

**CRITICAL:** Use DURATION only, NEVER page count!

**Examples:**
- "Read for 50 minutes (novel or technical book)"
- "Read 3-5 chapters for 1 hour"
- "Read academic paper for 55 minutes"

**Integration:**
- With SOCIAL: "Read for 45 min then have 30-min discussion with friend"
- With CREATIVITY: "Read for 1 hour taking notes for later writing"
- With ADVENTURE: "Read outdoors for 50 minutes in park"
""",

    (TaskTopic.READING, Rarity.EPIC): """
**Metric Type:** TIME-BASED
**Duration:** 1.5-2 hours (90-120 minutes)
**Material:** Major section of book, multiple articles, extensive reading
**Focus:** Serious reading session
**Pattern:** Deep immersive reading

**CRITICAL:** Use DURATION only, NEVER page count!

**Examples:**
- "Read for 90 minutes (novel or non-fiction book)"
- "Read multiple research papers for 2 hours"
- "Deep reading session for 100 minutes"

**Integration:**
- With SOCIAL: "Read for 90 min then have extended discussion"
- With CREATIVITY: "Read for 2 hours gathering ideas for writing project"
""",

    (TaskTopic.READING, Rarity.LEGENDARY): """
**Metric Type:** TIME-BASED
**Duration:** 3-4 hours
**Material:** Extensive reading, full book sections, marathon session
**Focus:** Epic reading marathon
**Pattern:** Extended deep reading

**CRITICAL:** Use DURATION only, NEVER page count!

**Examples:**
- "Read for 3 hours (complete book sections)"
- "Deep reading marathon for 3.5 hours"
- "Read multiple books/papers for 4 hours"

**Integration:**
- With SOCIAL: "Read for 3 hours then have comprehensive group discussion"
- With CREATIVITY: "Read for 4 hours gathering extensive material for major writing"
""",

    # ========================================================================
    # MUSIC (COMPLEXITY-BASED)
    # ========================================================================

    (TaskTopic.MUSIC, Rarity.COMMON): """
**Metric Type:** COMPLEXITY-BASED (COUNT)
**Amount:** 1-2 landmark tracks
**Focus:** Brief listening, specific songs
**Pattern:** Single track or pair

**CRITICAL:** 
- Use TRACK COUNT only, NEVER mention time/duration!
- MUST specify exact track names and artists
- NO generic descriptions ("ambient music", "jazz tracks")

**FORBIDDEN albums:** Kind of Blue, Abbey Road, Dark Side of the Moon, OK Computer, Blonde on Blonde

**Suggested tracks from landmark albums:**
- Burial: Archangel, Untrue, Homeless
- Aphex Twin: Xtal, Tha, Pulsewidth
- Portishead: Glory Box, Sour Times
- Massive Attack: Teardrop, Angel

**Examples:**
- "Listen to Burial - Archangel (1 track)"
- "Listen to Aphex Twin - Xtal and Tha (2 tracks)"
- "Listen to Portishead - Glory Box and Sour Times (2 tracks)"

**Integration:**
- With PHYSICAL: "Do push-ups for 8 min while listening to [2 tracks]"
- With CREATIVITY: "Sketch while listening to [2 tracks]"
""",

    (TaskTopic.MUSIC, Rarity.UNCOMMON): """
**Metric Type:** COMPLEXITY-BASED (COUNT)
**Amount:** 1 mini-album/EP (3-6 tracks)
**Focus:** Short album or EP, complete small work
**Pattern:** Brief album experience

**CRITICAL:**
- Use TRACK COUNT only, NEVER time!
- MUST specify exact album/EP name, artist, and track count in parentheses

**FORBIDDEN:** Mainstream classics

**Suggested EPs:**
- Burial - Kindred EP (3 tracks)
- Aphex Twin - Windowlicker EP (3 tracks)
- Four Tet - Rounds selections (5 tracks)
- Boards of Canada - In A Beautiful Place (6 tracks)

**Or first half of albums:**
- Portishead - Dummy first 5 tracks
- Massive Attack - Mezzanine first 6 tracks

**Examples:**
- "Listen to Burial - Kindred EP (3 tracks)"
- "Listen to Portishead - Dummy first 5 tracks"
- "Listen to Four Tet selections (5 tracks)"

**Integration:**
- With PHYSICAL: "Do circuit workout for 25 min while listening to [EP, 5 tracks]"
- With ADVENTURE: "Walk for 30 min while listening to [EP, 4 tracks]"
""",

    (TaskTopic.MUSIC, Rarity.RARE): """
**Metric Type:** COMPLEXITY-BASED (COUNT)
**Amount:** 1 full landmark album (typically 10-15 tracks)
**Focus:** Complete album experience, deep listening
**Pattern:** Full album from start to finish

**CRITICAL:**
- Use ALBUM + TRACK COUNT, NEVER time!
- MUST specify: Artist - Album Title (X tracks)
- NO generic descriptions or mainstream classics

**Landmark albums by genre:**

**Trip-hop:**
- Portishead - Dummy (11 tracks)
- Massive Attack - Mezzanine (11 tracks)
- Tricky - Maxinquaye (15 tracks)
- Massive Attack - Blue Lines (9 tracks)

**Krautrock:**
- Can - Tago Mago (5 tracks)
- Neu! - Neu! (6 tracks)
- Faust - Faust IV (6 tracks)
- Can - Ege Bamyasi (6 tracks)

**Afrobeat:**
- Fela Kuti - Zombie (9 tracks)
- Fela Kuti - Expensive Shit (6 tracks)
- Tony Allen - Film of Life (7 tracks)

**IDM/Electronic:**
- Burial - Untrue (13 tracks)
- Aphex Twin - Selected Ambient Works 85-92 (13 tracks)
- Boards of Canada - Music Has the Right to Children (23 tracks)
- Autechre - Tri Repetae (11 tracks)
- Four Tet - Rounds (10 tracks)

**Post-rock:**
- Godspeed You! Black Emperor - Lift Your Skinny Fists (4 tracks)
- Mogwai - Young Team (10 tracks)
- Tortoise - Millions Now Living (11 tracks)

**Shoegaze:**
- My Bloody Valentine - Loveless (11 tracks)
- Slowdive - Souvlaki (11 tracks)
- Ride - Nowhere (10 tracks)

**Experimental/Jazz:**
- Alice Coltrane - Journey in Satchidananda (5 tracks)
- Pharoah Sanders - Karma (3 tracks)
- Sun Ra - Space Is the Place (8 tracks)
- Fishmans - Long Season (1 track, 35-min epic)
- This Heat - Deceit (11 tracks)

**Examples:**
- "Listen to Portishead - Dummy (11 tracks)"
- "Listen to Can - Tago Mago (5 tracks)"
- "Listen to Burial - Untrue (13 tracks)"
- "Listen to Fela Kuti - Zombie (9 tracks)"

**Integration:**
- With PHYSICAL: "Do 50-min workout while listening to Massive Attack - Mezzanine (11 tracks)"
- With ADVENTURE: "Walk for 1 hour while listening to Boards of Canada - MHTRTC (23 tracks)"
- With CREATIVITY: "Write for 1 hour while listening to Aphex Twin - SAW 85-92 (13 tracks)"
""",

    (TaskTopic.MUSIC, Rarity.EPIC): """
**Metric Type:** COMPLEXITY-BASED (COUNT)
**Amount:** 2-3 full albums (20-40 tracks total)
**Focus:** Extended listening, multiple album journey
**Pattern:** Genre exploration or artist deep-dive

**CRITICAL:**
- Specify ALL albums with exact names and track counts
- NEVER mention time/duration!
- Stay within related genres or coherent themes

**Suggested combinations:**

**Trip-hop trilogy:**
- Portishead - Dummy (11) + Massive Attack - Mezzanine (11) + Tricky - Maxinquaye (15) = 37 tracks

**Krautrock journey:**
- Can - Tago Mago (5) + Neu! - Neu! (6) + Faust - Faust IV (6) = 17 tracks

**IDM session:**
- Burial - Untrue (13) + Aphex Twin - SAW 85-92 (13) + Autechre - Tri Repetae (11) = 37 tracks

**Afrobeat marathon:**
- Fela Kuti - Zombie (9) + Expensive Shit (6) + Tony Allen - Film of Life (7) = 22 tracks

**Examples:**
- "Listen to Portishead - Dummy (11 tracks) + Massive Attack - Mezzanine (11 tracks) + Tricky - Maxinquaye (15 tracks)"
- "Listen to Can - Tago Mago (5 tracks) + Neu! - Neu! (6 tracks) + Faust IV (6 tracks)"

**Integration:**
- With PHYSICAL: "Train for 90 min while listening to [3 albums, 35 tracks]"
- With CREATIVITY: "Work on creative project while listening to [2 albums, 24 tracks]"
""",

    (TaskTopic.MUSIC, Rarity.LEGENDARY): """
**Metric Type:** COMPLEXITY-BASED (COUNT)
**Amount:** 4-5 full albums (40-60+ tracks)
**Focus:** Marathon listening, comprehensive genre exploration
**Pattern:** Day-long music journey

**CRITICAL:**
- Specify ALL albums with exact names and track counts
- NEVER mention time!
- Create coherent thematic journey

**Epic combinations:**

**Ultimate Trip-hop:**
- Portishead - Dummy (11) + Massive Attack - Mezzanine (11) + Blue Lines (9) + Tricky - Maxinquaye (15) + Martina Topley-Bird - Quixotic (12) = 58 tracks

**IDM Marathon:**
- Burial - Untrue (13) + Aphex Twin - SAW 85-92 (13) + Boards of Canada - MHTRTC (23) + Autechre - Tri Repetae (11) + Four Tet - Rounds (10) = 70 tracks

**Krautrock Day:**
- Can - Tago Mago (5) + Ege Bamyasi (6) + Neu! - Neu! (6) + Neu! 2 (6) + Faust - Faust IV (6) = 29 tracks

**Afrobeat Festival:**
- Fela Kuti - Zombie (9) + Expensive Shit (6) + Coffin for Head of State (5) + Tony Allen - Film of Life (7) + Antibalas - Security (10) = 37 tracks

**Examples:**
- "Listen to 5 landmark IDM albums: Burial - Untrue (13), Aphex Twin - SAW (13), Boards of Canada - MHTRTC (23), Autechre - Tri Repetae (11), Four Tet - Rounds (10) - total 70 tracks"
- "Listen to complete trip-hop journey: 5 albums spanning 58 tracks"

**Integration:**
- With PHYSICAL: "Train for 4 hours while listening to [5 albums, 60 tracks]"
- With CREATIVITY: "Work on major project while listening to [4 albums, 50 tracks]"
""",

    # ========================================================================
    # DEVELOPMENT (COMPLEXITY-BASED)
    # ========================================================================

    (TaskTopic.DEVELOPMENT, Rarity.COMMON): """
**Metric Type:** COMPLEXITY-BASED (PROBLEM COUNT)
**Amount:** 1 easy problem
**Focus:** Basic algorithm/coding task
**Difficulty:** Easy level on LeetCode/similar
**Pattern:** Single straightforward problem

**Topics:** Arrays, strings, basic math, simple loops

**Examples:**
- "Solve 1 easy array problem on LeetCode"
- "Complete 1 easy string manipulation problem"
- "Solve 1 easy hash table problem"

**Integration:**
- Hard to integrate naturally (requires focus)
- Can relate content: "Solve 1 easy problem about trees while learning data structures"
""",

    (TaskTopic.DEVELOPMENT, Rarity.UNCOMMON): """
**Metric Type:** COMPLEXITY-BASED (PROBLEM COUNT)
**Amount:** 1 medium problem
**Focus:** Intermediate algorithm/coding challenge
**Difficulty:** Medium level on LeetCode
**Pattern:** Single moderately complex problem

**Topics:** DP basics, trees, graphs, two pointers, sliding window

**Examples:**
- "Solve 1 medium problem on graphs"
- "Complete 1 medium dynamic programming problem"
- "Solve 1 medium tree traversal problem"

**Integration:**
- With CREATIVITY: "Solve 1 medium problem then write explanation article"
- With PRODUCTIVITY: "Solve 1 medium problem as part of structured study plan"
""",

    (TaskTopic.DEVELOPMENT, Rarity.RARE): """
**Metric Type:** COMPLEXITY-BASED (PROBLEM COUNT)
**Amount:** 2 medium problems
**Focus:** Multiple intermediate challenges
**Difficulty:** Medium level problems
**Pattern:** Two related or diverse problems

**Topics:** DP, graphs, trees, strings, backtracking

**Examples:**
- "Solve 2 medium problems on graphs"
- "Complete 2 medium DP problems"
- "Solve 2 medium problems: 1 tree + 1 graph"

**Integration:**
- With CREATIVITY: "Solve 2 medium problems and write detailed explanations"
- With MUSIC: "Solve 2 problems while listening to [album] in background"
- Domain integration: "Solve 2 medium algorithm problems with music theory applications"
""",

    (TaskTopic.DEVELOPMENT, Rarity.EPIC): """
**Metric Type:** COMPLEXITY-BASED (PROBLEM COUNT)
**Amount:** 1 hard problem
**Focus:** Advanced algorithm challenge
**Difficulty:** Hard level on LeetCode
**Pattern:** Single complex problem requiring deep thought

**Topics:** Advanced DP, complex graphs, advanced trees, bit manipulation, system design concepts

**Examples:**
- "Solve 1 hard dynamic programming problem"
- "Complete 1 hard graph problem"
- "Solve 1 hard problem involving multiple concepts"

**Integration:**
- With CREATIVITY: "Solve 1 hard problem and write comprehensive tutorial"
- With PRODUCTIVITY: "Solve 1 hard problem as capstone of study session"
""",

    (TaskTopic.DEVELOPMENT, Rarity.LEGENDARY): """
**Metric Type:** COMPLEXITY-BASED (PROBLEM COUNT)
**Amount:** 3 hard problems
**Focus:** Multiple advanced challenges
**Difficulty:** Hard level problems
**Pattern:** Marathon problem-solving session

**Topics:** Advanced algorithms across multiple domains

**Examples:**
- "Solve 3 hard algorithm problems"
- "Complete 3 hard problems: 1 DP + 1 graph + 1 tree"
- "Solve 3 diverse hard problems"

**Integration:**
- With CREATIVITY: "Solve 3 hard problems and create comprehensive guide"
- With SOCIAL: "Solve 3 hard problems then explain solutions to peer"
""",

    # ========================================================================
    # CREATIVITY (COMPLEXITY-BASED)
    # ========================================================================

    (TaskTopic.CREATIVITY, Rarity.COMMON): """
**Metric Type:** COMPLEXITY-BASED
**Amount:** 50-100 words OR 1-3 simple concepts/designs
**Focus:** Brief creative output
**Forms:** Flash fiction, micro-essay, simple sketch, logo concept
**Pattern:** Quick creative exercise

**Examples:**
- "Write 80-word micro-story"
- "Design 1 simple logo concept with sketch"
- "Write 100-word character description"
- "Create 2 UI component sketches"

**Integration:**
- With MUSIC: "Write 80 words while listening to [2 tracks]"
- With READING: "Read article then write 100-word response"
""",

    (TaskTopic.CREATIVITY, Rarity.UNCOMMON): """
**Metric Type:** COMPLEXITY-BASED
**Amount:** 300-500 words OR 5-10 concepts/designs
**Focus:** Moderate creative work
**Forms:** Short essay, scene, multiple sketches, design mockups
**Pattern:** Focused creative session

**Examples:**
- "Write 400-word short story"
- "Create 5 UI mockup concepts"
- "Write 500-word essay on [topic]"
- "Design 8 logo variations with sketches"

**Integration:**
- With MUSIC: "Write 500 words while listening to [EP, 5 tracks]"
- With DEVELOPMENT: "Write 400-word technical article about algorithm"
- Content integration: "Write 500-word essay about afrobeat music history"
""",

    (TaskTopic.CREATIVITY, Rarity.RARE): """
**Metric Type:** COMPLEXITY-BASED
**Amount:** 1000-1200 words OR 15-20 concepts/designs
**Focus:** Substantial creative work
**Forms:** Full short story, comprehensive essay, complete design system, UI kit
**Pattern:** Extended creative session

**Examples:**
- "Write 1200-word short story"
- "Design 1 complete UI mockup with 15 components"
- "Write 1000-word analytical essay"
- "Create 20 design concept variations"

**Integration:**
- With MUSIC: "Write 1000 words while listening to [full album, 11 tracks]"
- With READING: "Read for 1 hour then write 1200-word analysis"
- Content: "Write 1000-word essay about trip-hop genre evolution"
- With NUTRITION: "Design 15 meal presentation concepts with sketches"
""",

    (TaskTopic.CREATIVITY, Rarity.EPIC): """
**Metric Type:** COMPLEXITY-BASED
**Amount:** 2000-2500 words OR 30-50 designs/concepts
**Focus:** Major creative project
**Forms:** Long story, extended essay, comprehensive design work, portfolio piece
**Pattern:** Serious creative undertaking

**Examples:**
- "Write 2000-word short story"
- "Create complete design system with 40 components"
- "Write 2500-word analytical article"
- "Develop 50 creative concepts across project"

**Integration:**
- With MUSIC: "Write 2000 words while listening to [2-3 albums, 30 tracks]"
- With DEVELOPMENT: "Write 2000-word technical guide with code examples"
- Content: "Write 2500-word comprehensive essay on krautrock movement"
""",

    (TaskTopic.CREATIVITY, Rarity.LEGENDARY): """
**Metric Type:** COMPLEXITY-BASED
**Amount:** 5000+ words OR 80-100 designs/concepts
**Focus:** Epic creative marathon
**Forms:** Novella section, extensive essay, massive design portfolio, complete creative work
**Pattern:** All-day creative session

**Examples:**
- "Write 5000-word novella chapter"
- "Create comprehensive portfolio with 100 design concepts"
- "Write 5000-word thesis-style essay"
- "Develop complete design language with 80+ elements"

**Integration:**
- With MUSIC: "Write 5000 words while listening to [5 albums, 60 tracks]"
- With READING: "Read for 3 hours gathering material, then write 5000-word piece"
- Content: "Write 5000-word comprehensive history of IDM electronic music"
""",

    # ========================================================================
    # SOCIAL_SKILLS (COMPLEXITY-BASED)
    # ========================================================================

    (TaskTopic.SOCIAL_SKILLS, Rarity.COMMON): """
**Metric Type:** COMPLEXITY-BASED (INTERACTION COUNT)
**Amount:** 1 brief interaction
**Focus:** Simple social engagement
**Types:** 
  - STRANGERS: Brief conversation, asking question
  - FRIENDS: Short chat, catching up
**Pattern:** Single low-pressure interaction

**CRITICAL:** Face-to-face ONLY, NO online/digital

**Examples:**
- "Have 1 conversation with stranger (ask opinion or directions)"
- "Catch up with 1 friend for brief chat"
- "Approach 1 person and start conversation"

**Integration:**
- Hard to integrate meaningfully at COMMON level
""",

    (TaskTopic.SOCIAL_SKILLS, Rarity.UNCOMMON): """
**Metric Type:** COMPLEXITY-BASED (INTERACTION COUNT)
**Amount:** 2-3 interactions OR 1 paired activity
**Focus:** Multiple brief interactions or single activity with friend
**Types:**
  - STRANGERS: Multiple brief conversations
  - FRIENDS: Paired activity (cook, walk, discuss)
**Pattern:** Multiple simple OR one meaningful interaction

**CRITICAL:** Face-to-face ONLY

**Examples:**
- "Have conversations with 3 strangers"
- "Cook meal together with friend while discussing technique"
- "Have 2 meaningful conversations with friends"

**Integration:**
- With NUTRITION: "Cook dish with friend while teaching technique (1 paired activity)"
- With ADVENTURE: "Take 45-min walk with friend discussing topics"
- With READING: "Read article then discuss with friend (1 deep interaction)"
""",

    (TaskTopic.SOCIAL_SKILLS, Rarity.RARE): """
**Metric Type:** COMPLEXITY-BASED (INTERACTION COUNT)
**Amount:** 1 deep conversation/engagement OR 3-5 interactions
**Focus:** Extended meaningful interaction or multiple engagements
**Types:**
  - STRANGERS: Networking at event, multiple conversations
  - FRIENDS: Deep discussion, teaching session, extended activity
**Pattern:** Quality over quantity

**CRITICAL:** Face-to-face ONLY

**Examples:**
- "Have 1 deep philosophical discussion with friend"
- "Teach 1 friend a skill through conversation and demonstration"
- "Network at event: meaningful conversations with 5 people"

**Integration:**
- With READING: "Read 45-min article and have 1-hour discussion with friend"
- With DEVELOPMENT: "Teach friend 3 algorithm concepts through conversation"
- With ADVENTURE: "Take 90-min walk with friend having deep discussion"
- With MUSIC: "Discuss and analyze album together with friend (1 deep conversation)"
- With NUTRITION: "Cook complex meal with friend while discussing cooking philosophy"
""",

    (TaskTopic.SOCIAL_SKILLS, Rarity.EPIC): """
**Metric Type:** COMPLEXITY-BASED (EVENT SCALE)
**Amount:** 1 presentation/workshop to 5-8 people OR organizing group event
**Focus:** Public speaking or group facilitation
**Types:**
  - PUBLIC: Present topic to small group
  - FACILITATION: Lead discussion or workshop
  - TEACHING: Teach group of people
**Pattern:** Leadership and public engagement

**CRITICAL:** Face-to-face ONLY

**Examples:**
- "Give 1 presentation on topic to 5-7 people"
- "Lead 1 workshop for 6 participants"
- "Teach skill to group of 8 people"
- "Facilitate group discussion with 6 people"

**Integration:**
- With DEVELOPMENT: "Present technical topic to 7 people"
- With CREATIVITY: "Lead creative workshop for 6 participants"
- With READING: "Present book analysis to group of 5"
""",

    (TaskTopic.SOCIAL_SKILLS, Rarity.LEGENDARY): """
**Metric Type:** COMPLEXITY-BASED (EVENT SCALE)
**Amount:** Organize and host event for 10-15 people
**Focus:** Major social coordination and hosting
**Types:**
  - EVENT ORGANIZATION: Plan and execute gathering
  - HOSTING: Facilitate multi-person event
  - COORDINATION: Manage group dynamics
**Pattern:** Full event planning and execution

**CRITICAL:** Face-to-face ONLY

**Examples:**
- "Organize and host event for 12 people"
- "Plan and execute gathering for 10 participants"
- "Coordinate and facilitate meetup for 15 people"

**Integration:**
- With NUTRITION: "Organize dinner party for 12 people (cook and host)"
- With CREATIVITY: "Organize creative workshop/showcase for 10 people"
- With READING: "Organize book club event for 15 people"
""",

    # ========================================================================
    # NUTRITION (COMPLEXITY-BASED)
    # ========================================================================

    (TaskTopic.NUTRITION, Rarity.COMMON): """
**Metric Type:** COMPLEXITY-BASED (MEAL/ITEM COUNT)
**Amount:** 1 simple item
**Focus:** Basic eating/preparation
**Two types:**
  - TYPE 1 (CONSUME): Eat healthy item, drink water
  - TYPE 2 (COOK): Simple dish (eggs, sandwich, salad)
**Pattern:** Single basic action

**Examples:**
- "Eat 1 healthy meal with vegetables"
- "Cook simple breakfast (eggs or oatmeal)"
- "Prepare basic sandwich and salad"
- "Drink 2L water throughout day"

**Integration:**
- With READING: "Read for 12 min while eating healthy breakfast"
- With MUSIC: "Cook simple meal while listening to [2 tracks]"
""",

    (TaskTopic.NUTRITION, Rarity.UNCOMMON): """
**Metric Type:** COMPLEXITY-BASED (MEAL/DISH COUNT)
**Amount:** 1-2 moderate dishes OR 2-3 servings
**Focus:** Moderate cooking or consuming
**Two types:**
  - TYPE 1 (CONSUME): Eat 2-3 balanced meals
  - TYPE 2 (COOK): Cook 1-2 medium dishes (30-min meals)
**Pattern:** Moderate effort meal(s)

**Examples:**
- "Cook 1 pasta dish with vegetables (30-min recipe)"
- "Prepare 2 balanced meals for the day"
- "Cook stir-fry with protein and vegetables"
- "Meal prep 2 different salads"

**Integration:**
- With SOCIAL: "Cook dish with friend while teaching technique"
- With MUSIC: "Cook for 30 min while listening to [EP, 5 tracks]"
- With CREATIVITY: "Cook meal and photograph process artistically (5 photos)"
""",

    (TaskTopic.NUTRITION, Rarity.RARE): """
**Metric Type:** COMPLEXITY-BASED (DISH COUNT)
**Amount:** 1 complex dish from scratch OR 3 simpler dishes
**Focus:** Challenging cooking or substantial meal prep
**Type:** COOK only (complex preparation)
**Pattern:** Serious cooking session

**Cuisines:** Mediterranean, Asian, Mexican, Middle Eastern, Indian

**Examples:**
- "Cook 1 complex dish from scratch (60+ min recipe)"
- "Meal prep 3 different dishes"
- "Cook elaborate multi-component meal"
- "Prepare 1 challenging recipe requiring multiple techniques"

**Integration:**
- With MUSIC: "Cook for 1 hour while listening to [full album, 11 tracks]"
- With SOCIAL: "Cook complex recipe with friend discussing technique (1 deep interaction)"
- With CREATIVITY: "Cook dish and document process with 15 photos/descriptions"
""",

    (TaskTopic.NUTRITION, Rarity.EPIC): """
**Metric Type:** COMPLEXITY-BASED (MEAL COUNT)
**Amount:** 5-7 meals prepped OR 1 feast for 6-8 people
**Focus:** Major meal prep or event cooking
**Type:** COOK - extensive preparation
**Pattern:** Multi-hour cooking session

**Examples:**
- "Meal prep 5 balanced meals for the week"
- "Cook feast with 3-4 courses for 7 people"
- "Prepare 6 different dishes for meal prep"
- "Cook elaborate dinner party menu for 8"

**Integration:**
- With MUSIC: "Meal prep for 2 hours while listening to [2-3 albums, 30 tracks]"
- With SOCIAL: "Cook feast for 7 people and host dinner"
- With CREATIVITY: "Meal prep 5 dishes with artistic presentation (30 design photos)"
""",

    (TaskTopic.NUTRITION, Rarity.LEGENDARY): """
**Metric Type:** COMPLEXITY-BASED (MEAL COUNT)
**Amount:** 15-20 meals prepped OR feast for 10+ people
**Focus:** Epic meal prep marathon or major event
**Type:** COOK - marathon session
**Pattern:** All-day cooking

**Examples:**
- "Meal prep 18 balanced meals for 6 days"
- "Cook elaborate feast for 12 people with multiple courses"
- "Prepare 20 meals across different recipes"
- "Cook wedding-style feast for 15 people"

**Integration:**
- With MUSIC: "Meal prep for 4 hours while listening to [5 albums, 60 tracks]"
- With SOCIAL: "Cook and host feast for 12 people (major event)"
- With CREATIVITY: "Meal prep 20 meals with comprehensive photo documentation (80 photos)"
""",

    # ========================================================================
    # PRODUCTIVITY (COMPLEXITY-BASED)
    # ========================================================================

    (TaskTopic.PRODUCTIVITY, Rarity.COMMON): """
**Metric Type:** COMPLEXITY-BASED (TASK COUNT)
**Amount:** 1 simple plan OR 3-5 tasks organized
**Focus:** Basic organization/planning
**Forms:** Simple task list, basic schedule
**Pattern:** Quick planning session

**Examples:**
- "Create task list with 3 priority items"
- "Plan tomorrow's schedule (5 tasks)"
- "Organize 4 tasks with basic priorities"

**Integration:**
- Productivity is META - plans OTHER activities
- Hard to integrate naturally at COMMON level
""",

    (TaskTopic.PRODUCTIVITY, Rarity.UNCOMMON): """
**Metric Type:** COMPLEXITY-BASED (TASK COUNT)
**Amount:** 5-8 tasks organized with priorities
**Focus:** Moderate planning/organization
**Forms:** Prioritized list, basic time-blocking
**Pattern:** Structured planning session

**Examples:**
- "Organize and prioritize 5 tasks for tomorrow"
- "Create time-blocked schedule with 6 tasks"
- "Plan day with 7 tasks using Eisenhower matrix"

**Integration:**
- With READING: "Create reading schedule for week with 5 time blocks"
- With DEVELOPMENT: "Plan study schedule with 6 problems to solve"
- META: Plan activities across other topics
""",

    (TaskTopic.PRODUCTIVITY, Rarity.RARE): """
**Metric Type:** COMPLEXITY-BASED (TASK COUNT)
**Amount:** 8-10 tasks, full day time-blocked
**Focus:** Comprehensive daily planning
**Forms:** Full day schedule, detailed time-blocking, GTD system
**Pattern:** Thorough planning session

**Examples:**
- "Time-block full day with 10 tasks and priorities"
- "Create comprehensive schedule with 8 tasks and time allocations"
- "Plan day using GTD: 9 tasks with contexts and priorities"

**Integration:**
- With PHYSICAL: "Plan week workout schedule with 10 training sessions"
- With CREATIVITY: "Organize 8-task creative project with milestones"
- With READING: "Create detailed reading schedule for week (10 time blocks)"
- META: Comprehensive planning of other activities
""",

    (TaskTopic.PRODUCTIVITY, Rarity.EPIC): """
**Metric Type:** COMPLEXITY-BASED (TASK COUNT)
**Amount:** 15 tasks organized, full week planned
**Focus:** Weekly comprehensive planning
**Forms:** Week schedule, multiple systems, detailed tracking
**Pattern:** Extended planning session

**Examples:**
- "Plan entire week with 15 tasks, priorities, and time blocks"
- "Create comprehensive GTD system for 15 ongoing tasks"
- "Organize week with 15 tasks using multiple frameworks"

**Integration:**
- With PHYSICAL: "Plan 2-week training program with 15 sessions"
- With DEVELOPMENT: "Organize learning path with 15 study sessions"
- With CREATIVITY: "Plan creative project timeline with 15 milestones"
- META: Multi-day planning across topics
""",

    (TaskTopic.PRODUCTIVITY, Rarity.LEGENDARY): """
**Metric Type:** COMPLEXITY-BASED (TASK COUNT)
**Amount:** 25+ tasks, comprehensive system for multiple weeks
**Focus:** Major productivity system implementation
**Forms:** Multi-week planning, complete GTD system, habit tracking
**Pattern:** Building entire productivity infrastructure

**Examples:**
- "Create comprehensive system for 25 tasks with reviews and tracking"
- "Plan month with 30 tasks across all life areas"
- "Build complete productivity system managing 25+ ongoing tasks"

**Integration:**
- With READING: "Plan quarter reading schedule with 25+ books time-blocked"
- With PHYSICAL: "Design month training program with 25 sessions"
- With DEVELOPMENT: "Create 3-month learning path with 25 milestones"
- META: Comprehensive life planning system
""",

    # ========================================================================
    # BRAIN (COMPLEXITY-BASED)
    # ========================================================================

    (TaskTopic.BRAIN, Rarity.COMMON): """
**Metric Type:** COMPLEXITY-BASED (PUZZLE COUNT)
**Amount:** 1-2 easy puzzles/challenges
**Focus:** Simple mental exercise
**Forms:** Easy sudoku, simple riddles, basic memory
**Pattern:** Quick brain warm-up

**Examples:**
- "Solve 2 easy sudoku puzzles"
- "Complete 1 simple crossword"
- "Solve 2 basic logic riddles"

**Integration:**
- With ADVENTURE: "Walk for 15 min while solving 2 mental riddles"
- With PHYSICAL: Limited (both need focus)
""",

    (TaskTopic.BRAIN, Rarity.UNCOMMON): """
**Metric Type:** COMPLEXITY-BASED (PUZZLE COUNT)
**Amount:** 5 medium puzzles/problems
**Focus:** Moderate mental challenge
**Forms:** Medium sudoku, chess puzzles, memory sequences
**Pattern:** Focused brain workout

**Examples:**
- "Solve 5 medium chess tactics puzzles"
- "Complete 5 medium sudoku puzzles"
- "Solve 5 logic grid puzzles"

**Integration:**
- With ADVENTURE: "Walk for 30 min while solving 5 mental arithmetic problems"
- With MUSIC: "Solve 5 puzzles while listening to [ambient album] in background"
""",

    (TaskTopic.BRAIN, Rarity.RARE): """
**Metric Type:** COMPLEXITY-BASED (PUZZLE COUNT)
**Amount:** 15 hard puzzles/challenges
**Focus:** Serious mental workout
**Forms:** Hard puzzles across categories, complex logic
**Pattern:** Extended brain training

**Examples:**
- "Solve 15 hard logic puzzles"
- "Complete 15 chess tactics (intermediate-advanced)"
- "Solve 15 challenging sudoku/kakuro puzzles"

**Integration:**
- With MUSIC: "Solve 15 puzzles analyzing patterns while [ambient album] plays"
- Content: "Solve 10 chess puzzles then analyze 2 classical music structures"
- Limited integration (requires focus)
""",

    (TaskTopic.BRAIN, Rarity.EPIC): """
**Metric Type:** COMPLEXITY-BASED (PROBLEM COUNT)
**Amount:** 30 intensive problems/challenges
**Focus:** Major mental marathon
**Forms:** Mixed hard puzzles, advanced challenges
**Pattern:** Extended brain workout session

**Examples:**
- "Complete 30 intensive problems across multiple categories"
- "Solve 30 hard chess puzzles"
- "Complete 30 challenging mental exercises (mixed types)"

**Integration:**
- Limited (requires sustained focus)
- Content: "Solve 30 puzzles including music theory problems"
""",

    (TaskTopic.BRAIN, Rarity.LEGENDARY): """
**Metric Type:** COMPLEXITY-BASED (CHALLENGE COUNT)
**Amount:** 80-100 brain challenges
**Focus:** Epic mental endurance
**Forms:** Marathon puzzle session, all categories
**Pattern:** All-day brain training

**Examples:**
- "Solve 80 brain challenges across multiple categories"
- "Complete 100 puzzles: sudoku, chess, logic, memory, math"
- "Solve 100-puzzle marathon mixing all types"

**Integration:**
- Minimal (requires sustained deep focus)
- Content-based only: problems about other topics
""",

    # ========================================================================
    # CYBERSPORT (COMPLEXITY-BASED)
    # ========================================================================

    (TaskTopic.CYBERSPORT, Rarity.COMMON): """
**Metric Type:** COMPLEXITY-BASED (DRILL COUNT)
**Amount:** 10 drills
**Focus:** Basic mechanical practice
**Forms:** Aim training, basic drills
**Pattern:** Short practice session

**CRITICAL:** Use DRILL COUNT, NEVER mention time/duration!

**Drills:** Flick shots, tracking, crosshair placement

**Examples:**
- "Complete 10 aim drills (flick shots)"
- "Do 10 tracking drills"
- "Complete 10 crosshair placement drills"

**Integration:**
- Hard to integrate (requires focus)
""",

    (TaskTopic.CYBERSPORT, Rarity.UNCOMMON): """
**Metric Type:** COMPLEXITY-BASED (DRILLS + MATCHES)
**Amount:** 20 drills + 2 matches
**Focus:** Practice + application
**Forms:** Aim drills + ranked/casual games
**Pattern:** Drills followed by gameplay

**CRITICAL:** Use DRILL + MATCH COUNT, NEVER time!

**Examples:**
- "Complete 20 drills + play 2 ranked matches"
- "Do 15 aim drills + 15 movement drills + 2 games"
- "Complete 20 focused drills then 2 matches"

**Integration:**
- With PRODUCTIVITY: "Complete 20 drills + 2 matches while tracking performance metrics"
""",

    (TaskTopic.CYBERSPORT, Rarity.RARE): """
**Metric Type:** COMPLEXITY-BASED (DRILLS + MATCHES)
**Amount:** 35 drills + 3 ranked matches
**Focus:** Serious practice + competitive play
**Forms:** Comprehensive drills + ranked gameplay
**Pattern:** Full training then competitive matches

**CRITICAL:** DRILL + MATCH COUNT only, NEVER time!

**Drills:** Flicks, tracking, spray control, movement, utility, peeking

**Examples:**
- "Complete 35 drills + 3 ranked matches with focus"
- "Do 35 comprehensive drills across all skills + 3 competitive games"
- "Complete 30 aim drills + 5 utility drills + 3 ranked matches"

**Integration:**
- With BRAIN: "Complete 35 drills + 3 matches analyzing opponent patterns each game"
- With PRODUCTIVITY: "Do 35 drills + 3 matches tracking metrics for improvement"
""",

    (TaskTopic.CYBERSPORT, Rarity.EPIC): """
**Metric Type:** COMPLEXITY-BASED (DRILLS + MATCHES)
**Amount:** 60 drills + 5 competitive games
**Focus:** Extended training + competitive session
**Forms:** Marathon drill session + multiple ranked games
**Pattern:** Comprehensive training day

**CRITICAL:** DRILL + MATCH COUNT only, NO time!

**Examples:**
- "Complete 60 drills + 5 competitive games"
- "Do 60 comprehensive drills across all mechanics + 5 ranked matches"
- "Complete 50 aim drills + 10 utility drills + 5 competitive games"

**Integration:**
- With BRAIN: "Do 60 drills + 5 matches analyzing game theory decisions"
- With PRODUCTIVITY: "Complete 60 drills + 5 matches with detailed performance tracking"
""",

    (TaskTopic.CYBERSPORT, Rarity.LEGENDARY): """
**Metric Type:** COMPLEXITY-BASED (DRILLS + MATCHES)
**Amount:** 100 drills + 10 ranked games
**Focus:** Epic training marathon
**Forms:** Full-day intensive training
**Pattern:** All-day competitive gaming session

**CRITICAL:** DRILL + MATCH COUNT only, NO time!

**Examples:**
- "Complete 100 drills + 10 ranked matches"
- "Do 100 comprehensive drills across all skills + 10 competitive games"
- "Complete 80 aim drills + 20 utility drills + 10 ranked matches"

**Integration:**
- Minimal (requires sustained focus and stamina)
- With PRODUCTIVITY: "Complete 100 drills + 10 matches with comprehensive analytics"
""",

    # ========================================================================
    # LANGUAGE_LEARNING (COMPLEXITY-BASED)
    # ========================================================================

    (TaskTopic.LANGUAGE_LEARNING, Rarity.COMMON): """
**Metric Type:** COMPLEXITY-BASED (WORD COUNT)
**Amount:** 5-10 new words with pronunciation
**Focus:** Basic vocabulary acquisition
**Forms:** Flashcards, pronunciation practice, simple usage
**Pattern:** Quick learning session

**Examples:**
- "Learn 8 new words with pronunciation and usage"
- "Study 10 vocabulary words with example sentences"
- "Learn 5 new words and practice pronunciation"

**Integration:**
- With NUTRITION: "Learn 8 food-related words while preparing meal"
- With MUSIC: "Learn 10 words while listening to [2 tracks] in background"
""",

    (TaskTopic.LANGUAGE_LEARNING, Rarity.UNCOMMON): """
**Metric Type:** COMPLEXITY-BASED (WORDS + SENTENCES)
**Amount:** 18-20 words + 5 sentences written
**Focus:** Vocabulary + basic production
**Forms:** Flashcards, sentence construction, writing practice
**Pattern:** Moderate learning session

**Examples:**
- "Learn 20 new words + write 5 sentences in target language"
- "Study 18 vocabulary words + construct 5 example sentences"
- "Learn 20 words and write 5 practice sentences"

**Integration:**
- With READING: "Learn 20 words from article in target language"
- With NUTRITION: "Learn 20 cooking terms while preparing dish"
- With CREATIVITY: "Learn 20 words + write 5 creative sentences"
""",

    (TaskTopic.LANGUAGE_LEARNING, Rarity.RARE): """
**Metric Type:** COMPLEXITY-BASED (WORDS + EXERCISES)
**Amount:** 45-50 words + 10 sentences + 3 conversation topics
**Focus:** Substantial vocabulary + conversation practice
**Forms:** Extensive vocabulary, writing, speaking practice
**Pattern:** Comprehensive language session

**Examples:**
- "Learn 50 words + write 10 sentences + practice 3 dialogue topics"
- "Study 45 vocabulary words + complete 10 writing exercises + practice 3 conversations"
- "Learn 50 words + construct 10 complex sentences + practice 3 speaking scenarios"

**Integration:**
- With READING: "Read 45-min text in target language and note 50 new words"
- With SOCIAL: "Learn 50 words + practice 3 conversation topics with language partner"
- With CREATIVITY: "Learn 50 words + write 10 sentences + compose 3 short dialogues"
- With NUTRITION: "Learn 50 culinary terms while cooking dish"
""",

    (TaskTopic.LANGUAGE_LEARNING, Rarity.EPIC): """
**Metric Type:** COMPLEXITY-BASED (WORDS + EXERCISES)
**Amount:** 90-100 words + 15 sentences + 5 dialogue exercises
**Focus:** Major vocabulary boost + extensive practice
**Forms:** Large vocabulary set, extensive writing and speaking
**Pattern:** Intensive language day

**Examples:**
- "Learn 100 words + write 15 complex sentences + complete 5 dialogue role-plays"
- "Study 90 vocabulary words + complete 15 writing exercises + practice 5 conversation scenarios"
- "Learn 100 words across themes + construct 15 sentences + practice 5 speaking exercises"

**Integration:**
- With READING: "Read 90-min text in target language gathering 100 new words"
- With SOCIAL: "Learn 100 words + have 5 extended conversations in target language"
- With CREATIVITY: "Learn 100 words + write 15 sentences + compose 5 dialogues"
""",

    (TaskTopic.LANGUAGE_LEARNING, Rarity.LEGENDARY): """
**Metric Type:** COMPLEXITY-BASED (WORDS + EXERCISES)
**Amount:** 180-200 words + 20 sentences + 10 speaking exercises
**Focus:** Epic vocabulary marathon + comprehensive practice
**Forms:** Massive vocabulary, extensive production practice
**Pattern:** Full-day immersion

**Examples:**
- "Learn 200 words + write 20 complex sentences + complete 10 speaking/writing exercises"
- "Study 180 vocabulary words + construct 20 varied sentences + practice 10 conversation scenarios"
- "Learn 200 words across multiple themes + complete 20 writing exercises + do 10 dialogue practices"

**Integration:**
- With READING: "Read for 3 hours in target language gathering 200 new words"
- With SOCIAL: "Learn 200 words + have 10 extended conversations throughout day"
- With CREATIVITY: "Learn 200 words + write 20 sentences + compose 10 short texts/dialogues"
""",
}


def get_requirements(topic: TaskTopic, rarity: Rarity) -> str:
    """
    Получить детальные требования для конкретной пары топик+редкость.

    Args:
        topic: Топик задачи
        rarity: Редкость задачи

    Returns:
        Строка с детальными требованиями для генерации задачи
    """
    key = (topic, rarity)
    requirements = TOPIC_RARITY_REQUIREMENTS.get(key)

    if not requirements:
        # Fallback на случай если пара не найдена
        return f"""
Generate task for {topic.value} with {rarity.value} difficulty.
Use appropriate scope and metrics for this combination.
Follow general rules for this topic type.
"""

    return requirements.strip()
