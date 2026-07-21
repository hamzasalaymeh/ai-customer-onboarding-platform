import type { OnboardingStep } from "../types/customer";

interface StepIndicatorProps {
  steps: OnboardingStep[];
}

export function StepIndicator({ steps }: StepIndicatorProps) {
  return (
    <div className="step-indicator">
      {steps.map((step) => (
        <span
          key={step.id}
          className={`step-indicator__dot step-indicator__dot--${
            step.status === "completed" ? "complete" : "current"
          }`}
          title={step.step_key}
        />
      ))}
    </div>
  );
}
