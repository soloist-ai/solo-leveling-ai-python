import random

from src.avro.enums.task_topic import TaskTopic

SCENARIO_CONTEXT_MAP = {
    "MORNING": {
        "intensity": "High energy",
        "context": {
            "general": "Start fresh, energizing activities",
            TaskTopic.PHYSICAL_ACTIVITY: "Light cardio, stretching",
            TaskTopic.PRODUCTIVITY: "Most important tasks first",
            TaskTopic.BRAIN: "Mental warm-up puzzles",
        },
    },
    "OFFICE": {
        "intensity": "Medium energy, quiet",
        "context": {
            "general": "Professional, desk-friendly",
            TaskTopic.DEVELOPMENT: "Code reviews, debugging",
            TaskTopic.PRODUCTIVITY: "Deep focus work",
            TaskTopic.BRAIN: "Quick mental breaks",
            TaskTopic.SOCIAL_SKILLS: "Networking, colleague interactions",
        },
    },
    "EVENING": {
        "intensity": "Low-medium energy",
        "context": {
            "general": "Wind down, social, creative",
            TaskTopic.MUSIC: "Active album listening",
            TaskTopic.CREATIVITY: "Creative projects",
            TaskTopic.SOCIAL_SKILLS: "Social gatherings",
            TaskTopic.READING: "Leisure reading",
        },
    },
    "HOME": {
        "intensity": "Flexible",
        "context": {
            "general": "Comfortable, all resources available",
            TaskTopic.NUTRITION: "Meal prep, cooking experiments",
            TaskTopic.DEVELOPMENT: "Personal projects",
            TaskTopic.CYBERSPORT: "Training sessions",
        },
    },
    "GYM": {
        "intensity": "High energy",
        "context": {
            "general": "Intensive physical training",
            TaskTopic.PHYSICAL_ACTIVITY: "Strength, cardio, HIIT",
        },
    },
    "OUTDOOR": {
        "intensity": "Medium-high energy",
        "context": {
            "general": "Fresh air, exploration",
            TaskTopic.ADVENTURE: "Urban/nature exploration",
            TaskTopic.PHYSICAL_ACTIVITY: "Running, hiking, sports",
        },
    },
    "LATE_NIGHT": {
        "intensity": "Low energy",
        "context": {
            "general": "Quiet, reflective",
            TaskTopic.READING: "Deep reading",
            TaskTopic.BRAIN: "Strategic puzzles",
            TaskTopic.DEVELOPMENT: "Late-night coding",
        },
    },
    "WEEKEND": {
        "intensity": "Flexible, high time budget",
        "context": {
            "general": "Large projects, exploration",
            TaskTopic.ADVENTURE: "Day trips, long walks",
            TaskTopic.CREATIVITY: "Extended creative work",
            TaskTopic.MUSIC: "Multi-album listening sessions",
        },
    },
    "COMMUTE": {
        "intensity": "Low energy, limited mobility",
        "context": {
            "general": "Passive, mobile-friendly",
            TaskTopic.MUSIC: "Album discovery",
            TaskTopic.LANGUAGE_LEARNING: "Audio lessons, flashcards",
            TaskTopic.READING: "Mobile reading",
        },
    },
    "BREAK": {
        "intensity": "Quick refresh",
        "context": {
            "general": "10-30 min activities",
            TaskTopic.PHYSICAL_ACTIVITY: "Stretches, quick walk",
            TaskTopic.BRAIN: "1-2 quick puzzles",
        },
    },
}

TOPIC_SCENARIOS_MAP: dict[TaskTopic, list[str]] = {
    TaskTopic.PHYSICAL_ACTIVITY: ["MORNING", "GYM", "OUTDOOR", "BREAK"],
    TaskTopic.MUSIC: ["EVENING", "COMMUTE", "WEEKEND", "HOME"],
    TaskTopic.DEVELOPMENT: ["OFFICE", "HOME", "LATE_NIGHT", "WEEKEND"],
    TaskTopic.CREATIVITY: ["EVENING", "WEEKEND", "HOME"],
    TaskTopic.SOCIAL_SKILLS: ["OFFICE", "EVENING", "WEEKEND"],
    TaskTopic.NUTRITION: ["HOME", "WEEKEND"],
    TaskTopic.PRODUCTIVITY: ["MORNING", "OFFICE", "HOME"],
    TaskTopic.ADVENTURE: ["OUTDOOR", "WEEKEND"],
    TaskTopic.BRAIN: ["OFFICE", "LATE_NIGHT", "BREAK", "COMMUTE"],
    TaskTopic.CYBERSPORT: ["HOME", "EVENING", "WEEKEND"],
    TaskTopic.READING: ["COMMUTE", "EVENING", "LATE_NIGHT", "HOME"],
    TaskTopic.LANGUAGE_LEARNING: ["COMMUTE", "HOME", "EVENING"],
}


def add_diversity_hint(topic: TaskTopic) -> str:
    """Добавляет случайную подсказку для разнообразия задач"""

    diversity_hints = {
        TaskTopic.PHYSICAL_ACTIVITY: [
            "Focus on push-up variations (wide grip, close grip, decline, incline)",
            "Emphasize bodyweight squats (standard, jump squats, single-leg)",
            "Use pull-ups or chin-ups if available",
            "Focus on plank holds (standard, side plank)",
            "Emphasize lunges (forward, reverse, walking)",
            "Use burpees for full-body work",
            "Focus on running or jogging intervals",
            "Emphasize dips if parallel bars available",
            "Use jumping jacks for cardio",
            "Focus on sit-ups and crunches for core",
        ],
        TaskTopic.MUSIC: [
            "Choose krautrock: Can - Tago Mago, Neu!, Faust",
            "Select afrobeat: Fela Kuti - Zombie, Expensive Shit",
            "Use trip-hop: Portishead, Massive Attack, Tricky",
            "Choose post-rock: Godspeed, Mogwai, Explosions in the Sky",
            "Select IDM: Aphex Twin, Boards of Canada, Autechre",
            "Use shoegaze: My Bloody Valentine, Slowdive",
            "Choose avant-garde jazz: Alice Coltrane, Pharoah Sanders, Sun Ra",
            "Select experimental: Fishmans - Long Season, This Heat",
            "Use electronic: Burial, Four Tet, Flying Lotus",
            "Choose dub techno: Basic Channel, Rhythm & Sound",
        ],
        TaskTopic.DEVELOPMENT: [
            "Focus on graph algorithms (BFS, DFS, shortest path)",
            "Emphasize dynamic programming patterns",
            "Use bit manipulation and bitwise operations",
            "Focus on tree traversals and binary search trees",
            "Emphasize sliding window or two-pointer techniques",
            "Use backtracking and recursion problems",
            "Focus on system design patterns (singleton, factory, observer)",
            "Emphasize test-driven development (write tests first)",
            "Use refactoring exercises on legacy code",
            "Focus on concurrent programming challenges",
        ],
        TaskTopic.CREATIVITY: [
            "Write in second-person perspective",
            "Use stream-of-consciousness style",
            "Create non-linear narrative structure",
            "Focus on sensory details (sounds, textures, smells)",
            "Use dialogue-only format (no narration)",
            "Create speculative fiction or magical realism",
            "Focus on character emotions through actions, not descriptions",
            "Use constraints (no letter 'e', only 100 words, etc.)",
            "Create visual mind maps or concept boards",
            "Focus on world-building elements (languages, cultures, systems)",
        ],
        TaskTopic.SOCIAL_SKILLS: [
            "Practice active listening without interrupting",
            "Use open-ended questions to deepen conversations",
            "Practice giving specific, genuine compliments",
            "Focus on mirroring body language subtly",
            "Practice storytelling with clear structure (setup, conflict, resolution)",
            "Use the 'cold approach' with strangers in public spaces",
            "Practice remembering and using people's names",
            "Focus on finding common ground quickly",
            "Practice graceful disagreement without conflict",
            "Use humor and self-deprecation appropriately",
        ],
        TaskTopic.NUTRITION: [
            "Focus on fermented foods (kimchi, sauerkraut, miso)",
            "Emphasize plant-based protein sources",
            "Use spice blends from different cuisines",
            "Focus on batch cooking grains and legumes",
            "Emphasize seasonal and local ingredients",
            "Use one-pot or sheet-pan meals for efficiency",
            "Focus on protein-forward breakfasts",
            "Emphasize colorful vegetables (eat the rainbow)",
            "Use meal prep containers for portion control",
            "Focus on hydration tracking alongside meals",
        ],
        TaskTopic.PRODUCTIVITY: [
            "Use time-blocking with strict boundaries",
            "Focus on single-tasking (no multitasking)",
            "Apply the 2-minute rule (do it now if < 2 min)",
            "Use the Eisenhower matrix (urgent vs important)",
            "Focus on 'eating the frog' (hardest task first)",
            "Use Pomodoro with 25/5 intervals",
            "Focus on batching similar tasks together",
            "Use the '3 MIT' method (3 Most Important Tasks)",
            "Apply Pareto principle (80/20 rule)",
            "Focus on environment design (remove distractions)",
        ],
        TaskTopic.ADVENTURE: [
            "Explore industrial areas or abandoned places (safely)",
            "Focus on street art and murals in unexpected neighborhoods",
            "Visit local historical markers and read plaques",
            "Explore rooftops or elevated viewpoints",
            "Focus on hidden parks or green spaces",
            "Visit ethnic neighborhoods and cultural districts",
            "Explore waterfronts, rivers, or canals",
            "Focus on architectural details in old buildings",
            "Visit local markets or bazaars",
            "Explore underground passages or metro art",
        ],
        TaskTopic.BRAIN: [
            "Focus on chess tactics (pins, forks, skewers)",
            "Use logic grid puzzles (zebra puzzles)",
            "Solve Sudoku variants (killer, samurai, irregular)",
            "Focus on spatial reasoning puzzles",
            "Use memory techniques (method of loci, linking)",
            "Solve mathematical riddles and paradoxes",
            "Focus on pattern recognition sequences",
            "Use lateral thinking puzzles (situation puzzles)",
            "Solve cryptic crosswords or ciphers",
            "Focus on probability and combinatorics problems",
        ],
        TaskTopic.CYBERSPORT: [
            "Focus on flick accuracy drills",
            "Emphasize tracking moving targets smoothly",
            "Use spray pattern control practice",
            "Focus on crosshair placement pre-aiming",
            "Emphasize counter-strafing mechanics",
            "Use utility lineups memorization",
            "Focus on peeking angles and timing",
            "Emphasize movement optimization (bunny hops, strafes)",
            "Use demo review for decision-making analysis",
            "Focus on economy management in ranked matches",
        ],
        TaskTopic.READING: [
            "Focus on classic literature (pre-1950)",
            "Read long-form investigative journalism",
            "Focus on philosophy or critical theory",
            "Read technical documentation or whitepapers",
            "Focus on biographies of unconventional figures",
            "Read scientific papers or research studies",
            "Focus on translated literature (non-English origins)",
            "Read essay collections or thought pieces",
            "Focus on historical non-fiction",
            "Read genre-blending experimental fiction",
        ],
        TaskTopic.LANGUAGE_LEARNING: [
            "Focus on colloquial expressions and slang",
            "Use sentence mining from native content",
            "Focus on shadowing native speakers",
            "Emphasize writing without translation apps",
            "Use spaced repetition with context sentences",
            "Focus on pronunciation drills (minimal pairs)",
            "Emphasize active recall over passive review",
            "Use comprehensible input (reading/listening just above level)",
            "Focus on grammatical patterns in context",
            "Emphasize conversational practice with natives",
        ],
    }

    hints = diversity_hints.get(topic, [])
    if not hints:
        return ""

    selected_hint = random.choice(hints)
    return f"\n🎯 **Diversity instruction:** {selected_hint}"
