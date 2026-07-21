from fastapi import APIRouter

from app.api.v1.endpoints import ai_assistant, customers, health, onboarding

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(customers.router, tags=["customers"])
api_router.include_router(onboarding.router, tags=["onboarding"])
api_router.include_router(ai_assistant.router, tags=["ai"])
