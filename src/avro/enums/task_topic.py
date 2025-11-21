from enum import Enum


class TaskTopic(str, Enum):
    PHYSICAL_ACTIVITY = "PHYSICAL_ACTIVITY"
    MENTAL_HEALTH = "MENTAL_HEALTH"
    EDUCATION = "EDUCATION"
    CREATIVITY = "CREATIVITY"
    SOCIAL_SKILLS = "SOCIAL_SKILLS"
    HEALTHY_EATING = "HEALTHY_EATING"
    PRODUCTIVITY = "PRODUCTIVITY"
    EXPERIMENTS = "EXPERIMENTS"
    ECOLOGY = "ECOLOGY"
    TEAMWORK = "TEAMWORK"

    def to_dict(self) -> str:
        return self.value

    @classmethod
    def from_dict(cls, data: str) -> "TaskTopic":
        return cls(data)
