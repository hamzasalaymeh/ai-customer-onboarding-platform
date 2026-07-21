# Tests

- `backend/` — pytest tests for the FastAPI backend (also runnable via
  `pytest` from within `backend/`, since `backend/pyproject.toml` includes
  this directory in `testpaths`).
- `e2e/` — end-to-end tests exercising the deployed frontend + backend
  together.

Frontend unit tests live alongside their components under
`frontend/src/**/*.test.tsx` and run via `npm run test` in `frontend/`.

## Running

```bash
# Backend unit/integration tests
cd backend && pytest

# End-to-end tests
cd tests/e2e && npm install && npm run test
```
