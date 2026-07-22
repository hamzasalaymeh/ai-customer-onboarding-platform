# AI Customer Onboarding Platform

An AI-assisted platform for onboarding new customers: guided multi-step
onboarding flows, automated document/KYC verification, and a conversational
AI assistant that helps customers complete onboarding faster.

## Project layout

```
.
├── .claude/          Claude Code project configuration and instructions
├── backend/          FastAPI application (REST API, AI services, data layer)
├── frontend/         React + TypeScript single-page application
├── infrastructure/   Terraform IaC for cloud environments
├── docker/           Docker Compose orchestration for local/dev/prod
├── docs/             Architecture and API documentation
└── tests/            Cross-cutting and end-to-end tests
```

## Quick start

### Local development with Docker

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
docker compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml up --build
```

- Backend API: http://localhost:8000
- API docs (Swagger): http://localhost:8000/docs
- Frontend: http://localhost:5173

### Running services individually

See [`backend/README.md`](backend/README.md) and
[`frontend/README.md`](frontend/README.md) for instructions on running each
service without Docker.

## Documentation

### Quick Links

- **[Enterprise Architecture Overview](docs/enterprise-architecture.md)** — Complete 12-specification framework (Workflow Engine, Business Rules, Security, AI, Integration, Infrastructure, DevSecOps)
- **[Technical Architecture](docs/architecture.md)** — Component diagrams and data flow
- **[Architecture Topic Index](docs/architecture-index.md)** — Searchable index of 1000+ topics
- **[Cross-Reference Matrix](docs/cross-reference-matrix.md)** — Bidirectional specification mapping
- **[API Reference](docs/api-reference.md)** — REST API specification
- **[Getting Started](docs/getting-started.md)** — Developer quick-start guide

Start with [`docs/README.md`](docs/README.md) for complete architecture, API, and
onboarding-flow documentation.

## Testing

See [`tests/README.md`](tests/README.md) for how backend, frontend, and
end-to-end tests are organized and run.
