
from fastapi import FastAPI

app = FastAPI(
    title="RetailTracker API",
    description="Track product prices and stock across retailers",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to RetailTracker API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
