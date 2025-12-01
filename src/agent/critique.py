from pydantic import BaseModel, Field


class CritiqueResult(BaseModel):
    is_approved: bool = Field(
        description="True if the task is valid and fits the topic, False otherwise."
    )
    feedback: str = Field(
        description="If not approved, explain why specifically. If approved, leave empty."
    )
