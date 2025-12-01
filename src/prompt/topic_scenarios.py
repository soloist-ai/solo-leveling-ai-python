from src.avro.enums.task_topic import TaskTopic

ALL_SCENARIOS = [
    "Morning Kick-start (Бодрое начало дня)",
    "Midday Reset (Обеденный сброс/перезагрузка)",
    "Evening Wind-down (Вечернее расслабление)",
    "Late Night Ritual (Поздний вечер перед сном)",
    "Quick 5-15 min Break (Быстрый перерыв)",
    "Deep Focus / Dedicated Session (Глубокое погружение)",
    "Low Energy / Recovery Mode (Восстановление / Спокойный режим)",
    "High Energy Challenge (Прилив сил / Амбициозная цель)",
    "At Home / Indoors (Дома / В помещении)",
    "Outdoor Activity (На свежем воздухе)",
    "Work/Study Environment (Рабочая/учебная обстановка)",
    "Solo Time (Время наедине с собой)",
    "With Others / Social Context (В компании / Социальный момент)",
    "Weekend / Free Time (Выходной / Свободное время)",
]

# Маппинг: топик -> подходящие сценарии
TOPIC_SCENARIOS_MAP: dict[TaskTopic, list[str]] = {

    TaskTopic.PHYSICAL_ACTIVITY: [
        "Morning Kick-start (Бодрое начало дня)",
        "Midday Reset (Обеденный сброс/перезагрузка)",
        "Evening Wind-down (Вечернее расслабление)",
        "Quick 5-15 min Break (Быстрый перерыв)",
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
        "Quick 5-15 min Break (Быстрый перерыв)",
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
        "Quick 5-15 min Break (Быстрый перерыв)",
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
        "Quick 5-15 min Break (Быстрый перерыв)",
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

    TaskTopic.MUSIC: ALL_SCENARIOS,  # Музыку можно слушать везде и всегда!

    TaskTopic.BRAIN: [
        "Morning Kick-start (Бодрое начало дня)",
        "Midday Reset (Обеденный сброс/перезагрузка)",
        "Evening Wind-down (Вечернее расслабление)",
        "Late Night Ritual (Поздний вечер перед сном)",
        "Quick 5-15 min Break (Быстрый перерыв)",
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
        "Quick 5-15 min Break (Быстрый перерыв)",
        "Deep Focus / Dedicated Session (Глубокое погружение)",  # обязательно!
        "At Home / Indoors (Дома / В помещении)",
        "Work/Study Environment (Рабочая/учебная обстановка)",  # обязательно!
        "Solo Time (Время наедине с собой)",
        "Weekend / Free Time (Выходной / Свободное время)",
    ],

    TaskTopic.READING: ALL_SCENARIOS,  # Читать можно везде и всегда!

    TaskTopic.LANGUAGE_LEARNING: [
        "Morning Kick-start (Бодрое начало дня)",
        "Midday Reset (Обеденный сброс/перезагрузка)",
        "Evening Wind-down (Вечернее расслабление)",
        "Late Night Ritual (Поздний вечер перед сном)",
        "Quick 5-15 min Break (Быстрый перерыв)",
        "Deep Focus / Dedicated Session (Глубокое погружение)",
        "Low Energy / Recovery Mode (Восстановление / Спокойный режим)",
        "At Home / Indoors (Дома / В помещении)",
        "Work/Study Environment (Рабочая/учебная обстановка)",
        "Solo Time (Время наедине с собой)",
        "With Others / Social Context (В компании / Социальный момент)",  # разговорная практика
        "Weekend / Free Time (Выходной / Свободное время)",
    ],
}
