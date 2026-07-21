from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.onboarding import OnboardingStatus, OnboardingStepSubmission
from app.services.onboarding_service import OnboardingService

router = APIRouter()


@router.get("/onboarding/{customer_id}", response_model=OnboardingStatus)
def get_onboarding_status(customer_id: str, db: Session = Depends(get_db)) -> OnboardingStatus:
    service = OnboardingService(db)
    steps = service.get_or_create_steps(customer_id)
    next_key = service.next_step_key(steps)
    return OnboardingStatus(
        customer_id=customer_id,
        steps=steps,
        next_step_key=next_key,
        is_complete=next_key is None,
    )


@router.post("/onboarding/{customer_id}/steps/{step_id}", response_model=OnboardingStatus)
def submit_onboarding_step(
    customer_id: str,
    step_id: str,
    payload: OnboardingStepSubmission,
    db: Session = Depends(get_db),
) -> OnboardingStatus:
    service = OnboardingService(db)
    step = service.complete_step(customer_id, step_id)
    if step is None:
        raise HTTPException(status_code=404, detail="Onboarding step not found")

    steps = service.get_or_create_steps(customer_id)
    next_key = service.next_step_key(steps)
    return OnboardingStatus(
        customer_id=customer_id,
        steps=steps,
        next_step_key=next_key,
        is_complete=next_key is None,
    )
