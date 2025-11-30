from enum import Enum


class TaskTopic(str, Enum):
    PHYSICAL_ACTIVITY = "PHYSICAL_ACTIVITY"
    CREATIVITY = "CREATIVITY"
    SOCIAL_SKILLS = "SOCIAL_SKILLS"
    NUTRITION = "NUTRITION"
    PRODUCTIVITY = "PRODUCTIVITY"
    ADVENTURE = "ADVENTURE"
    MUSIC = "MUSIC"
    BRAIN = "BRAIN"
    CYBERSPORT = "CYBERSPORT"
    DEVELOPMENT = "DEVELOPMENT"
    READING = "READING"
    LANGUAGE_LEARNING = "LANGUAGE_LEARNING"

    def to_dict(self) -> str:
        return self.value

    @classmethod
    def from_dict(cls, data: str) -> "TaskTopic":
        return cls(data)
