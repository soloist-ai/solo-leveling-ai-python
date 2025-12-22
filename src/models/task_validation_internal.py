from typing import List, Literal, Optional
from pydantic import BaseModel, Field, ConfigDict

from src.avro.enums.localization_item import LocalizationItem


class Requirement(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(description="Unique requirement id, e.g. req_1")
    text: str = Field(description="Human-readable requirement")
    must: bool = Field(default=True, description="If true, failing it invalidates the task")
    kind: Literal["duration", "count", "presence", "multi", "quality", "other"] = "other"
    unit: Optional[str] = None  # "min", "km", "reps", "tracks", etc.
    acceptable_evidence: List[str] = Field(default_factory=list)


class TaskRequirements(BaseModel):
    model_config = ConfigDict(extra="forbid")
    requirements: List[Requirement]


class VisualFact(BaseModel):
    model_config = ConfigDict(extra="forbid")

    kind: Literal["object", "action", "text", "ui", "scene"]
    value: str
    confidence: float = Field(ge=0.0, le=1.0)


class VisualFacts(BaseModel):
    model_config = ConfigDict(extra="forbid")
    facts: List[VisualFact]


class RequirementCheck(BaseModel):
    model_config = ConfigDict(extra="forbid")

    requirement_id: str
    status: Literal["met", "not_met", "unknown"]
    evidence: List[str] = Field(default_factory=list)
    notes: Optional[str] = None


class TaskValidationDecision(BaseModel):
    model_config = ConfigDict(extra="forbid")

    is_valid: bool
    confidence: float = Field(ge=0.0, le=1.0)
    feedback: LocalizationItem
    checks: List[RequirementCheck] = Field(default_factory=list)
