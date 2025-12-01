from src.avro.enums.task_topic import TaskTopic

SCENARIO_CONTEXT_MAP = {
    "Morning Kick-start (Бодрое начало дня)": {
        "description": "Early morning (6-9 AM), fresh energy, setting tone for the day",
        "intensity": "MEDIUM-HIGH - energizing, activating, invigorating",
        "context": {
            TaskTopic.PHYSICAL_ACTIVITY: "Energizing exercises to wake up the body (jumping jacks, light jog, dynamic stretching). Moderate to high intensity.",
            TaskTopic.CREATIVITY: "Fresh mind for brainstorming, morning pages, creative writing. High mental clarity.",
            TaskTopic.SOCIAL_SKILLS: "Morning greetings, networking breakfast, positive interactions to start the day.",
            TaskTopic.NUTRITION: "Healthy breakfast preparation, morning smoothie, meal planning for the day.",
            TaskTopic.PRODUCTIVITY: "Most important task first, deep focus work, planning the day. Peak cognitive performance.",
            TaskTopic.ADVENTURE: "Morning exploration walk, sunrise photography, discovering new routes.",
            TaskTopic.MUSIC: "Uplifting, energizing music (rock, pop, electronic, upbeat classics).",
            TaskTopic.BRAIN: "Morning mental exercises, logic puzzles, memory training. Sharp mind.",
            TaskTopic.CYBERSPORT: "Practice aim drills, warm-up routines, reaction time training.",
            TaskTopic.DEVELOPMENT: "Tackle hardest coding problem first, system design, architecture planning.",
            TaskTopic.READING: "Educational reading, technical docs, motivational content.",
            TaskTopic.LANGUAGE_LEARNING: "Vocabulary review, grammar exercises, morning language practice.",
        }
    },

    "Midday Reset (Обеденный сброс/перезагрузка)": {
        "description": "Lunch break (12-2 PM), recharge between work sessions, break from routine",
        "intensity": "MEDIUM - refreshing, resetting, re-energizing",
        "context": {
            TaskTopic.PHYSICAL_ACTIVITY: "Midday walk, desk stretches, light cardio to break up sitting. Moderate intensity.",
            TaskTopic.CREATIVITY: "Creative break from work, doodling, quick artistic exercise.",
            TaskTopic.SOCIAL_SKILLS: "Lunch conversations, networking during break, team interactions.",
            TaskTopic.NUTRITION: "Healthy lunch preparation, mindful eating, balanced meal.",
            TaskTopic.PRODUCTIVITY: "Quick task completion, organizing workspace, short focused work burst.",
            TaskTopic.ADVENTURE: "Explore nearby area during lunch, visit new café, urban discovery.",
            TaskTopic.MUSIC: "Background music for lunch, discovering new artists, relaxing listening.",
            TaskTopic.BRAIN: "Midday mental break with puzzles, crosswords, brain teasers.",
            TaskTopic.CYBERSPORT: "Quick practice session, reviewing strategies, short competitive match.",
            TaskTopic.DEVELOPMENT: "Code review, refactoring, documentation work.",
            TaskTopic.READING: "Articles, blog posts, industry news during lunch break.",
            TaskTopic.LANGUAGE_LEARNING: "Quick language app session, flashcards, podcast listening.",
        }
    },

    "Evening Wind-down (Вечернее расслабление)": {
        "description": "After work/dinner (7-10 PM), transitioning to rest, lowering energy",
        "intensity": "LOW - calming, gentle, relaxing, preparing for sleep",
        "context": {
            TaskTopic.PHYSICAL_ACTIVITY: "Gentle yoga, slow stretching, evening walk at relaxed pace, light mobility work. LOW intensity only.",
            TaskTopic.CREATIVITY: "Relaxing creative hobbies (coloring, gentle crafts), journaling, reflective writing.",
            TaskTopic.SOCIAL_SKILLS: "Calm conversations with family/friends, reflective discussions, video calls.",
            TaskTopic.NUTRITION: "Light dinner preparation, evening tea ritual, meal planning for tomorrow.",
            TaskTopic.PRODUCTIVITY: "Review day accomplishments, light planning, organizing for tomorrow. No intense work.",
            TaskTopic.ADVENTURE: "Calm evening stroll, neighborhood exploration, sunset photography.",
            TaskTopic.MUSIC: "Ambient, classical, jazz, chill music. Soothing, calming albums.",
            TaskTopic.BRAIN: "Relaxing puzzles, easy Sudoku, memory games. Not too mentally taxing.",
            TaskTopic.CYBERSPORT: "Casual gaming, reviewing replays, strategy analysis (not competitive matches).",
            TaskTopic.DEVELOPMENT: "Light coding, reading documentation, learning new concepts. No debugging.",
            TaskTopic.READING: "Fiction, relaxing non-fiction, leisurely reading.",
            TaskTopic.LANGUAGE_LEARNING: "Passive learning (watching shows), easy reading, review of learned material.",
        }
    },

    "Late Night Ritual (Поздний вечер перед сном)": {
        "description": "Before bed (10 PM-midnight), winding down, preparing for sleep",
        "intensity": "VERY LOW - minimal effort, meditative, calming, sleep-friendly",
        "context": {
            TaskTopic.CREATIVITY: "Journaling, gratitude writing, gentle sketching, bedtime reflections.",
            TaskTopic.NUTRITION: "Planning tomorrow's meals, herbal tea preparation, light prep work.",
            TaskTopic.BRAIN: "Very light mental activity (easy riddles, calming puzzles). Nothing stimulating.",
            TaskTopic.CYBERSPORT: "Watching pro streams (not playing), strategy review, planning practice.",
            TaskTopic.DEVELOPMENT: "Reading documentation, learning theory, planning tomorrow's work. No coding.",
            TaskTopic.READING: "Light fiction, calming books, bedtime reading.",
            TaskTopic.LANGUAGE_LEARNING: "Passive listening, meditation in target language, light review.",
        }
    },

    "Deep Focus / Dedicated Session (Глубокое погружение)": {
        "description": "Extended focused time, no interruptions, maximum concentration",
        "intensity": "HIGH - intensive, sustained effort, flow state",
        "context": {
            TaskTopic.CREATIVITY: "Major creative project, extensive writing, detailed artwork, deep creative work.",
            TaskTopic.PRODUCTIVITY: "Deep work on critical project, extensive task completion, major deliverables.",
            TaskTopic.BRAIN: "Complex problem-solving, challenging puzzles, intensive mental training.",
            TaskTopic.CYBERSPORT: "Extended practice session, competitive grinding, skill mastery work.",
            TaskTopic.DEVELOPMENT: "Complex feature implementation, system design, hard algorithm problems.",
            TaskTopic.READING: "Deep reading with notes, analyzing complex texts, extensive study.",
            TaskTopic.LANGUAGE_LEARNING: "Intensive grammar study, extensive conversation practice, immersion session.",
        }
    },

    "Low Energy / Recovery Mode (Восстановление / Спокойный режим)": {
        "description": "Tired, low motivation, gentle activities only, self-care",
        "intensity": "VERY LOW - minimal effort, restorative, gentle",
        "context": {
            TaskTopic.PHYSICAL_ACTIVITY: "Gentle stretching, slow walk, restorative yoga, light mobility. No cardio.",
            TaskTopic.CREATIVITY: "Coloring books, simple crafts, easy creative tasks. No pressure.",
            TaskTopic.BRAIN: "Easy puzzles, simple games, light mental activity. Nothing challenging.",
            TaskTopic.READING: "Light fiction, easy reading, no dense material.",
            TaskTopic.LANGUAGE_LEARNING: "Passive listening, watching shows with subtitles, easy review.",
        }
    },

    "High Energy Challenge (Прилив сил / Амбициозная цель)": {
        "description": "Peak energy, motivated, ready for intense challenge",
        "intensity": "VERY HIGH - vigorous, demanding, maximum effort",
        "context": {
            TaskTopic.PHYSICAL_ACTIVITY: "Intensive workouts, HIIT, long runs, challenging sports. Maximum intensity.",
            TaskTopic.SOCIAL_SKILLS: "Public speaking, leading groups, networking events, bold interactions.",
            TaskTopic.PRODUCTIVITY: "Tackle biggest project, complete major milestone, extensive task clearing.",
            TaskTopic.ADVENTURE: "Long hikes, challenging exploration, full-day adventure.",
        }
    },

    "At Home / Indoors (Дома / В помещении)": {
        "description": "Indoor setting, home environment, controlled space",
        "intensity": "VARIABLE - depends on activity",
        "context": {
            TaskTopic.PHYSICAL_ACTIVITY: "Bodyweight exercises, indoor cardio, yoga, resistance bands. No equipment needed.",
            TaskTopic.CREATIVITY: "Home crafts, writing, drawing, DIY projects.",
            TaskTopic.SOCIAL_SKILLS: "Phone calls, video chats, family interactions.",
            TaskTopic.NUTRITION: "Cooking, meal prep, kitchen organization.",
            TaskTopic.PRODUCTIVITY: "Home office work, organizing living space, household tasks.",
            TaskTopic.ADVENTURE: "Exploring rooms/areas you don't usually visit, reorganizing spaces.",
            TaskTopic.MUSIC: "Home listening session, discovering albums at leisure.",
            TaskTopic.BRAIN: "Puzzles, board games, mental exercises at home.",
            TaskTopic.CYBERSPORT: "Gaming setup at home, practice in comfortable environment.",
            TaskTopic.DEVELOPMENT: "Coding at home setup, personal projects, learning.",
            TaskTopic.READING: "Comfortable reading at home, library browsing.",
            TaskTopic.LANGUAGE_LEARNING: "Home study, app practice, online lessons.",
        }
    },

    "Outdoor Activity (На свежем воздухе)": {
        "description": "Outside environment, fresh air, nature or urban setting",
        "intensity": "MEDIUM-HIGH - active, exploring, movement-focused",
        "context": {
            TaskTopic.PHYSICAL_ACTIVITY: "Running, hiking, outdoor sports, park workouts. Use outdoor space.",
            TaskTopic.SOCIAL_SKILLS: "Meeting people outdoors, park conversations, street interactions.",
            TaskTopic.ADVENTURE: "Exploring nature/city, hiking trails, urban discovery, photography walks.",
        }
    },

    "Work/Study Environment (Рабочая/учебная обстановка)": {
        "description": "Professional/academic setting, desk work, focused environment",
        "intensity": "MEDIUM - productive, focused, goal-oriented",
        "context": {
            TaskTopic.PHYSICAL_ACTIVITY: "Desk stretches, office yoga, stair climbing, walking meetings.",
            TaskTopic.CREATIVITY: "Work-related creative tasks, brainstorming at desk, design work.",
            TaskTopic.SOCIAL_SKILLS: "Professional networking, team communication, presentations.",
            TaskTopic.NUTRITION: "Healthy office snacks, meal prep for work, lunch planning.",
            TaskTopic.PRODUCTIVITY: "Core work tasks, project completion, professional deliverables.",
            TaskTopic.CYBERSPORT: "Practice in study setup, skill training at desk.",
            TaskTopic.DEVELOPMENT: "Professional coding, work projects, technical tasks.",
            TaskTopic.READING: "Industry reading, technical documentation, professional learning.",
            TaskTopic.LANGUAGE_LEARNING: "Business language practice, professional vocabulary.",
        }
    },

    "Solo Time (Время наедине с собой)": {
        "description": "Alone, self-focused, no social interaction required",
        "intensity": "VARIABLE - introspective, personal",
        "context": {
            TaskTopic.PHYSICAL_ACTIVITY: "Individual workouts, solo runs, personal training.",
            TaskTopic.CREATIVITY: "Personal creative projects, solo art, journaling.",
            TaskTopic.NUTRITION: "Cooking for yourself, meal prep, personal nutrition planning.",
            TaskTopic.PRODUCTIVITY: "Individual work, personal projects, solo focus time.",
            TaskTopic.ADVENTURE: "Solo exploration, independent discovery, personal journeys.",
            TaskTopic.MUSIC: "Personal listening sessions, discovering music alone.",
            TaskTopic.BRAIN: "Individual puzzles, solo mental challenges.",
            TaskTopic.CYBERSPORT: "Solo practice, individual skill training, self-analysis.",
            TaskTopic.DEVELOPMENT: "Personal coding projects, individual learning.",
            TaskTopic.READING: "Personal reading time, solo study.",
            TaskTopic.LANGUAGE_LEARNING: "Self-study, independent practice, solo learning.",
        }
    },

    "With Others / Social Context (В компании / Социальный момент)": {
        "description": "Group setting, social interaction, collaborative environment",
        "intensity": "MEDIUM-HIGH - social, interactive, collaborative",
        "context": {
            TaskTopic.PHYSICAL_ACTIVITY: "Group sports, partner workouts, team activities.",
            TaskTopic.SOCIAL_SKILLS: "Group conversations, networking, social events. PRIMARY FOCUS.",
            TaskTopic.ADVENTURE: "Group exploration, social outings, discovering places with others.",
            TaskTopic.LANGUAGE_LEARNING: "Conversation practice with others, language exchange, group learning.",
        }
    },

    "Weekend / Free Time (Выходной / Свободное время)": {
        "description": "Days off, leisure time, flexible schedule, no work pressure",
        "intensity": "VARIABLE - relaxed, exploratory, at your own pace",
        "context": {
            # Применимо ко ВСЕМ топикам - свободное время для любых активностей
            "general": "More time available, flexible scheduling, can do longer/more intensive tasks, leisure mindset, personal projects, hobbies, exploration. No work deadlines or constraints."
        }
    },
}

TOPIC_SCENARIOS_MAP: dict[TaskTopic, list[str]] = {

    TaskTopic.PHYSICAL_ACTIVITY: [
        "Morning Kick-start (Бодрое начало дня)",
        "Midday Reset (Обеденный сброс/перезагрузка)",
        "Evening Wind-down (Вечернее расслабление)",
        "High Energy Challenge (Прилив сил / Амбициозная цель)",
        "At Home / Indoors (Дома / В помещении)",
        "Outdoor Activity (На свежем воздухе)",
        "Solo Time (Время наедине с собой)",
        "Weekend / Free Time (Выходной / Свободное время)",
    ],

    TaskTopic.CREATIVITY: [
        "Morning Kick-start (Бодрое начало дня)",
        "Midday Reset (Обеденный сброс/перезагрузка)",
        "Evening Wind-down (Вечернее расслабление)",
        "Late Night Ritual (Поздний вечер перед сном)",
        "Deep Focus / Dedicated Session (Глубокое погружение)",
        "Low Energy / Recovery Mode (Восстановление / Спокойный режим)",
        "At Home / Indoors (Дома / В помещении)",
        "Work/Study Environment (Рабочая/учебная обстановка)",
        "Solo Time (Время наедине с собой)",
        "Weekend / Free Time (Выходной / Свободное время)",
    ],

    TaskTopic.SOCIAL_SKILLS: [
        "Morning Kick-start (Бодрое начало дня)",
        "Midday Reset (Обеденный сброс/перезагрузка)",
        "Evening Wind-down (Вечернее расслабление)",
        "High Energy Challenge (Прилив сил / Амбициозная цель)",
        "At Home / Indoors (Дома / В помещении)",  # звонки, видеозвонки
        "Outdoor Activity (На свежем воздухе)",  # знакомства в парке
        "Work/Study Environment (Рабочая/учебная обстановка)",
        "With Others / Social Context (В компании / Социальный момент)",  # обязательно!
        "Weekend / Free Time (Выходной / Свободное время)",
    ],

    TaskTopic.NUTRITION: [
        "Morning Kick-start (Бодрое начало дня)",  # завтрак
        "Midday Reset (Обеденный сброс/перезагрузка)",  # обед
        "Evening Wind-down (Вечернее расслабление)",  # ужин
        "Late Night Ritual (Поздний вечер перед сном)",  # планирование
        "At Home / Indoors (Дома / В помещении)",
        "Work/Study Environment (Рабочая/учебная обстановка)",  # meal prep
        "Solo Time (Время наедине с собой)",
        "Weekend / Free Time (Выходной / Свободное время)",
    ],

    TaskTopic.PRODUCTIVITY: [
        "Morning Kick-start (Бодрое начало дня)",
        "Midday Reset (Обеденный сброс/перезагрузка)",
        "Deep Focus / Dedicated Session (Глубокое погружение)",  # обязательно!
        "At Home / Indoors (Дома / В помещении)",
        "Work/Study Environment (Рабочая/учебная обстановка)",  # обязательно!
        "Solo Time (Время наедине с собой)",
        "Weekend / Free Time (Выходной / Свободное время)",
    ],

    TaskTopic.ADVENTURE: [
        "Morning Kick-start (Бодрое начало дня)",
        "Midday Reset (Обеденный сброс/перезагрузка)",
        "High Energy Challenge (Прилив сил / Амбициозная цель)",
        "Outdoor Activity (На свежем воздухе)",  # обязательно!
        "Solo Time (Время наедине с собой)",
        "With Others / Social Context (В компании / Социальный момент)",
        "Weekend / Free Time (Выходной / Свободное время)",  # обязательно!
    ],

    TaskTopic.MUSIC: list(SCENARIO_CONTEXT_MAP.keys()),  # Музыку можно слушать везде и всегда!

    TaskTopic.BRAIN: [
        "Morning Kick-start (Бодрое начало дня)",
        "Midday Reset (Обеденный сброс/перезагрузка)",
        "Evening Wind-down (Вечернее расслабление)",
        "Late Night Ritual (Поздний вечер перед сном)",
        "Deep Focus / Dedicated Session (Глубокое погружение)",
        "Low Energy / Recovery Mode (Восстановление / Спокойный режим)",
        "At Home / Indoors (Дома / В помещении)",
        "Work/Study Environment (Рабочая/учебная обстановка)",
        "Solo Time (Время наедине с собой)",
        "Weekend / Free Time (Выходной / Свободное время)",
    ],

    TaskTopic.CYBERSPORT: [
        "Midday Reset (Обеденный сброс/перезагрузка)",
        "Evening Wind-down (Вечернее расслабление)",
        "Late Night Ritual (Поздний вечер перед сном)",
        "Deep Focus / Dedicated Session (Глубокое погружение)",
        "At Home / Indoors (Дома / В помещении)",  # обязательно!
        "Work/Study Environment (Рабочая/учебная обстановка)",  # домашний офис
        "Solo Time (Время наедине с собой)",
        "Weekend / Free Time (Выходной / Свободное время)",
    ],

    TaskTopic.DEVELOPMENT: [
        "Morning Kick-start (Бодрое начало дня)",
        "Midday Reset (Обеденный сброс/перезагрузка)",
        "Evening Wind-down (Вечернее расслабление)",
        "Late Night Ritual (Поздний вечер перед сном)",
        "Deep Focus / Dedicated Session (Глубокое погружение)",  # обязательно!
        "At Home / Indoors (Дома / В помещении)",
        "Work/Study Environment (Рабочая/учебная обстановка)",  # обязательно!
        "Solo Time (Время наедине с собой)",
        "Weekend / Free Time (Выходной / Свободное время)",
    ],

    TaskTopic.READING: list(SCENARIO_CONTEXT_MAP.keys()),  # Читать можно везде и всегда!

    TaskTopic.LANGUAGE_LEARNING: [
        "Morning Kick-start (Бодрое начало дня)",
        "Midday Reset (Обеденный сброс/перезагрузка)",
        "Evening Wind-down (Вечернее расслабление)",
        "Late Night Ritual (Поздний вечер перед сном)",
        "Deep Focus / Dedicated Session (Глубокое погружение)",
        "Low Energy / Recovery Mode (Восстановление / Спокойный режим)",
        "At Home / Indoors (Дома / В помещении)",
        "Work/Study Environment (Рабочая/учебная обстановка)",
        "Solo Time (Время наедине с собой)",
        "With Others / Social Context (В компании / Социальный момент)",  # разговорная практика
        "Weekend / Free Time (Выходной / Свободное время)",
    ],
}

