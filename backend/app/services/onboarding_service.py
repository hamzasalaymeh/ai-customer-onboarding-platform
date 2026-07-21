from datetime import datetime

from sqlalchemy.orm import Session

from app.models.onboarding import OnboardingStep, OnboardingStepStatus

DEFAULT_STEP_KEYS = [
    "company_details",
    "identity_verification",
    "payment_setup",
    "team_invite",
]


class OnboardingService:
    def __init__(self, db: Session):
        self.db = db

    def get_or_create_steps(self, customer_id: str) -> list[OnboardingStep]:
        steps = (
            self.db.query(OnboardingStep)
            .filter(OnboardingStep.customer_id == customer_id)
            .all()
        )
        if steps:
            return steps

        steps = [
            OnboardingStep(customer_id=customer_id, step_key=key)
            for key in DEFAULT_STEP_KEYS
        ]
        self.db.add_all(steps)
        self.db.commit()
        for step in steps:
            self.db.refresh(step)
        return steps

    def complete_step(self, customer_id: str, step_id: str) -> OnboardingStep | None:
        step = (
            self.db.query(OnboardingStep)
            .filter(OnboardingStep.id == step_id, OnboardingStep.customer_id == customer_id)
            .first()
        )
        if step is None:
            return None

        step.status = OnboardingStepStatus.COMPLETED
        step.completed_at = datetime.utcnow()
        self.db.commit()
        self.db.refresh(step)
        return step

    def next_step_key(self, steps: list[OnboardingStep]) -> str | None:
        for step in steps:
            if step.status == OnboardingStepStatus.PENDING:
                return step.step_key
        return None
