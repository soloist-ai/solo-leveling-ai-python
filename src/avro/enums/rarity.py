from enum import Enum


class Rarity(str, Enum):
    COMMON = "COMMON"
    UNCOMMON = "UNCOMMON"
    RARE = "RARE"
    EPIC = "EPIC"
    LEGENDARY = "LEGENDARY"

    def to_dict(self) -> str:
        return self.value

    @classmethod
    def from_dict(cls, data: str) -> "Rarity":
        return cls(data)
