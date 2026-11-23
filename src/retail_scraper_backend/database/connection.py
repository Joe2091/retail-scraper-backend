from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from retail_scraper_backend.core.config import settings


# Creates the connection to PostgreSQL
engine = create_engine(
    settings.database_url,
    echo=True,
)


# Creates database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# Base class for all database models
class Base(DeclarativeBase):
    pass