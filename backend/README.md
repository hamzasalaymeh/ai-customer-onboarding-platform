# Backend

FastAPI service powering the onboarding API, data persistence, and AI
assistant orchestration.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
cp .env.example .env
```

## Run

```bash
uvicorn app.main:app --reload
```

API docs: http://localhost:8000/docs

## Test

```bash
pytest
```

## Layout

```
app/
├── main.py            FastAPI app factory / entry point
├── core/               Settings and logging configuration
├── api/                Routing (versioned under api/v1)
├── schemas/            Pydantic request/response models
├── services/            Business logic
├── models/             SQLAlchemy ORM models
└── db/                 Database session/engine setup
```
