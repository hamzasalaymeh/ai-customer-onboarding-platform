# Getting Started

## Prerequisites

- Python 3.11+
- Node.js 20+
- Docker and Docker Compose (optional, for containerized runs)

## Option A: Docker Compose (recommended)

```bash
cp backend/.env.example backend/.env
cp frontend/.env.example frontend/.env
docker compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml up --build
```

## Option B: Run services locally

### Backend

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
cp .env.example .env
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
cp .env.example .env
npm run dev
```

## Running tests

```bash
# Backend
cd backend && pytest

# Frontend
cd frontend && npm run test

# End-to-end
cd tests/e2e && npm install && npm run test
```
