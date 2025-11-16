from dataclasses import dataclass, asdict


@dataclass
class LocalizationItem:
    en: str
    ru: str

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "LocalizationItem":
        return cls(en=data["en"], ru=data["ru"])
