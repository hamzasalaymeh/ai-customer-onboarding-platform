from fastapi import APIRouter

from app.schemas.ai import ChatRequest, ChatResponse
from app.services.ai_service import AIService

router = APIRouter()
ai_service = AIService()


@router.post("/ai/chat", response_model=ChatResponse)
async def chat(payload: ChatRequest) -> ChatResponse:
    reply = await ai_service.chat(payload.messages)
    return ChatResponse(reply=reply)
