# Architecture

## Overview

```
┌──────────────┐        HTTPS/JSON        ┌───────────────┐
│   Frontend   │  ─────────────────────►  │    Backend    │
│ React + Vite │  ◄─────────────────────  │   FastAPI     │
└──────────────┘                          └───────┬───────┘
                                                   │
                                     ┌─────────────┼──────────────┐
                                     │             │              │
                              ┌──────▼─────┐ ┌─────▼──────┐ ┌─────▼──────┐
                              │  Database   │ │ AI Service │ │ External   │
                              │ (SQLAlchemy)│ │ (assistant,│ │ KYC/verify │
                              │             │ │  doc check)│ │ providers  │
                              └─────────────┘ └────────────┘ └────────────┘
```

## Components

### Frontend (`frontend/`)

A React + TypeScript single-page app. Presents the onboarding wizard,
step-by-step progress, and an embedded chat assistant. Talks to the backend
exclusively through the versioned REST API (`/api/v1/...`).

### Backend (`backend/`)

A FastAPI application organized in layers:

- `app/api/` — HTTP routing and request/response handling.
- `app/schemas/` — Pydantic request/response models.
- `app/services/` — business logic (onboarding progression, AI assistant
  orchestration).
- `app/models/` — persistence models (SQLAlchemy).
- `app/db/` — database session/engine setup.
- `app/core/` — configuration and cross-cutting concerns (logging, settings).

### AI assistant

`app/services/ai_service.py` centralizes calls to the language model
provider used to power the onboarding chat assistant and any automated
document-verification summaries. Route handlers never call the model
provider directly.

### Infrastructure (`infrastructure/`)

Terraform definitions for provisioning the cloud resources the platform
runs on (compute, database, networking), split by environment via
`.tfvars` files.

### Docker (`docker/`)

Compose files that wire the backend and frontend together for local
development (`docker-compose.dev.yml`) and production-like runs
(`docker-compose.yml`).

## Data flow: onboarding step submission

1. Frontend submits a step's form data to `POST /api/v1/onboarding/{customer_id}/steps/{step_id}`.
2. The endpoint validates the payload against a Pydantic schema and delegates
   to `OnboardingService`.
3. `OnboardingService` persists the step result, determines the next step,
   and — if the step involves document verification — calls the AI service.
4. The response includes the updated onboarding status and the next step to
   render.
