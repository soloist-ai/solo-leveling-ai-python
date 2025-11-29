from enum import Enum


class TaskTopic(str, Enum):
    PHYSICAL_ACTIVITY = "PHYSICAL_ACTIVITY"
    CREATIVITY = "CREATIVITY"
    SOCIAL_SKILLS = "SOCIAL_SKILLS"
    NUTRITION = "NUTRITION"
    PRODUCTIVITY = "PRODUCTIVITY"
    CYBERSPORT = "CYBERSPORT"
    CODING_AND_DEV = "CODING_AND_DEV"
    ADVENTURE = "ADVENTURE"
    READING = "READING"
    LANGUAGE_LEARNING = "LANGUAGE_LEARNING"
    HOUSEHOLD = "HOUSEHOLD"
    DETOX = "DETOX"
    FINANCE = "FINANCE"
    SLEEP = "SLEEP"

    def to_dict(self) -> str:
        return self.value

    @classmethod
    def from_dict(cls, data: str) -> "TaskTopic":
        return cls(data)
