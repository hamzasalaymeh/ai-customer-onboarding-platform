# Docker

Compose files that orchestrate the backend and frontend containers.

- `docker-compose.yml` — base service definitions.
- `docker-compose.dev.yml` — development overrides (hot reload, bind mounts).

## Local development

```bash
cp ../backend/.env.example ../backend/.env
cp ../frontend/.env.example ../frontend/.env
docker compose -f docker-compose.yml -f docker-compose.dev.yml up --build
```

## Production-like run

```bash
docker compose -f docker-compose.yml up --build
```
