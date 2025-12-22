from pydantic import BaseModel, Field

from src.avro.enums.localization_item import LocalizationItem


class TaskValidationResponse(BaseModel):
    """Результат валидации выполнения задачи"""
    is_valid: bool = Field(description="Прошла ли задача валидацию")
    confidence: float = Field(
        ge=0.0,
        le=1.0,
        description="Уверенность в решении (0.0 - 1.0)"
    )
    feedback: LocalizationItem = Field(
        description="Объяснение решения на двух языках"
    )