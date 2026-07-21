from collections.abc import Generator

from sqlalchemy.orm import Session

from app.db.session import get_db

DbSession = Generator[Session, None, None]

__all__ = ["get_db"]
