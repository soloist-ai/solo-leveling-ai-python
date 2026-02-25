from enum import Enum


class SaveTasksOperation(str, Enum):
    INITIALIZE = "INITIALIZE"
    COMPLETE = "COMPLETE"
    SKIP = "SKIP"

    def to_dict(self) -> str:
        return self.value

    @classmethod
    def from_dict(cls, data: str) -> "SaveTasksOperation":
        return cls(data)
