from pydantic import BaseModel


class LocalizationItem(BaseModel):
    en: str
    ru: str
