# AI Customer Onboarding Platform — Claude Code Guide

## What this project is

A platform that helps businesses onboard new customers with an AI-assisted
guided flow: multi-step forms, document/KYC verification, and a
conversational assistant that answers questions and unblocks stuck users.

Built on a comprehensive 12-specification enterprise architecture framework
including Workflow Engine, Business Rules Engine, Security Architecture, AI
Architecture, Integration Architecture, Infrastructure Architecture, and
DevSecOps Architecture. See [Enterprise Architecture Overview](../docs/enterprise-architecture.md)
for complete architectural documentation.

## Stack

- **backend/** — Python, FastAPI, SQLAlchemy, Pydantic. Entry point:
  `backend/app/main.py`. API routes live under `backend/app/api/v1/endpoints/`.
- **frontend/** — React + TypeScript, built with Vite. Entry point:
  `frontend/src/main.tsx`.
- **infrastructure/** — Terraform for cloud environments (dev/prod).
- **docker/** — Compose files that orchestrate backend + frontend for local
  development and production-like environments.
- **tests/** — Backend (pytest) and end-to-end tests. Frontend unit tests
  live alongside components in `frontend/src`.

## Conventions

- Backend: type-annotated Python, Pydantic schemas separate from SQLAlchemy
  models (`app/schemas/` vs `app/models/`). Business logic belongs in
  `app/services/`, not in route handlers.
- Frontend: functional components with hooks, TypeScript types in
  `src/types/`, API calls centralized in `src/api/client.ts`.
- Keep route handlers thin — validate input, call a service, return the
  response.

## Running things

See the root `README.md` for Docker quick start, or `backend/README.md` /
`frontend/README.md` for running each service standalone.

## Before committing

- Backend: `pytest` from `backend/`.
- Frontend: `npm run lint && npm run build` from `frontend/`.
