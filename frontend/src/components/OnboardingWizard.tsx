import { useEffect, useState } from "react";
import { api } from "../api/client";
import type { OnboardingStatus } from "../types/customer";
import { StepIndicator } from "./StepIndicator";

interface OnboardingWizardProps {
  customerId: string;
}

export function OnboardingWizard({ customerId }: OnboardingWizardProps) {
  const [status, setStatus] = useState<OnboardingStatus | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    api
      .getOnboardingStatus(customerId)
      .then(setStatus)
      .catch(() => setError("Could not load onboarding status."));
  }, [customerId]);

  if (error) return <p role="alert">{error}</p>;
  if (!status) return <p>Loading onboarding status…</p>;

  const currentStep = status.steps.find((s) => s.step_key === status.next_step_key);

  async function completeCurrentStep() {
    if (!currentStep) return;
    const updated = await api.submitOnboardingStep(customerId, currentStep.id, {});
    setStatus(updated);
  }

  return (
    <section>
      <StepIndicator steps={status.steps} />
      {status.is_complete ? (
        <p>🎉 Onboarding complete!</p>
      ) : (
        <div>
          <h2>{currentStep?.step_key.replace(/_/g, " ")}</h2>
          <button onClick={completeCurrentStep}>Mark step complete</button>
        </div>
      )}
    </section>
  );
}
