import uuid
from datetime import datetime
from enum import StrEnum

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class OnboardingStepStatus(StrEnum):
    PENDING = "pending"
    COMPLETED = "completed"
    SKIPPED = "skipped"


class OnboardingStep(Base):
    __tablename__ = "onboarding_steps"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    customer_id: Mapped[str] = mapped_column(String(36), ForeignKey("customers.id"), index=True)
    step_key: Mapped[str] = mapped_column(String(100))
    status: Mapped[str] = mapped_column(String(20), default=OnboardingStepStatus.PENDING)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
