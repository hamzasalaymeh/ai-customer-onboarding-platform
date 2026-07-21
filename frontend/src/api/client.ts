import type { ChatMessage, OnboardingStatus } from "../types/customer";

const BASE_URL = import.meta.env.VITE_API_BASE_URL ?? "/api/v1";

async function request<T>(path: string, options?: RequestInit): Promise<T> {
  const response = await fetch(`${BASE_URL}${path}`, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });

  if (!response.ok) {
    throw new Error(`Request to ${path} failed with status ${response.status}`);
  }

  return response.json() as Promise<T>;
}

export const api = {
  getOnboardingStatus: (customerId: string) =>
    request<OnboardingStatus>(`/onboarding/${customerId}`),

  submitOnboardingStep: (customerId: string, stepId: string, data: Record<string, unknown>) =>
    request<OnboardingStatus>(`/onboarding/${customerId}/steps/${stepId}`, {
      method: "POST",
      body: JSON.stringify({ data }),
    }),

  sendChatMessage: (messages: ChatMessage[], customerId?: string) =>
    request<{ reply: string }>("/ai/chat", {
      method: "POST",
      body: JSON.stringify({ messages, customer_id: customerId }),
    }),
};
