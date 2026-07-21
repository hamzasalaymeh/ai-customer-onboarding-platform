# API Reference

Base URL: `/api/v1`

Interactive docs are also served by the running backend at `/docs`
(Swagger UI) and `/redoc`.

## Health

| Method | Path       | Description                 |
|--------|------------|------------------------------|
| GET    | `/health`  | Liveness/readiness check.   |

## Customers

| Method | Path                 | Description                    |
|--------|----------------------|---------------------------------|
| GET    | `/customers`         | List customers.                |
| POST   | `/customers`         | Create a customer record.      |
| GET    | `/customers/{id}`    | Fetch a single customer.       |

## Onboarding

| Method | Path                                          | Description                              |
|--------|------------------------------------------------|-------------------------------------------|
| GET    | `/onboarding/{customer_id}`                    | Get current onboarding status and steps. |
| POST   | `/onboarding/{customer_id}/steps/{step_id}`    | Submit data for an onboarding step.      |

## AI Assistant

| Method | Path              | Description                                   |
|--------|-------------------|-------------------------------------------------|
| POST   | `/ai/chat`        | Send a message to the onboarding assistant.    |

Request bodies and response schemas are defined in `backend/app/schemas/`
and are the source of truth; this document is a summary.
