import { ChatAssistant } from "../components/ChatAssistant";
import { OnboardingWizard } from "../components/OnboardingWizard";

interface OnboardingPageProps {
  customerId: string;
}

export function OnboardingPage({ customerId }: OnboardingPageProps) {
  return (
    <div>
      <h1>Welcome — let's get you set up</h1>
      <OnboardingWizard customerId={customerId} />
      <ChatAssistant />
    </div>
  );
}
