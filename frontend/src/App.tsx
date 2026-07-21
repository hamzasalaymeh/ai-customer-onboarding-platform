import { OnboardingPage } from "./pages/Onboarding";

const DEMO_CUSTOMER_ID = "demo-customer";

export function App() {
  return (
    <div className="app-shell">
      <OnboardingPage customerId={DEMO_CUSTOMER_ID} />
    </div>
  );
}
