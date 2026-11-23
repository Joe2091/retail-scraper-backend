from collections.abc import Generator

from sqlalchemy.orm import Session

from retail_scraper_backend.database.connection import SessionLocal


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()