from typing import List, Dict

from src.avro.enums.task_topic import TaskTopic
from src.avro.enums.rarity import Rarity

DIVERSITY_HINTS: Dict[TaskTopic, List[str]] = {
    TaskTopic.PHYSICAL_ACTIVITY: [
        "Focus on push-up variations (wide grip, close grip, decline, incline, diamond)",
        "Emphasize bodyweight squats (standard, jump squats, single-leg, pistol squats)",
        "Use pull-ups or chin-ups with different grips (wide, narrow, neutral)",
        "Focus on plank holds (standard, side plank, plank-to-downdog, walking plank)",
        "Emphasize lunges (forward, reverse, walking, jumping lunges)",
        "Use burpees for full-body work (standard, burpee tuck jumps, burpee pull-ups)",
        "Focus on running or jogging (intervals, tempo runs, fartlek, hill sprints)",
        "Emphasize dips if parallel bars available (chest dips, tricep dips, L-sit dips)",
        "Use jumping jacks for cardio (standard, seal jacks, plank jacks)",
        "Focus on sit-ups and crunches for core (bicycle crunches, Russian twists, leg raises)",
        "Emphasize explosive movements (jump squats, box jumps, explosive push-ups, clap push-ups)",
        "Use isometric holds (wall sits, dead hangs, L-sits, hollow body holds)",
        "Focus on tempo variations (3-1-3 tempo, pause reps, slow negatives)",
        "Emphasize unilateral movements (single-leg deadlifts, one-arm push-ups, single-leg bridges)",
        "Use compound movements (burpees, thrusters, man-makers, mountain climbers)",
    ],
    TaskTopic.MUSIC: [
        "Choose krautrock (Can - Tago Mago, Neu!, Faust, Harmonia)",
        "Select afrobeat (Fela Kuti - Zombie, Expensive Shit, Tony Allen)",
        "Use trip-hop (Portishead, Massive Attack, Tricky, Morcheeba)",
        "Choose post-rock (Godspeed You! Black Emperor, Mogwai, Explosions in the Sky, Tortoise)",
        "Select IDM (Aphex Twin, Boards of Canada, Autechre, Squarepusher)",
        "Use shoegaze (My Bloody Valentine, Slowdive, Ride, Lush)",
        "Choose avant-garde jazz (Alice Coltrane, Pharoah Sanders, Sun Ra, Don Cherry)",
        "Select experimental (Fishmans - Long Season, This Heat, Faust, The Residents)",
        "Use electronic (Burial, Four Tet, Flying Lotus, Nicolas Jaar)",
        "Choose dub techno (Basic Channel, Rhythm & Sound, Deepchord, Maurizio)",
        "Select minimal techno (Richie Hawtin, Robert Hood, Jeff Mills, Ricardo Villalobos)",
        "Use dark ambient (Lustmord, Atrium Carceri, Raison d'être, Kammarheit)",
        "Choose progressive house (Sasha, John Digweed, Eric Prydz, Guy J)",
        "Select future garage (Burial followers, James Blake, SBTRKT, Mount Kimbie)",
        "Use math rock (Don Caballero, Battles, Toe, Hella)",
        "Choose drone (Sunn O))), Earth, Stars of the Lid, Tim Hecker)",
        "Select UK garage (MJ Cole, Artful Dodger, Craig David early work)",
        "Use downtempo (Bonobo, Thievery Corporation, Nightmares on Wax, Zero 7)",
    ],
    TaskTopic.DEVELOPMENT: [
        "Focus on graph algorithms (BFS, DFS, shortest path, topological sort)",
        "Emphasize dynamic programming patterns (knapsack, LCS, LIS, coin change)",
        "Use bit manipulation and bitwise operations (XOR tricks, bit masks, power of two)",
        "Focus on tree traversals and binary search trees (inorder, preorder, postorder, Morris)",
        "Emphasize sliding window or two-pointer techniques (maximum subarray, longest substring)",
        "Use backtracking and recursion problems (N-queens, sudoku solver, permutations)",
        "Focus on system design patterns (singleton, factory, observer, strategy, decorator)",
        "Emphasize test-driven development (write tests first, red-green-refactor cycle)",
        "Use refactoring exercises on legacy code (extract method, rename, move class)",
        "Focus on concurrent programming challenges (thread safety, deadlocks, race conditions)",
        "Emphasize greedy algorithms (interval scheduling, Huffman coding, fractional knapsack)",
        "Use divide and conquer (merge sort variations, quick select, Strassen's algorithm)",
        "Focus on hash map optimization patterns (two sum, group anagrams, frequency counting)",
        "Emphasize monotonic stack/queue problems (next greater element, sliding window maximum)",
        "Use prefix sum and difference arrays (range sum query, subarray sum)",
        "Focus on trie and suffix structures (word search, autocomplete, longest common prefix)",
        "Emphasize union-find (disjoint sets, connected components, Kruskal's algorithm)",
    ],
    TaskTopic.CREATIVITY: [
        "Write in second-person perspective (you walk, you see, you feel)",
        "Use stream-of-consciousness style (no punctuation, free flow, Joycean)",
        "Create non-linear narrative structure (flashbacks, parallel timelines, fragmented)",
        "Focus on sensory details (sounds, textures, smells, tastes, temperatures)",
        "Use dialogue-only format (no narration, only conversations)",
        "Create speculative fiction or magical realism (subtle fantasy elements in real world)",
        "Focus on character emotions through actions, not descriptions (show don't tell)",
        "Use constraints (no letter 'e', only 100 words, one sentence story)",
        "Create visual mind maps or concept boards (sketch ideas, connect concepts)",
        "Focus on world-building elements (languages, cultures, systems, geography)",
        "Use unreliable narrator perspective (narrator lies, contradicts, misremembers)",
        "Create reverse chronology structure (end to beginning, backward timeline)",
        "Focus on epistolary format (letters, emails, texts, diary entries)",
        "Use found footage or documentary style (interview transcripts, reports)",
        "Create multiple timelines or parallel narratives (alternate realities, different POVs)",
        "Focus on minimalist prose (Hemingway style, short sentences, sparse description)",
        "Use absurdist or surrealist elements (Kafka, Ionesco, dreamlike logic)",
    ],
    TaskTopic.SOCIAL_SKILLS: [
        "Practice active listening without interrupting (maintain eye contact, nod, paraphrase)",
        "Use open-ended questions to deepen conversations (how, why, what if)",
        "Practice giving specific, genuine compliments (notice details, be sincere)",
        "Focus on mirroring body language subtly (match posture, gestures, energy)",
        "Practice storytelling with clear structure (setup, conflict, resolution, lesson)",
        "Use the cold approach with strangers in public spaces (ask time, directions, opinion)",
        "Practice remembering and using people's names (repeat, associate, use 3 times)",
        "Focus on finding common ground quickly (shared interests, experiences, values)",
        "Practice graceful disagreement without conflict (acknowledge, reframe, bridge)",
        "Use humor and self-deprecation appropriately (laugh at yourself, timing, read room)",
        "Practice vulnerability and authentic sharing (share struggles, admit mistakes)",
        "Focus on asking for help or favors (Ben Franklin effect, build rapport)",
        "Use power poses before interactions (stand tall, expand, boost confidence)",
        "Practice giving and receiving constructive feedback (sandwich method, be specific)",
        "Focus on network expansion (introduce people, connect others, be connector)",
    ],
    TaskTopic.NUTRITION: [
        "Focus on fermented foods (kimchi, sauerkraut, miso, kombucha, kefir)",
        "Emphasize plant-based protein sources (lentils, chickpeas, tofu, tempeh, seitan)",
        "Use spice blends from different cuisines (garam masala, za'atar, berbere, harissa)",
        "Focus on batch cooking grains and legumes (quinoa, brown rice, black beans)",
        "Emphasize seasonal and local ingredients (farmer's market, CSA box, what's in season)",
        "Use one-pot or sheet-pan meals for efficiency (roast vegetables and protein together)",
        "Focus on protein-forward breakfasts (eggs, Greek yogurt, protein smoothies)",
        "Emphasize colorful vegetables (eat the rainbow, phytonutrients, variety)",
        "Use meal prep containers for portion control (glass containers, divide macros)",
        "Focus on hydration tracking alongside meals (water intake, herbal teas)",
        "Emphasize whole food ingredients (avoid processed, cook from scratch)",
        "Use ethnic cuisine exploration (Thai, Ethiopian, Peruvian, Georgian)",
        "Focus on omega-3 rich foods (salmon, mackerel, walnuts, flaxseeds, chia)",
        "Emphasize probiotic and prebiotic foods (yogurt, garlic, onions, asparagus)",
    ],
    TaskTopic.PRODUCTIVITY: [
        "Use time-blocking with strict boundaries (calendar blocks, no interruptions)",
        "Focus on single-tasking (no multitasking, one thing at a time, deep work)",
        "Apply the 2-minute rule (do it now if under 2 minutes, clear small tasks)",
        "Use the Eisenhower matrix (urgent vs important, quadrant planning)",
        "Focus on eating the frog (hardest task first, morning productivity)",
        "Use Pomodoro with 25/5 intervals (timer, focused bursts, regular breaks)",
        "Focus on batching similar tasks together (email blocks, calls block, errands)",
        "Use the 3 MIT method (3 Most Important Tasks, daily priorities)",
        "Apply Pareto principle (80/20 rule, focus on high-impact activities)",
        "Focus on environment design (remove distractions, optimize workspace, friction reduction)",
        "Use Getting Things Done (GTD) system (capture, clarify, organize, reflect, engage)",
        "Focus on energy management over time management (work with natural rhythms)",
        "Use commitment devices (accountability partner, public declaration, stakes)",
        "Focus on habit stacking (link new habit to existing one, anchor behavior)",
    ],
    TaskTopic.ADVENTURE: [
        "Explore industrial areas or abandoned places (safely, urban decay, history)",
        "Focus on street art and murals in unexpected neighborhoods (graffiti tours)",
        "Visit local historical markers and read plaques (learn city history)",
        "Explore rooftops or elevated viewpoints (safe access, city panoramas)",
        "Focus on hidden parks or green spaces (pocket parks, community gardens)",
        "Visit ethnic neighborhoods and cultural districts (Chinatown, Little Italy, explore)",
        "Explore waterfronts, rivers, or canals (walking paths, bridges, water views)",
        "Focus on architectural details in old buildings (ornaments, styles, eras)",
        "Visit local markets or bazaars (food markets, flea markets, farmer's markets)",
        "Explore underground passages or metro art (subway stations, tunnels, public art)",
        "Focus on discovering new streets (take random turns, get deliberately lost)",
        "Visit public libraries or bookstores (browse sections, discover books)",
        "Explore university campuses (architecture, museums, public lectures)",
    ],
    TaskTopic.BRAIN: [
        "Focus on chess tactics (pins, forks, skewers, discovered attacks)",
        "Use logic grid puzzles (zebra puzzles, Einstein's riddle variations)",
        "Solve Sudoku variants (killer sudoku, samurai, irregular, X-sudoku)",
        "Focus on spatial reasoning puzzles (tangrams, pentominoes, cube nets)",
        "Use memory techniques (method of loci, linking, peg system, chunking)",
        "Solve mathematical riddles and paradoxes (Monty Hall, unexpected hanging)",
        "Focus on pattern recognition (sequences, number patterns, visual patterns)",
        "Use lateral thinking puzzles (situation puzzles, mystery scenarios)",
        "Solve cryptic crosswords or ciphers (Caesar cipher, substitution, cryptograms)",
        "Focus on probability and combinatorics problems (permutations, combinations)",
        "Use Rubik's cube solving (learn algorithms, speed cubing, blindfolded)",
        "Focus on mental arithmetic (rapid calculation, estimation, Vedic math)",
        "Solve Kakuro puzzles (cross-sum puzzles, numerical clues)",
        "Use SET card game patterns (find sets, visual-spatial reasoning)",
    ],
    TaskTopic.CYBERSPORT: [
        "Focus on flick accuracy drills (fast precise clicks, target switching)",
        "Emphasize tracking moving targets smoothly (consistent aim, no flicks)",
        "Use spray pattern control practice (recoil control, burst fire, tap shooting)",
        "Focus on crosshair placement (pre-aiming angles, head level)",
        "Emphasize counter-strafing mechanics (stop before shooting, accuracy)",
        "Use utility lineups memorization (smokes, flashes, mollies, specific spots)",
        "Focus on peeking angles and timing (jiggle peek, shoulder peek, wide swing)",
        "Emphasize movement optimization (bunny hops, strafes, air acceleration)",
        "Use demo review for decision-making analysis (watch replays, learn mistakes)",
        "Focus on economy management in ranked matches (save rounds, force buys, eco)",
        "Use aim trainers with specific scenarios (Kovaak's, Aim Lab, task-focused)",
        "Focus on warm-up routines (consistent pre-game, muscle memory)",
    ],
    TaskTopic.READING: [
        "Focus on classic literature (pre-1950, canonical works, timeless themes)",
        "Read long-form investigative journalism (New Yorker, Atlantic, in-depth reporting)",
        "Focus on philosophy or critical theory (existentialism, phenomenology, Frankfurt School)",
        "Read technical documentation or whitepapers (research papers, RFCs, academic)",
        "Focus on biographies of unconventional figures (artists, rebels, innovators)",
        "Read scientific papers or research studies (Nature, Science, peer-reviewed)",
        "Focus on translated literature (non-English origins, world literature, Nobel winners)",
        "Read essay collections or thought pieces (Montaigne, Baldwin, Didion, Sontag)",
        "Focus on historical non-fiction (deep dives, narrative history, primary sources)",
        "Read genre-blending experimental fiction (postmodern, metafiction, magical realism)",
        "Focus on poetry collections (contemporary, classic, diverse voices)",
        "Read graphic novels and visual literature (Maus, Watchmen, Sandman, Persepolis)",
    ],
    TaskTopic.LANGUAGE_LEARNING: [
        "Focus on colloquial expressions and slang (real speech, informal language)",
        "Use sentence mining from native content (extract phrases, study in context)",
        "Focus on shadowing native speakers (repeat after audio, mimic intonation)",
        "Emphasize writing without translation apps (think in target language, natural phrasing)",
        "Use spaced repetition with context sentences (Anki, full sentences not words)",
        "Focus on pronunciation drills (minimal pairs, difficult sounds, IPA)",
        "Emphasize active recall over passive review (test yourself, don't just read)",
        "Use comprehensible input (reading/listening just above level, i+1 principle)",
        "Focus on grammatical patterns in context (notice patterns, inductive learning)",
        "Emphasize conversational practice with natives (language exchange, italki, tandem)",
        "Use monolingual dictionaries (definitions in target language, native thinking)",
        "Focus on listening to podcasts at native speed (gradual speed increase, natural speech)",
    ],
    TaskTopic.MOTION: [
        "Vary walking pace: leisurely stroll (3-4 km/h), brisk walk (5-6 km/h), power walking (6-7 km/h)",
        "Alternate terrain types: flat urban streets, gentle hills, park trails, waterfront paths, cobblestone streets",
        "Use interval structures: 5-min walk / 2-min faster pace cycles, pyramid intervals (gradual acceleration/deceleration)",
        "Focus on route geometry: circular loops (return to start), point-to-point (A→B), figure-8 patterns, spiral outward/inward",
        "Emphasize time-of-day variations: sunrise walk (golden hour lighting), midday sun exposure, sunset stroll (changing colors), blue hour walking (dusk ambiance)",
        "Vary sensory focus: auditory walking (notice 5 distinct sounds), visual scanning (spot 10 specific colors), tactile awareness (feel ground textures through shoes)",
        "Use elevation profiles: flat terrain only, consistent gentle incline, rolling hills (repeated ascents/descents), stair segments integrated naturally",
        "Focus on surface diversity: pavement, gravel paths, grass fields, wooden boardwalks, sand (beach/dunes), mixed surfaces within single session",
        "Emphasize mindful locomotion: synchronized breathing with steps (e.g., inhale 4 steps/exhale 4 steps), heel-to-toe rolling gait focus, posture awareness (spine alignment)",
        "Vary social context: solo walking (internal focus), parallel walking with companion (minimal conversation), walking while listening to ambient sounds only (no audio)",
        "Use weather integration: light drizzle walk (waterproof gear), crisp autumn air, morning fog immersion, gentle breeze awareness (face wind direction changes)",
        "Focus on rhythm variations: steady metronome pace, natural acceleration/deceleration with terrain, syncopated stepping patterns (long-short-long steps)",
        "Emphasize directional changes: cardinal direction shifts (north→east→south→west segments), random turns at intersections, deliberate zigzag pattern",
        "Use urban micro-environments: residential streets only, commercial districts, park connectors, bridge crossings, underpasses/tunnels (safe, well-lit)",
        "Focus on duration phasing: single continuous block, two equal blocks with short rest, three ascending blocks (20/25/30 min with rests)",
        "Vary stride characteristics: natural stride length, slightly elongated strides, deliberate shorter quicker steps, occasional side-stepping segments",
        "Emphasize transition zones: walking through thresholds (park gates, bridge entrances, neighborhood boundaries) with momentary pause/awareness",
    ],
}

TOPIC_RARITY_REQUIREMENTS: dict[tuple[TaskTopic, Rarity], str] = {
    # ========================================================================
    # PHYSICAL_ACTIVITY (TIME-BASED)
    # ========================================================================
    (
        TaskTopic.PHYSICAL_ACTIVITY,
        Rarity.COMMON,
    ): """
Generate a simple physical activity task.

Requirements:
- Metric type: TIME only
- Duration: 5 to 10 minutes
- Intensity: Light, beginner-friendly, anyone can complete
- Exercises: Only 1-2 basic exercises from the allowed list

Allowed exercises ONLY:
- Push-ups (standard, wide grip, close grip)
- Squats (bodyweight, jump squats)
- Planks (standard, side plank)
- Lunges (forward, reverse)
- Burpees
- Running
- Jumping jacks
- Sit-ups/Crunches

Strictly forbidden:
- Animal movements (bear crawls, crab walks, frog jumps, spider-man, etc.)
- Yoga, sports, dancing, martial arts
- Creative or fancy movements
- Stories or adventure descriptions

Output format:
- Rotate exercise combinations across generations, avoid always using the same 3-4 movements.
- One single task in one sentence
- Structure: exercise + duration

Examples:
- "Do push-ups for 8 minutes"
- "Perform squats for 10 minutes"
- "Alternate plank holds and rest for 7 minutes"

Generate one task following this exact style.
""",
    (
        TaskTopic.PHYSICAL_ACTIVITY,
        Rarity.UNCOMMON,
    ): """
Generate a moderate physical activity task.

Requirements:
- Metric type: TIME only
- Duration: 20 to 30 minutes
- Intensity: Moderate, some variation allowed
- Exercises: 2-3 basic exercises from the allowed list
- Structure: Simple circuit or alternating exercises
- Format: Single direct instruction, no motivation or explanations

Allowed exercises ONLY:
- Push-ups (standard, wide, close, incline, decline)
- Squats (bodyweight, jump, single-leg)
- Planks (standard, side)
- Lunges (forward, reverse, walking)
- Burpees
- Pull-ups/Chin-ups (if bar available)
- Dips (if bars available)
- Running/Jogging
- Jumping jacks
- Sit-ups/Crunches

Strictly forbidden:
- Animal movements
- Yoga, sports, dancing, martial arts
- Creative or unusual exercises
- Story elements

Output format:
- Rotate exercise combinations across generations, avoid always using the same 3-4 movements.
- One single task in one sentence
- Structure: which exercises + how to alternate + total duration

Examples:
- "Circuit: push-ups, squats, and planks for 25 minutes"
- "Alternate lunges and burpees for 28 minutes"
- "Run and do bodyweight exercises for 22 minutes"

Generate one task following this exact style.
""",
    (
        TaskTopic.PHYSICAL_ACTIVITY,
        Rarity.RARE,
    ): """
Generate a challenging physical activity task.

Requirements:
- Metric type: TIME only
- Duration: 45 to 60 minutes
- Intensity: Challenging but sustainable for trained individuals
- Exercises: 3-4 basic exercises from the allowed list
- Structure: Full workout session with multiple sets/rounds
- Format: Technical instruction, no motivation or feelings description

Allowed exercises ONLY:
- All push-up variations
- All squat variations
- All plank variations
- All lunge variations
- Burpees
- Pull-ups/Chin-ups
- Dips
- Running/Jogging
- Jumping jacks
- Sit-ups/Crunches

Strictly forbidden:
- Animal movements
- Yoga, sports, dancing, martial arts
- Non-standard or creative exercises
- Story or role-play descriptions

Output format:
- Rotate exercise combinations across generations, avoid always using the same 3-4 movements.
- One single task in one sentence
- Structure: list exercises + workout structure + total time

Examples:
- "Complete workout: push-ups, squats, lunges, and planks for 50 minutes"
- "Circuit training with 5 exercises rotated for 55 minutes"
- "Run for 20 minutes then bodyweight circuit for 30 minutes"

Generate one task following this exact style.
""",
    (
        TaskTopic.PHYSICAL_ACTIVITY,
        Rarity.EPIC,
    ): """
Generate a high-volume physical activity task.

Requirements:
- Metric type: TIME only
- Duration: 60 to 120 minutes
- Intensity: High volume with multiple rounds, rest periods included
- Exercises: 4-5+ basic exercises from the allowed list
- Structure: Serious training session with circuits/blocks/rounds
- Format: Dry instruction resembling a training plan

Allowed exercises ONLY:
- All basic exercises: push-ups, squats, pull-ups, lunges, planks, burpees, dips, running, jumping jacks, sit-ups/crunches

Strictly forbidden:
- Animal movements
- Yoga, sports, dancing, martial arts
- Creative or non-standard exercises
- Story elements

Output format:
- Rotate exercise combinations across generations, avoid always using the same 3-4 movements.
- One single task in one sentence
- Structure: describe exercises/circuit format + total duration

Examples:
- "2-hour training: multiple circuits of push-ups, squats, pull-ups, and lunges with rest between rounds"
- "90-minute session: running plus full bodyweight workout"
- "Complete 10 rounds of 5-exercise circuit over 100 minutes"

Generate one task following this exact style.

""",
    (
        TaskTopic.PHYSICAL_ACTIVITY,
        Rarity.LEGENDARY,
    ): """
Generate an extreme endurance physical activity task.

Requirements:
- Metric type: TIME only
- Duration: 3 to 5 hours
- Intensity: Very high total volume with planned rest phases and exercise rotation
- Exercises: All basic movements from the allowed list, used throughout the duration
- Structure: Marathon-style training session divided into blocks/phases
- Format: Dry technical description

Allowed exercises ONLY:
- All basic exercises: push-ups, squats, pull-ups, lunges, planks, burpees, dips, running, jumping jacks, sit-ups/crunches

Strictly forbidden:
- Animal movements
- Yoga, sports, dancing, martial arts, games
- Creative or story elements

Output format:
- Rotate exercise combinations across generations, avoid always using the same 3-4 movements.
- One single task in one sentence
- Structure: describe the multi-hour session format + approximate phases + total duration

Examples:
- "4-hour epic session: multiple circuits, long runs, max reps across all exercises with planned rest periods"
- "3.5-hour endurance challenge rotating through all basic movements"
- "5-hour training marathon with structured exercise blocks and rest intervals"

Generate one task following this exact style.

""",
    # ========================================================================
    # ADVENTURE (TIME-BASED)
    # ========================================================================
    (TaskTopic.ADVENTURE, Rarity.COMMON): """
### TOPIC CONTEXT
- Topic: ADVENTURE (Exploration & Novelty)
- Rarity: COMMON (Minimal commitment, high accessibility)
- Duration: 10 to 20 minutes
- Scope: Universal — works in city, village, dacha, anywhere

### STAT HIERARCHY (CRITICAL)
- AGI (Primary): Navigation, route adaptation, novelty
- INT (Secondary): Observation, light awareness
- STR (Minimal): This is exploration, not physical training
- Rule: AGI ≥ INT ≥ STR (Agility must be highest (70%), INT (30%). STR near 0)

### DIVERSITY ENGINE
For THIS generation, randomly select ONE focus:
1. Route: New path/street never used before
2. Observation: Notice specific details (architecture, nature, sounds)
3. Discovery: Find something never noticed in your area

### CONSTRAINTS
- NO specific landmarks (monuments, museums, shops, cafes)
- NO location-dependent requirements (must work anywhere)
- NO photography or documentation requirements
- NO paid entry locations
- Description must work in both EN and RU (no culture-specific references)

### FORBIDDEN WORDS & CONCEPTS (CRITICAL)
Do NOT use these words or concepts:
- subway, metro, underground, tunnel, station
- market, marketplace, stall, vendor, shop, mall
- park, garden, pocket park, community garden, green space
- street art, mural, graffiti, sculpture, installation, public art
- bridge, hill, overlook, viewpoint, elevated, tall building
- university, campus, school, educational institution
- museum, gallery, exhibition, monument, memorial
- industrial, factory, warehouse, zone, district
- architectural, heritage, historic, old buildings

### INTEGRATION HINTS (If combined with other topics)
- With MUSIC: Focus on rhythm of exploration, not track counting
- With SOCIAL: Shared exploration, not conversation-focused

### EXAMPLES (CORRECT — Study the Pattern)
- "Take a new route home exploring unfamiliar street" (AGI high, INT low, STR minimal)
- "Walk through neighborhood area you rarely visit noticing details" (AGI high, INT mid, STR minimal)
- "Explore nearby path you've never walked before" (AGI high, INT low, STR minimal)

### EXAMPLES (WRONG — DO NOT USE)
- "Visit the park monument" → Specific landmark
- "Go to the nearest museum" → Location-dependent
- "Walk for 15 minutes" → No novelty element (this is MOTION, not ADVENTURE)

""",

    (TaskTopic.ADVENTURE, Rarity.UNCOMMON): """
### TOPIC CONTEXT
- Topic: ADVENTURE (Exploration & Novelty)
- Rarity: UNCOMMON (Moderate commitment, requires planning)
- Duration: 30 to 60 minutes
- Scope: Universal — works in city, village, dacha, anywhere

### STAT HIERARCHY (CRITICAL)
- AGI (Primary): Route navigation, multi-path adaptation
- INT (Secondary): Active observation, light mental mapping
- STR (Minimal): Extended duration only
- Rule: AGI ≥ INT ≥ STR (Agility must be highest (70%), INT (25%). STR near 5%)

### DIVERSITY ENGINE
For THIS generation, randomly select ONE discovery type:
1. Streets: Discover 2-3 completely new streets/paths
2. Details: Notice 10+ unique elements (buildings, plants, sounds)
3. Mapping: Mentally map an unfamiliar area layout

### CONSTRAINTS
- NO specific landmarks or named locations
- NO location-dependent requirements (universal accessibility)
- NO photography requirements
- Focus on route novelty, not destination check-in
- Description must work in both EN and RU (no culture-specific references)

### FORBIDDEN WORDS & CONCEPTS (CRITICAL)
Do NOT use these words or concepts:
- subway, metro, underground, tunnel, station
- market, marketplace, stall, vendor, shop, mall
- park, garden, pocket park, community garden, green space
- street art, mural, graffiti, sculpture, installation, public art
- bridge, hill, overlook, viewpoint, elevated, tall building
- university, campus, school, educational institution
- museum, gallery, exhibition, monument, memorial
- industrial, factory, warehouse, zone, district
- architectural, heritage, historic, old buildings

### INTEGRATION HINTS (If combined with other topics)
- With MUSIC: Match exploration pace to album flow
- With SOCIAL: Explore together, share discoveries in real-time

### EXAMPLES (CORRECT — Study the Pattern)
- "Explore 3 new streets in your area taking unfamiliar turns" (AGI high, INT mid, STR low)
- "Take an unfamiliar route while noting unique details about buildings" (AGI high, INT mid, STR low)
- "Discover a neighborhood section you've never walked mapping it mentally" (AGI high, INT mid, STR low)

### EXAMPLES (WRONG — DO NOT USE)
- "Visit the town square" → Specific landmark
- "Walk to the library and back" → Destination-focused
- "Explore for 40 minutes" → No novelty element specified
""",

    (TaskTopic.ADVENTURE, Rarity.RARE): """
### TOPIC CONTEXT
- Topic: ADVENTURE (Exploration & Novelty)
- Rarity: RARE (Significant commitment, deeper exploration)
- Duration: 60 to 120 minutes
- Scope: Universal — works in city, village, dacha, anywhere

### STAT HIERARCHY (CRITICAL)
- AGI (Primary): Complex route navigation, area coverage
- INT (Secondary): Detailed observation, mental mapping
- STR (Low): Duration-based endurance
- Rule: AGI ≥ INT ≥ STR (Agility must be highest (70%), INT (25%). STR near 5%)

### DIVERSITY ENGINE
For THIS generation, randomly select ONE exploration depth:
1. Area: Explore an entire unfamiliar neighborhood section
2. Routes: Take 5+ completely new paths/streets
3. Details: Document 20+ unique observations mentally

### CONSTRAINTS
- NO specific landmarks or named locations
- NO location-dependent requirements (must work anywhere)
- NO photography or mandatory documentation
- Optional: brief notes after walk (not during)
- Description must work in both EN and RU (no culture-specific references)

### FORBIDDEN WORDS & CONCEPTS (CRITICAL)
Do NOT use these words or concepts:
- subway, metro, underground, tunnel, station
- market, marketplace, stall, vendor, shop, mall
- park, garden, pocket park, community garden, green space
- street art, mural, graffiti, sculpture, installation, public art
- bridge, hill, overlook, viewpoint, elevated, tall building
- university, campus, school, educational institution
- museum, gallery, exhibition, monument, memorial
- industrial, factory, warehouse, zone, district
- architectural, heritage, historic, old buildings

### INTEGRATION HINTS (If combined with other topics)
- With MUSIC: Full album journey matching exploration phases
- With SOCIAL: Group exploration with shared discovery goals

### EXAMPLES (CORRECT — Study the Pattern)
- "Explore an entirely new neighborhood section taking multiple paths" (AGI high, INT mid, STR low)
- "Take 5+ unfamiliar routes while observing architectural details" (AGI high, INT mid, STR low)
- "Discover multiple new paths in your area creating mental map" (AGI high, INT mid, STR low)

### EXAMPLES (WRONG — DO NOT USE)
- "Visit the historic district" → Specific area (may not exist everywhere)
- "Walk to the castle and explore" → Landmark-dependent
- "Explore for 90 minutes" → No novelty depth specified
""",

    (TaskTopic.ADVENTURE, Rarity.EPIC): """
### TOPIC CONTEXT
- Topic: ADVENTURE (Exploration & Novelty)
- Rarity: EPIC (Serious commitment, half-day exploration)
- Duration: 180 to 240 minutes (3-4 hours)
- Scope: Within your settlement (no travel required)

### STAT HIERARCHY (CRITICAL)
- AGI (Primary): Extended navigation, route planning across areas
- INT (Secondary): Comprehensive observation, optional journaling
- STR (Low): Duration endurance
- Rule: AGI ≥ INT ≥ STR (Agility must be highest (70%), INT (25%). STR near 5%)

### DIVERSITY ENGINE
For THIS generation, randomly select ONE mission type:
1. Deep Dive: Explore the far side of your city/village never visited
2. Multi-Area: Discover 10+ new streets/paths across different sections
3. Comprehensive: Full mental map of an unfamiliar neighborhood

### CONSTRAINTS
- NO specific landmarks or named locations
- Must work within ANY settlement (city, village, dacha area)
- NO travel outside your current settlement required
- Optional: brief summary notes after (not during exploration)
- Description must work in both EN and RU (no culture-specific references)

### FORBIDDEN WORDS & CONCEPTS (CRITICAL)
Do NOT use these words or concepts:
- subway, metro, underground, tunnel, station
- market, marketplace, stall, vendor, shop, mall
- park, garden, pocket park, community garden, green space
- street art, mural, graffiti, sculpture, installation, public art
- bridge, hill, overlook, viewpoint, elevated, tall building
- university, campus, school, educational institution
- museum, gallery, exhibition, monument, memorial
- industrial, factory, warehouse, zone, district
- architectural, heritage, historic, old buildings

### INTEGRATION HINTS (If combined with other topics)
- With MUSIC: Multiple albums matching exploration phases
- With CREATIVITY: Collect ideas during walk, write them down after
- With SOCIAL: Half-day group adventure with shared exploration goals

### EXAMPLES (CORRECT — Study the Pattern)
- "Explore the far side of your city you've never visited taking new routes" (AGI very high, INT mid, STR low)
- "Discover 10+ new areas across your settlement mapping connections" (AGI very high, INT mid, STR low)
- "Deep exploration of unfamiliar neighborhood sections creating full mental map" (AGI very high, INT mid, STR low)

### EXAMPLES (WRONG — DO NOT USE)
- "Travel to neighboring city" → Requires travel outside settlement
- "Visit the central park" → Specific landmark
- "Explore for 3 hours" → No mission depth specified
""",

    (TaskTopic.ADVENTURE, Rarity.LEGENDARY): """
### TOPIC CONTEXT
- Topic: ADVENTURE (Exploration & Novelty)
- Rarity: LEGENDARY (Marathon commitment, full-day expedition)
- Duration: 300+ minutes (5+ hours, exact specification required)
- Scope: May include travel to unfamiliar settlement/area

### STAT HIERARCHY (CRITICAL)
- AGI (Primary): Complex navigation, new territory adaptation
- INT (Secondary): Strategic planning, comprehensive observation
- STR (Low): Extreme duration endurance
- Rule: AGI ≥ INT ≥ STR (Agility must be highest (70%), INT (25%). STR near 5%)

### DIVERSITY ENGINE
For THIS generation, randomly select ONE expedition type:
1. New Territory: Travel to and explore an unfamiliar village/town/region
2. Multi-Phase: 3+ distinct exploration phases in different new areas
3. Comprehensive: Full-day discovery mission with detailed mental mapping

### CONSTRAINTS
- NO specific landmarks or named destinations
- Must be achievable from ANY starting point (universal accessibility)
- Travel distance should be reasonable (not requiring flights/long trips)
- Optional: comprehensive journal after expedition (not during)
- Description must work in both EN and RU (no culture-specific references)

### FORBIDDEN WORDS & CONCEPTS (CRITICAL)
Do NOT use these words or concepts:
- subway, metro, underground, tunnel, station
- market, marketplace, stall, vendor, shop, mall
- park, garden, pocket park, community garden, green space
- street art, mural, graffiti, sculpture, installation, public art
- bridge, hill, overlook, viewpoint, elevated, tall building
- university, campus, school, educational institution
- museum, gallery, exhibition, monument, memorial
- industrial, factory, warehouse, zone, district
- architectural, heritage, historic, old buildings

### INTEGRATION HINTS (If combined with other topics)
- With MUSIC: Full-day soundtrack matching expedition phases
- With SOCIAL: Full-day group adventure with shared exploration goals
- With CREATIVITY: Collect inspiration during walk, create comprehensive work after

### EXAMPLES (CORRECT — Study the Pattern)
- "Travel to and explore an unfamiliar nearby village taking multiple routes" (AGI very high, INT mid, STR low)
- "Full-day expedition: 3 new areas with different terrain creating mental map" (AGI very high, INT mid, STR low)
- "Discover a region you've never visited through full-day exploration walk" (AGI very high, INT mid, STR low)

### EXAMPLES (WRONG — DO NOT USE)
- "Fly to another country" → Unrealistic travel requirement
- "Visit the famous mountain" → Specific landmark
- "Explore for 5 hours" → No expedition scope specified
""",
    # ========================================================================
    # READING (TIME-BASED)
    # ========================================================================
    (
        TaskTopic.READING,
        Rarity.COMMON,
    ): """
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
    (
        TaskTopic.READING,
        Rarity.UNCOMMON,
    ): """
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
    (
        TaskTopic.READING,
        Rarity.RARE,
    ): """
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
    (
        TaskTopic.READING,
        Rarity.EPIC,
    ): """
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
    (
        TaskTopic.READING,
        Rarity.LEGENDARY,
    ): """
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
    (
        TaskTopic.MUSIC,
        Rarity.COMMON,
    ): """
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
    (
        TaskTopic.MUSIC,
        Rarity.UNCOMMON,
    ): """
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
    (
        TaskTopic.MUSIC,
        Rarity.RARE,
    ): """
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
    (
        TaskTopic.MUSIC,
        Rarity.EPIC,
    ): """
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
    (
        TaskTopic.MUSIC,
        Rarity.LEGENDARY,
    ): """
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
    (
        TaskTopic.DEVELOPMENT,
        Rarity.COMMON,
    ): """
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
    (
        TaskTopic.DEVELOPMENT,
        Rarity.UNCOMMON,
    ): """
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
    (
        TaskTopic.DEVELOPMENT,
        Rarity.RARE,
    ): """
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
    (
        TaskTopic.DEVELOPMENT,
        Rarity.EPIC,
    ): """
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
    (
        TaskTopic.DEVELOPMENT,
        Rarity.LEGENDARY,
    ): """
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
    (
        TaskTopic.CREATIVITY,
        Rarity.COMMON,
    ): """
**Metric:** COMPLEXITY-BASED
**Output:** 50-100 words OR 1-3 concepts
**Forms:** Flash fiction, haiku, logo sketch, short edit, UI component
**Pattern:** 15-30min quick creative burst

**Examples:**
- "Write 80-word micro-story with twist ending"
- "Sketch 2 minimalist logo concepts for [brand]"
- "Write 3-stanza poem about [theme]"
- "Design 1 Instagram story concept with layout"
- "Create 60-second video edit storyboard (3 scenes)"

**Integration:**
- +NUTRITION: "Design 1 creative plate presentation sketch"
- +BRAIN: "Solve 1 lateral thinking puzzle, write 80-word creative solution"
""",
    (
        TaskTopic.CREATIVITY,
        Rarity.UNCOMMON,
    ): """
**Metric:** COMPLEXITY-BASED
**Output:** 300-500 words OR 5-10 concepts
**Forms:** Short story, character design set, poem series, moodboard, montage plan
**Pattern:** 1-2hr focused creative session

**Examples:**
- "Write 400-word sci-fi story with dialogue"
- "Design 7 character concept sketches with notes"
- "Create 5-poem series exploring [emotion]"
- "Build moodboard with 8 visual concepts + captions"
- "Plan 3-minute video montage (10 scene breakdown)"
- "Write 500-word screenplay scene"

**Integration:**
- +NUTRITION: "Develop 3 original recipes with creative plating (400 words)"
- +BRAIN: "Complete 5 creative thinking exercises, document process (500 words)"
""",
    (
        TaskTopic.CREATIVITY,
        Rarity.RARE,
    ): """
**Metric:** COMPLEXITY-BASED
**Output:** 1000-1200 words OR 15-20 concepts
**Forms:** Complete story, design system, illustrated poem, full edit plan, concept art series
**Pattern:** 2-4hr deep creative work

**Examples:**
- "Write 1200-word complete short story with arc"
- "Design 15-component UI kit with style guide"
- "Create illustrated poem series (5 poems + 5 sketches)"
- "Develop 20-shot video montage with timing notes"
- "Write 1000-word one-act play"
- "Design 18 concept art pieces for game environment"

**Integration:**
- +NUTRITION: "Create 8 recipe concepts with ingredient exploration + plating designs"
- +BRAIN: "Write 1200-word creative analysis solving complex problem from multiple perspectives"
""",
    (
        TaskTopic.CREATIVITY,
        Rarity.EPIC,
    ): """
**Metric:** COMPLEXITY-BASED
**Output:** 2000-2500 words OR 30-50 concepts
**Forms:** Novella chapter, portfolio project, anthology, full brand identity, complete video project
**Pattern:** 4-6hr major creative undertaking

**Examples:**
- "Write 2200-word story with multiple perspectives"
- "Create complete brand identity (40 elements: logos, colors, typography, mockups)"
- "Write 10-poem anthology with illustrations (2500 words total)"
- "Design 35-scene storyboard for 5-minute short film"
- "Develop 45 concept art pieces with descriptions"
- "Write 2000-word screenplay (complete scene sequence)"

**Integration:**
- +NUTRITION: "Develop complete themed menu: 15 recipes with creative presentations + cookbook design (2000 words)"
- +BRAIN: "Create 30 original creative thinking puzzles with illustrated solutions"
""",
    (
        TaskTopic.CREATIVITY,
        Rarity.LEGENDARY,
    ): """
**Metric:** COMPLEXITY-BASED
**Output:** 5000+ words OR 80-100 concepts
**Forms:** Novella, comprehensive portfolio, complete creative project, full production plan
**Pattern:** 8-12hr creative marathon

**Examples:**
- "Write 5000-word novella chapter with subplots"
- "Create 100-piece comprehensive design portfolio"
- "Write 20-poem illustrated collection (5000 words + art)"
- "Develop complete video production: script, storyboard, shot list (80+ elements)"
- "Design full game world: 90 concept art pieces + lore descriptions"
- "Write complete short screenplay (5000 words, multiple acts)"

**Integration:**
- +NUTRITION: "Create full cookbook: 40 original recipes with food photography concepts, styling notes, nutrition design (5000 words)"
- +BRAIN: "Develop comprehensive creative thinking course: 50 exercises with theory, examples, solutions (5000 words)"
""",
    # ========================================================================
    # SOCIAL_SKILLS (COMPLEXITY-BASED)
    # ========================================================================
    (
        TaskTopic.SOCIAL_SKILLS,
        Rarity.COMMON,
    ): """
    **Metric Type:** COMPLEXITY-BASED (INTERACTION COUNT)
    **Amount:** 1 brief interaction
    **Focus:** Simple, low-pressure communication
    **Pattern:** Single short offline situation

    **Types:**
      - STRANGERS: 1 short contact with stranger
      - FRIENDS: 1 short contact with acquaintance/friend

    **CRITICAL:** Face-to-face ONLY, NO online/digital

    **STRANGERS Examples:**
    - "Ask 1 stranger for directions or opinion"
    - "Give 1 genuine compliment to stranger"
    - "Ask 1 open question to barista/cashier"

    **FRIENDS Examples:**
    - "Approach 1 acquaintance for brief chat about day"
    - "Do 1 quick check-in with friend: ask how they are and listen actively"
    - "Share 1 small idea/news with friend"

    **Integration (FRIENDS):**
    - +READING: "Read short article, summarize to friend in 2-3 sentences"
    - +MUSIC: "Listen to 1 track, briefly discuss with friend"
    """,
    (
        TaskTopic.SOCIAL_SKILLS,
        Rarity.UNCOMMON,
    ): """
    **Metric Type:** COMPLEXITY-BASED (INTERACTION COUNT)
    **Amount:** 2-3 interactions OR 1 paired activity
    **Focus:** More meaningful communication
    **Pattern:** Multiple short OR single paired activity

    **CRITICAL:** Face-to-face ONLY

    **Types:**
      - STRANGERS: 2-3 short contacts with different people
      - FRIENDS: 1 paired activity or 2 small conversations

    **STRANGERS Examples:**
    - "Talk to 2-3 people in line/store (1-2 questions each)"
    - "Ask opinion about choice (clothes, tech, cafe) from 2 strangers"
    - "Exchange few phrases with 3 people (cashier, barista, receptionist)"

    **FRIENDS Examples:**
    - "Take 30-45min walk with friend discussing week's events"
    - "Cook simple dish together with friend, discuss results"
    - "Have 2 small meaningful conversations with friends (10-15min each)"

    **Integration (FRIENDS):**
    - +NUTRITION: "Cook 1 dish with friend, discuss recipe improvements"
    - +READING: "Read article, meet friend for 15-20min discussion"
    - +BRAIN: "Solve 2-3 puzzles together, discuss solution strategies"
    """,
    (
        TaskTopic.SOCIAL_SKILLS,
        Rarity.RARE,
    ): """
    **Metric Type:** COMPLEXITY-BASED (INTERACTION COUNT)
    **Amount:** 1 deep conversation OR 3-5 interactions
    **Focus:** Depth or series of meaningful contacts
    **Pattern:** Quality over quantity

    **CRITICAL:** Face-to-face ONLY

    **Types:**
      - STRANGERS: purposeful communication at event/space
      - FRIENDS: deep conversation or joint learning/discussion

    **STRANGERS Examples:**
    - "At event, have 3-5 meaningful conversations (beyond small talk)"
    - "Meet 3 new people, ask each about their interest/project"
    - "Participate in offline club/meetup, talk with at least 4 people"

    **FRIENDS Examples:**
    - "Have 1 deep conversation with friend about values/goals/philosophy"
    - "Teach friend 1 skill through conversation and demonstration"
    - "Conduct 1 strategic discussion with friend about joint project plans"

    **Integration (FRIENDS):**
    - +READING: "Read article, then have 1 deep discussion with friend about ideas"
    - +MUSIC: "Listen to album together, have 1 analytical discussion about themes/arrangements"
    - +NUTRITION: "Cook complex dish together while having deep conversation about food/health"
    - +BRAIN: "Complete 5-7 thinking tasks with friend, discuss approaches and mistakes"
    """,
    (
        TaskTopic.SOCIAL_SKILLS,
        Rarity.EPIC,
    ): """
    **Metric Type:** COMPLEXITY-BASED (EVENT SCALE)
    **Amount:** 1 small presentation / mini-group
    **Focus:** Group dynamics and mini-leadership
    **Pattern:** Work with 4-8 people

    **CRITICAL:** Face-to-face ONLY

    **Types:**
      - GROUP FRIENDS: offline mini-event with close friends/acquaintances
      - MIXED/STRANGERS: small open group

    **Examples (GROUP FRIENDS / MIXED):**
    - "Prepare and deliver 15-30min mini-presentation for 4-7 people"
    - "Organize and facilitate offline topic discussion in group of 5-6"
    - "Lead small workshop for 5-8 people (explain skill, answer questions)"

    **Integration:**
    - +READING: "Prepare book/article analysis, present to 4-6 people with discussion"
    - +BRAIN: "Run offline brainstorming or thinking tasks session for 4-6 participants"
    - +CREATIVITY: "Organize mini-creative workshop (sketches, ideas, stories) for 4-6 people"
    """,
    (
        TaskTopic.SOCIAL_SKILLS,
        Rarity.LEGENDARY,
    ): """
    **Metric Type:** COMPLEXITY-BASED (EVENT SCALE)
    **Amount:** Organize and host full offline event for 10-15 people
    **Focus:** Full cycle: planning, inviting, hosting, interaction
    **Pattern:** Large live gathering

    **CRITICAL:** Face-to-face ONLY

    **Types:**
      - FRIENDS/NETWORK: event with core of acquaintances plus new people
      - MIXED: club, meetup, mini-conference

    **Examples:**
    - "Organize and host offline meetup/party for 10-15 people with program"
    - "Plan, invite, and run mini-meetup on topic for 10-15 participants"
    - "Create event with intro, main part, and free networking (10+ people)"

    **Integration:**
    - +NUTRITION: "Organize offline dinner/feast for 10-15: plan menu, cook/coordinate food, host"
    - +READING: "Organize book club/themed meeting for 10-15 people with structured discussion"
    - +CREATIVITY: "Host creative evening/showcase for 10-15: mini-performances/demos and discussion"
    - +BRAIN: "Organize puzzle/quiz/brainstorming evening for 10-15 with multiple rounds"
    """,
    # ========================================================================
    # NUTRITION (COMPLEXITY-BASED)
    # ========================================================================
    (
        TaskTopic.NUTRITION,
        Rarity.COMMON,
    ): """
    **Metric Type:** COMPLEXITY-BASED (MEAL/ITEM COUNT)
    **Amount:** 1 simple item
    **Focus:** Basic eating/preparation
    **Two types:**
      - TYPE 1 (CONSUME): Eat healthy item, drink water
      - TYPE 2 (COOK): Simple dish (eggs, sandwich, salad)
    **Pattern:** Single basic action

    **Examples:**
    - "Eat 1 apple and drink 2 glasses of water"
    - "Cook scrambled eggs with vegetables"
    - "Prepare Greek salad with feta cheese"
    - "Make avocado toast with whole grain bread"
    - "Cook oatmeal with berries and nuts"
    """,
    (
        TaskTopic.NUTRITION,
        Rarity.UNCOMMON,
    ): """
    **Metric Type:** COMPLEXITY-BASED (MEAL/DISH COUNT)
    **Amount:** 1-2 moderate dishes OR 2-3 servings
    **Focus:** Moderate cooking or consuming
    **Two types:**
      - TYPE 1 (CONSUME): Eat 2-3 balanced meals
      - TYPE 2 (COOK): Cook 1-2 medium dishes (30-min meals)
    **Pattern:** Moderate effort meal(s)

    **Examples:**
    - "Cook pasta carbonara with peas"
    - "Prepare chicken stir-fry with vegetables and rice"
    - "Cook quinoa bowl with roasted vegetables"
    - "Make lentil soup with carrots and celery"
    - "Prepare salmon with steamed broccoli"

    **Integration:**
    - With CREATIVITY: "Cook 1 unusual recipe (e.g., shakshuka, bibimbap) and photograph process (5 photos)"
    """,
    (
        TaskTopic.NUTRITION,
        Rarity.RARE,
    ): """
    **Metric Type:** COMPLEXITY-BASED (DISH COUNT)
    **Amount:** 1 complex dish from scratch OR 3 simpler dishes
    **Focus:** Challenging cooking or substantial meal prep
    **Type:** COOK only (complex preparation)
    **Pattern:** Serious cooking session
    
    **Examples:**
    - "Cook beef bourguignon from scratch (60+ min)"
    - "Prepare authentic ramen with bone broth and chashu pork"
    - "Cook Thai green curry with homemade curry paste"
    - "Make Moroccan lamb tagine with preserved lemons"
    - "Prepare Korean bibimbap with 5 vegetable toppings"
    - "Cook Indian butter chicken with naan bread from scratch"
    - "Meal prep: chicken teriyaki, roasted vegetables, brown rice"
    
    **Integration:**
    - With CREATIVITY: "Cook 1 unusual complex recipe (e.g., Georgian khachapuri, Vietnamese pho, Japanese tonkatsu) and document process (15 photos/descriptions)"
    """,
    (
        TaskTopic.NUTRITION,
        Rarity.EPIC,
    ): """
    **Metric Type:** COMPLEXITY-BASED (MEAL COUNT)
    **Amount:** 5-7 meals prepped OR 1 feast for 6-8 people
    **Focus:** Major meal prep or event cooking
    **Type:** COOK - extensive preparation
    **Pattern:** Multi-hour cooking session

    **Examples:**
    - "Meal prep 5 meals: grilled chicken, baked salmon, lentil curry, quinoa salads, roasted vegetables"
    - "Cook feast: roast duck, potato gratin, ratatouille, Caesar salad"
    - "Prepare 6 dishes: turkey meatballs, veggie lasagna, chicken soup, 2 salads, baked cod"
    - "Cook dinner party: beef Wellington, truffle mashed potatoes, glazed carrots, spinach salad"

    **Integration:**
    - With CREATIVITY: "Cook 2 unusual recipes (e.g., Peruvian ceviche, Korean bulgogi) with artistic presentation (30 design photos)"
    """,
    (
        TaskTopic.NUTRITION,
        Rarity.LEGENDARY,
    ): """
    **Metric Type:** COMPLEXITY-BASED (MEAL COUNT)
    **Amount:** 15-20 meals prepped OR feast for 10+ people
    **Focus:** Epic meal prep marathon or major event
    **Type:** COOK - marathon session
    **Pattern:** All-day cooking

    **Examples:**
    - "Meal prep 18 meals: 6 chicken breast dishes, 6 fish dishes, 6 vegetarian dishes with sides"
    - "Cook wedding feast for 12: roast lamb, baked salmon, 3 salads, grilled vegetables, potato dishes"
    - "Prepare 20 meals across 5 recipes: teriyaki chicken, beef stew, fish tacos, lentil curry, veggie stir-fry"
    - "Cook banquet for 15: prime rib roast, lobster tails, truffle risotto, Caesar salad, roasted Brussels sprouts"

    **Integration:**
    - With CREATIVITY: "Cook 3 unusual recipes (e.g., Ethiopian doro wat, Vietnamese pho, Japanese katsu curry) with comprehensive photo documentation (80 photos)"
    """,
    # ========================================================================
    # PRODUCTIVITY (COMPLEXITY-BASED)
    # ========================================================================
    (
        TaskTopic.PRODUCTIVITY,
        Rarity.COMMON,
    ): """
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
    (
        TaskTopic.PRODUCTIVITY,
        Rarity.UNCOMMON,
    ): """
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
    (
        TaskTopic.PRODUCTIVITY,
        Rarity.RARE,
    ): """
**Metric Type:** COMPLEXITY-BASED (TASK COUNT)
**Amount:** 8-10 tasks, full day time-blocked
**Focus:** Comprehensive daily planning
**Forms:** Full day schedule, detailed time-blocking
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
    (
        TaskTopic.PRODUCTIVITY,
        Rarity.EPIC,
    ): """
**Metric Type:** COMPLEXITY-BASED (TASK COUNT)
**Amount:** 15 tasks organized, full week planned
**Focus:** Weekly comprehensive planning
**Forms:** Week schedule, multiple systems, detailed tracking
**Pattern:** Extended planning session

**Examples:**
- "Plan entire week with 15 tasks, priorities, and time blocks"
- "Create comprehensive system for 15 ongoing tasks"
- "Organize week with 15 tasks using multiple frameworks"

**Integration:**
- With PHYSICAL: "Plan 2-week training program with 15 sessions"
- With DEVELOPMENT: "Organize learning path with 15 study sessions"
- With CREATIVITY: "Plan creative project timeline with 15 milestones"
- META: Multi-day planning across topics
""",
    (
        TaskTopic.PRODUCTIVITY,
        Rarity.LEGENDARY,
    ): """
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
    (
        TaskTopic.BRAIN,
        Rarity.COMMON,
    ): """
**Metric Type:** COMPLEXITY-BASED (PUZZLE COUNT)
**Amount:** 1-2 easy puzzles/challenges
**Focus:** Simple mental exercise, light brain warm-up
**Pattern:** One specific short task

**ALLOWED puzzle types (ROTATE between them):**
1. Easy sudoku (beginner level)
2. Simple crossword puzzles
3. Basic chess tactics puzzles (1–2 move solutions)
4. Simple logic riddles
5. Basic memory exercises (short sequences, simple item lists)
6. Basic arithmetic problems

**CRITICAL RULES:**
- You MUST choose ONE specific puzzle type from the list above.
- ROTATE types across generations — avoid repeating the same type consecutively.
- You MUST specify the EXACT type and difficulty.
- DO NOT use words like "such as", "including", "like", "for example".
- DO NOT describe puzzles in vague terms ("brain teasers", "mental exercises" without type).

**Diversity instruction:** If you recently generated sudoku, choose a DIFFERENT type (crosswords, chess, logic riddles, etc.)

**Examples (CORRECT):**
- "Solve 2 easy sudoku puzzles"
- "Complete 1 simple crossword puzzle"
- "Solve 2 beginner chess tactics puzzles"
- "Do 1 memory exercise: memorize and recall a list of 10 items"

**Examples (WRONG — DO NOT USE):**
- "Solve 2 easy puzzles such as sudoku or crosswords"
- "Complete some easy brain teasers"

**Integration:**
- With ADVENTURE: "Walk for 15 min while solving 2 basic logic riddles"
- With PHYSICAL: Limited (both need focus)
""",
    (
        TaskTopic.BRAIN,
        Rarity.UNCOMMON,
    ): """
**Metric Type:** COMPLEXITY-BASED (PUZZLE COUNT)
**Amount:** Exactly 5 medium puzzles/problems
**Focus:** Moderate mental challenge, focused brain workout
**Pattern:** Set of 5 tasks of the same type and difficulty

**ALLOWED puzzle types (PRIORITIZE variety):**
1. Medium crossword puzzles
2. Medium chess tactics puzzles (2–4 move solutions)
3. Logic grid puzzles (medium difficulty)
4. Medium kakuro
5. Memory sequences (15–20 items)
6. Medium math problems (algebra, basic geometry)
7. Medium sudoku (use LAST if others were used recently)

**CRITICAL RULES:**
- You MUST choose ONE specific puzzle type from the list above.
- ROTATE puzzle types to ensure variety across generations.
- Avoid defaulting to sudoku unless other types were used in recent tasks.
- You MUST specify EXACTLY 5 puzzles.
- DO NOT use "such as", "including", "like", "or" lists of options.
- DO NOT mix easy and hard puzzles in one task.

**Diversity instruction:** Prioritize puzzle types NOT used in the last 3 generations. Chess, crosswords, and logic grids should appear as often as sudoku.

**Examples (CORRECT):**
- "Solve 5 medium chess tactics puzzles"
- "Complete 5 medium crossword puzzles"
- "Solve 5 logic grid puzzles"
- "Complete 5 medium kakuro puzzles"
- "Do 5 memory exercises, each with a sequence of 15–20 items"

**Examples (WRONG — DO NOT USE):**
- "Solve 5 puzzles such as sudoku, chess tactics, or logic grids"
- "Solve 5 medium brain teasers"

**Integration:**
- With ADVENTURE: "Walk for 30 min while solving 5 medium mental arithmetic problems"
- With MUSIC: "Solve 5 medium crossword puzzles while listening to a calm ambient album"
""",
    (
        TaskTopic.BRAIN,
        Rarity.RARE,
    ): """
**Metric Type:** COMPLEXITY-BASED (PUZZLE COUNT)
**Amount:** Exactly 15 hard puzzles/challenges
**Focus:** Serious mental workout, high concentration
**Pattern:** Extended brain training session

**ALLOWED puzzle types (BALANCED rotation):**
1. Advanced chess tactics puzzles (4+ move solutions)
2. Difficult crossword puzzles
3. Complex logic puzzles
4. Hard kakuro
5. Advanced math problems
6. Intro cryptography puzzles
7. Advanced memory challenges (complex sequences and patterns)
8. Hard/expert sudoku (ROTATE with others)

**CRITICAL RULES:**
- You MUST be SPECIFIC.
- Option A: choose ONE type and use all 15 on that type.
- Option B: use a MIX of 2-3 types, but you MUST specify exact counts for each type, and the total MUST be 15.
- ROTATE primary puzzle type across generations to avoid repetition.
- DO NOT use "such as", "including", "like", "various hard puzzles".

**Diversity instruction:** Balance puzzle types. If sudoku was used recently, prefer chess, cryptography, or math. Mix types when appropriate (e.g., 8 chess + 7 logic grids).

**Examples (CORRECT):**
- "Solve 15 advanced chess tactics puzzles"
- "Complete 15 hard cryptography challenges"
- "Solve 15 puzzles: 8 advanced chess tactics, 7 hard logic grids"
- "Complete 15 puzzles: 5 expert sudoku, 5 hard kakuro, 5 complex logic puzzles"

**Examples (WRONG — DO NOT USE):**
- "Solve 15 hard puzzles including sudoku and chess"
- "Complete 15 challenging brain exercises"

**Integration:**
- With MUSIC: "Solve 15 hard logic puzzles while a calm ambient album plays in the background"
- With CONTENT: "Solve 10 advanced chess puzzles and 5 hard logic problems based on math or music patterns"
""",
    (
        TaskTopic.BRAIN,
        Rarity.EPIC,
    ): """
**Metric Type:** COMPLEXITY-BASED (PROBLEM COUNT)
**Amount:** Exactly 30 intensive problems/challenges
**Focus:** Major mental marathon, sustained high effort
**Pattern:** Long brain workout session with variety

**ALLOWED problem types (MIX for endurance):**
1. Advanced chess puzzles (high-level tactics and combinations)
2. Complex logic puzzles
3. Expert kakuro
4. Advanced math problems (algebra, geometry, calculus)
5. Cryptography challenges
6. Hard crosswords
7. Complex memory tasks (long sequences, multi-step recall)
8. Expert sudoku (balance with other types)

**CRITICAL RULES:**
- You MUST be SPECIFIC.
- Option A: one type only — all 30 problems of the same type (rare, use for specialization).
- Option B (PREFERRED): mixed types — you MUST give exact numbers for each type, total = 30.
- Use AT LEAST 2 different types for variety and mental endurance.
- DO NOT use "including", "such as", "various", "across multiple categories" without specific numbers.

**Diversity instruction:** For 30-problem marathons, MIX types to maintain engagement (e.g., 15 chess + 15 logic, or 10 math + 10 cryptography + 10 chess).

**Examples (CORRECT):**
- "Solve 30 problems: 15 advanced chess tactics, 15 complex logic puzzles"
- "Complete 30 challenges: 10 expert sudoku, 10 hard cryptography, 10 advanced math problems"
- "Solve 30 puzzles: 12 advanced chess tactics, 12 complex logic grids, 6 hard kakuro"
- "Complete 30 advanced math problems" (only if specializing)

**Examples (WRONG — DO NOT USE):**
- "Complete 30 intensive problems including chess, sudoku, and logic"
- "Solve 30 various expert puzzles"

**Integration:**
- Limited (requires sustained focus)
- Content-based: "Solve 30 problems: 15 math problems on musical patterns, 15 logic puzzles on algorithmic thinking"
""",
    (
        TaskTopic.BRAIN,
        Rarity.LEGENDARY,
    ): """
**Metric Type:** COMPLEXITY-BASED (CHALLENGE COUNT)
**Amount:** 80-100 brain challenges
**Focus:** Epic mental endurance, all-day brain training
**Pattern:** Large mixed set with mandatory diversity

**ALLOWED challenge types (MUST mix):**
1. Chess puzzles (advanced/master level)
2. Logic puzzles (hard)
3. Kakuro (hard/expert)
4. Advanced math problems
5. Cryptography and code-breaking puzzles
6. Advanced memory challenges
7. Crosswords (difficult)
8. Sudoku (hard/expert) — balance with other types

**CRITICAL RULES:**
- You MUST provide a SPECIFIC breakdown by type.
- You MUST use AT LEAST 4 different puzzle types.
- You MUST specify exact counts for each type.
- The total MUST be between 80 and 100.
- BALANCE types evenly (no single type should exceed 40% of total).
- DO NOT use vague phrases like "across multiple categories" without numbers.

**Diversity instruction:** LEGENDARY tasks require MAXIMUM variety for sustained engagement. Distribute challenges across at least 4 types (e.g., 25 chess, 25 logic, 25 math, 25 cryptography).

**Examples (CORRECT):**
- "Solve 100 challenges: 25 advanced chess puzzles, 25 complex logic grids, 25 hard cryptography, 25 advanced math problems"
- "Complete 90 puzzles: 30 advanced chess tactics, 25 hard logic puzzles, 20 expert kakuro, 15 cryptography challenges"
- "Solve 80 problems: 20 expert sudoku, 20 advanced chess, 20 hard logic grids, 20 complex memory tasks"

**Examples (WRONG — DO NOT USE):**
- "Solve 80 brain challenges across multiple categories"
- "Complete 100 puzzles including sudoku, chess, logic, memory, and math"
- "Solve 100 challenges: 60 sudoku, 20 chess, 20 logic" (imbalanced)

**Integration:**
- Minimal (requires deep sustained focus)
- Content-based only: "Solve 100 challenges: 30 math problems on music theory, 30 logic puzzles on algorithms, 20 chess tactics, 20 cryptography"
""",
    # ========================================================================
    # CYBERSPORT (COMPLEXITY-BASED)
    # ========================================================================
    (
        TaskTopic.CYBERSPORT,
        Rarity.COMMON,
    ): """
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
    (
        TaskTopic.CYBERSPORT,
        Rarity.UNCOMMON,
    ): """
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
    (
        TaskTopic.CYBERSPORT,
        Rarity.RARE,
    ): """
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
    (
        TaskTopic.CYBERSPORT,
        Rarity.EPIC,
    ): """
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
    (
        TaskTopic.CYBERSPORT,
        Rarity.LEGENDARY,
    ): """
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
    (
        TaskTopic.LANGUAGE_LEARNING,
        Rarity.COMMON,
    ): """
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
    (
        TaskTopic.LANGUAGE_LEARNING,
        Rarity.UNCOMMON,
    ): """
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
    (
        TaskTopic.LANGUAGE_LEARNING,
        Rarity.RARE,
    ): """
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
    (
        TaskTopic.LANGUAGE_LEARNING,
        Rarity.EPIC,
    ): """
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
    (
        TaskTopic.LANGUAGE_LEARNING,
        Rarity.LEGENDARY,
    ): """
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
    # ========================================================================
    # MOTION (TIME-BASED LOCOMOTION)
    # ========================================================================
    (TaskTopic.MOTION, Rarity.COMMON): """

    ### PARAMETERS
    - **Rarity:** COMMON (Minimal effort, high accessibility)
    - **Duration:** 5 to 10 minutes (Exact integer)
    - **Intensity:** Very Light (Zone 1, conversational breathing)
    - **Core Action:** Walking or Strolling
    - AGI is the PRIMARY stat for MOTION (AGI ≥ STR ≥ INT).
    - INT must be 0 or 1 only (physical task, not mental).

    ### DIVERSITY ENGINE (CRITICAL)
    For THIS generation, randomly select ONE focus dimension to include in the task:
    1. **Location:** (e.g., indoors, around block, near home)
    2. **Purpose:** (e.g., to clear mind, to relax, for fresh air)
    3. **Condition:** (e.g., while listening to music, at sunrise, after meal)
    Do NOT copy examples exactly. Use them as a style reference.

    ### CONSTRAINTS
    - Use TIME only (minutes). No distance (km/miles).
    - Keep language encouraging and simple.
    - Single activity type only (no exercise combinations).
    - Pace must remain leisurely/relaxed.

    ### OUTPUT FORMAT
    Return ONLY the task string: "{Action} {Focus} for {Duration} minutes"

    ### EXAMPLES (CORRECT — Note Structural Variety)
    - "Walk leisurely around your block for 8 minutes"
    - "Take a slow 7-minute stroll to clear your mind"
    - "Walk at a relaxed pace indoors while listening to music for 10 minutes"
    - "Gentle walking near your home for 6 minutes"

    ### EXAMPLES (WRONG — DO NOT USE)
    - "Move around for 10 minutes" (Too vague)
    - "Walk and do squats" (Mixes activity types)
    - "Explore mysterious forest for 10 minutes" (Story-focused, not duration-focused)
    """,

    (TaskTopic.MOTION, Rarity.UNCOMMON): """

    ### PARAMETERS
    - **Rarity:** UNCOMMON (Moderate effort, light cardio)
    - **Duration:** 20 to 30 minutes (Exact integer)
    - **Intensity:** Light Cardio (Zone 2, purposeful pace)
    - **Core Action:** Brisk Walking or Light Walk-Jog
    - AGI is the PRIMARY stat for MOTION (AGI ≥ STR ≥ INT).
    - INT must be 0 or 1 only (physical task, not mental).

    ### DIVERSITY ENGINE (CRITICAL)
    For THIS generation, randomly select ONE pacing style:
    1. **Steady:** Consistent brisk pace throughout
    2. **Intervals:** Simple alternation (e.g., 3 min walk / 2 min jog)
    3. **Terrain:** Include gentle hills or varied surfaces
    4. **Purposeful:** "Power walking" with clear intent
    Do NOT copy examples exactly. Use them as a style reference.

    ### CONSTRAINTS
    - Use TIME only. No distance metrics.
    - Specify pace clearly (e.g., "brisk", "purposeful", "light jog").
    - Prioritize brisk walking over running for accessibility.
    - If intervals used, specify simple structure.

    ### OUTPUT FORMAT
    Return ONLY the task string: "{Action} at {Pace} for {Duration} minutes ({Style})"

    ### EXAMPLES (CORRECT — Note Structural Variety)
    - "Brisk walk at a purposeful pace for 25 minutes (Steady)"
    - "Alternate 3 min walking and 2 min light jogging for 28 minutes (Intervals)"
    - "Power walk on a route with gentle hills for 22 minutes (Terrain)"
    - "Sustained brisk walking for 30 minutes to build endurance (Purposeful)"

    ### EXAMPLES (WRONG — DO NOT USE)
    - "Jog for 25 minutes" (Too intense without qualification)
    - "Move at moderate intensity for 30 minutes" (Vague pacing)
    - "Walk 3 km" (Distance-based metric forbidden)
    """,

    (TaskTopic.MOTION, Rarity.RARE): """

    ### PARAMETERS
    - **Rarity:** RARE (Significant effort, endurance focus)
    - **Duration:** 45 to 60 minutes (Exact integer)
    - **Intensity:** Moderate Cardio (Zone 3, sustainable jogging pace)
    - **Core Action:** Jogging, Extended Brisk Walking, or Structured Intervals
    - AGI is the PRIMARY stat for MOTION (AGI ≥ STR ≥ INT).
    - INT must be 0 or 1 only (physical task, not mental).

    ### DIVERSITY ENGINE (CRITICAL)
    For THIS generation, randomly select ONE engagement hook:
    1. **Flow State:** Focus on rhythm, breathing, and consistency
    2. **Exploration:** New route, trail, or natural environment
    3. **Structure:** Defined work/rest or jog/walk ratios
    4. **Resilience:** Pushing through mild fatigue comfortably
    Do NOT copy examples exactly. Use them as a style reference.

    ### CONSTRAINTS
    - Use TIME only. No distance metrics.
    - Must specify structure if intervals are used (e.g., "5 min jog / 3 min walk").
    - Pace must be sustainable (conversational jogging).
    - Brief rest periods allowed but not counted as primary activity.

    ### OUTPUT FORMAT
    Return ONLY the task string: "{Action} for {Duration} minutes ({Hook})"

    ### EXAMPLES (CORRECT — Note Structural Variety)
    - "Steady jogging at a conversational pace for 50 minutes (Flow State)"
    - "Trail walking on moderate terrain for 55 minutes (Exploration)"
    - "Cycle of 5 min jog / 3 min walk for 45 minutes total (Structure)"
    - "Extended brisk walk continuously for 60 minutes to build stamina (Resilience)"

    ### EXAMPLES (WRONG — DO NOT USE)
    - "Run for an hour" (Vague pace — specify "jog" vs "run")
    - "Walk 5 km on trails" (Distance-based metric forbidden)
    - "Jog with exercise stops every 10 min" (Mixes activity types without context)
    """,

    (TaskTopic.MOTION, Rarity.EPIC): """

    ### PARAMETERS
    - **Rarity:** EPIC (High effort, planning required)
    - **Duration:** 60 to 120 minutes (Exact integer or half-hours)
    - **Intensity:** Moderate to High Sustained (Zone 3-4)
    - **Core Action:** Long-distance Jogging, Fast Walking, or Mixed Phases
    - AGI is the PRIMARY stat for MOTION (AGI ≥ STR ≥ INT).
    - INT must be 0 or 1 only (physical task, not mental).

    ### DIVERSITY ENGINE (CRITICAL)
    For THIS generation, randomly select ONE strategic element:
    1. **Phased:** Split session into distinct blocks (e.g., Urban + Trail)
    2. **Pacing:** Negative split (start slow, finish strong)
    3. **Environment:** Mixed terrain challenge
    4. **Mental:** Focus on discipline and consistency over time
    Do NOT copy examples exactly. Use them as a style reference.

    ### CONSTRAINTS
    - Use TIME only. No distance metrics.
    - Describe pacing strategy briefly in the task.
    - Hydration breaks allowed but not counted as rest time.
    - Total locomotion time must be 60-120 min.

    ### OUTPUT FORMAT
    Return ONLY the task string: "{Action} with {Strategy} for {Duration} minutes ({Element})"

    ### EXAMPLES (CORRECT — Note Structural Variety)
    - "Sustainable jogging with negative split pacing for 90 minutes (Pacing)"
    - "Mixed terrain: 40 min road + 40 min trail for 80 minutes total (Phased)"
    - "Fast walking continuously with focused discipline for 75 minutes (Mental)"
    - "Alternate 12 min jogging and 5 min walking for 100 minutes total (Environment)"

    ### EXAMPLES (WRONG — DO NOT USE)
    - "Run for 2 hours" (Vague — specify sustainable/jogging pace)
    - "Cover as much distance as possible in 90 minutes" (Goal-oriented, not duration-focused)
    - "Jog with random stops for exercises" (Unstructured activity mixing)
    """,

    (TaskTopic.MOTION, Rarity.LEGENDARY): """

    ### PARAMETERS
    - **Rarity:** LEGENDARY (Extreme effort, event-level achievement)
    - **Duration:** 3 to 5 hours (Exact hours/minutes, e.g., "3 hours 20 minutes")
    - **Intensity:** Ultra-Endurance (Sustainable over hours, Zone 2-3)
    - **Core Action:** LSD Jogging, Ultra-Walking, or Multi-Phase Sessions
    - AGI is the PRIMARY stat for MOTION (AGI ≥ STR ≥ INT).
    - INT must be 0 or 1 only (physical task, not mental).
    
    ### DIVERSITY ENGINE (CRITICAL)
    For THIS generation, randomly select ONE narrative theme:
    1. **The Journey:** Point A to Point B exploration
    2. **The Test:** Pure endurance and mental grit
    3. **The Ritual:** Meditative long movement
    4. **The Marathoner:** Structured race-pace simulation
    Do NOT copy examples exactly. Use them as a style reference.

    ### CONSTRAINTS
    - Use TIME only (e.g., "3 hours 15 minutes", "4.5 hours").
    - Must include planned micro-breaks or phase changes in description.
    - Tone should be inspiring and serious (achievement-focused).
    - Total duration must be 3-5 hours (planned rests included in total).

    ### OUTPUT FORMAT
    Return ONLY the task string: "{Theme}: {Action} for {Duration} ({Details})"

    ### EXAMPLES (CORRECT — Note Structural Variety)
    - "The Journey: Mixed terrain walking/jogging for 4 hours (Urban to Nature)"
    - "The Test: LSD jogging at sustainable pace for 3 hours 30 minutes (Mental Grit)"
    - "The Ritual: Mindful ultra-walking with brief hydration stops for 5 hours (Meditative)"
    - "The Marathoner: Three 70-minute blocks with 10-min rests for 4 hours total (Structured)"

    ### EXAMPLES (WRONG — DO NOT USE)
    - "Walk all day" (No exact duration specified)
    - "Run 5 hours straight without stopping" (Unrealistic, ignores necessary breaks)
    - "Cover maximum distance in 4 hours" (Distance/goal-focused, not pure locomotion)
    """
}


def get_requirements(topic: TaskTopic, rarity: Rarity) -> str:
    key = (topic, rarity)
    if key not in TOPIC_RARITY_REQUIREMENTS:
        raise ValueError(
            f"No requirements found for topic={topic.value}, rarity={rarity.value}"
        )
    return TOPIC_RARITY_REQUIREMENTS[key]


def get_diversity_hints(topic: TaskTopic) -> List[str]:
    return DIVERSITY_HINTS.get(topic, [])
