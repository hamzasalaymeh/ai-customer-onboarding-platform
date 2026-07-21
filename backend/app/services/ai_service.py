"""Orchestrates calls to the language model that powers the onboarding
assistant. Kept isolated from route handlers so the provider can be swapped
without touching API code.
"""

from app.core.config import get_settings
from app.schemas.ai import ChatMessage

settings = get_settings()

SYSTEM_PROMPT = (
    "You are the onboarding assistant for a B2B platform. Help the customer "
    "complete their onboarding steps clearly and concisely."
)


class AIService:
    def __init__(self) -> None:
        self.model_name = settings.ai_model_name
        self.api_key = settings.ai_provider_api_key

    async def chat(self, messages: list[ChatMessage]) -> str:
        if not self.api_key:
            return self._fallback_reply(messages)

        # Integration point: call the configured LLM provider here, e.g.
        # via the Anthropic SDK, passing SYSTEM_PROMPT + `messages`.
        return self._fallback_reply(messages)

    def _fallback_reply(self, messages: list[ChatMessage]) -> str:
        last_user_message = next(
            (m.content for m in reversed(messages) if m.role == "user"), ""
        )
        return (
            "Thanks for your message. I can help you with onboarding steps "
            f"like identity verification and payment setup. You said: "
            f"\"{last_user_message}\""
        )
