export interface Customer {
  id: string;
  full_name: string;
  email: string;
  company_name: string | null;
  created_at: string;
}

export interface OnboardingStep {
  id: string;
  step_key: string;
  status: "pending" | "completed" | "skipped";
  completed_at: string | null;
}

export interface OnboardingStatus {
  customer_id: string;
  steps: OnboardingStep[];
  next_step_key: string | null;
  is_complete: boolean;
}

export interface ChatMessage {
  role: "user" | "assistant";
  content: string;
}
