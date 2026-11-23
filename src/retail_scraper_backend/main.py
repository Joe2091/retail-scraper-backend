from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from retail_scraper_backend.database.session import get_db

app = FastAPI(
    title="RetailTracker API",
    description="Track product prices and stock across retailers",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Welcome to RetailTracker API"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/health/database")
def database_health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))

    return {
        "status": "connected",
        "database": "PostgreSQL",
    }