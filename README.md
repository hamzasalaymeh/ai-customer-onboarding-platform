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

- **[Enterprise Architecture Overview](docs/enterprise-architecture.md)** — Complete 21-specification framework (Workflow Engine, Business Rules, Security, AI, Integration, Infrastructure, DevSecOps, Testing, Operations, Data Governance, Analytics & BI, IAM, ESB, Microservices, Cloud, Kubernetes)
- **[Technical Architecture](docs/architecture.md)** — Component diagrams and data flow
- **[Testing Architecture](docs/testing-architecture.md)** — Quality assurance framework
- **[Operations Architecture](docs/operations-architecture.md)** — Service management framework
- **[Data Governance Architecture](docs/data-governance-architecture.md)** — Data governance framework
- **[Analytics & Business Intelligence Architecture](docs/analytics-bi-architecture.md)** — Analytics and BI framework
- **[Microservices Architecture](docs/microservices-architecture.md)** — Microservices and distributed systems framework
- **[Architecture Topic Index](docs/architecture-index.md)** — Searchable index of 2280+ topics
- **[Kubernetes Architecture](docs/kubernetes-architecture.md)** — Kubernetes specification overview
- **[Kubernetes Topic Index](docs/kubernetes-topic-index.md)** — Kubernetes architecture topics (200+ across 5 parts)
- **[Testing Topic Index](docs/testing-topic-index.md)** — Testing topics (200+ across 10 parts)
- **[Operations Topic Index](docs/operations-topic-index.md)** — Operations topics (60+ across 6 parts)
- **[Data Governance Topic Index](docs/data-governance-topic-index.md)** — Data governance topics (80+ across 6 parts)
- **[Analytics & Business Intelligence Topic Index](docs/analytics-bi-topic-index.md)** — Analytics topics (80+ across 6 parts)
- **[IAM Topic Index](docs/iam-topic-index.md)** — Identity and access management topics (100+ across 6 parts)
- **[ESB Topic Index](docs/esb-topic-index.md)** — ESB and event-driven architecture topics (160+ across 6 parts)
- **[Microservices Topic Index](docs/microservices-topic-index.md)** — Microservices and distributed systems topics (190+ across 6 parts)
- **[Cloud Topic Index](docs/cloud-topic-index.md)** — Cloud architecture topics (220+ across 6 parts)
- **[Cross-Reference Matrix](docs/cross-reference-matrix.md)** — Bidirectional specification mapping (430+ interconnections)
- **[API Reference](docs/api-reference.md)** — REST API specification
- **[Getting Started](docs/getting-started.md)** — Developer quick-start guide

Start with [`docs/README.md`](docs/README.md) for complete architecture, API, and
onboarding-flow documentation.

## Testing

See [`tests/README.md`](tests/README.md) for how backend, frontend, and
end-to-end tests are organized and run.
