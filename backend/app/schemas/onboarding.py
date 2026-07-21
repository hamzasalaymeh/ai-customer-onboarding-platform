from datetime import datetime

from pydantic import BaseModel, ConfigDict


class OnboardingStepRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    step_key: str
    status: str
    completed_at: datetime | None = None


class OnboardingStatus(BaseModel):
    customer_id: str
    steps: list[OnboardingStepRead]
    next_step_key: str | None = None
    is_complete: bool


class OnboardingStepSubmission(BaseModel):
    data: dict = {}
