from fastapi import FastAPI
from app.routes import ingest

from app.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Generic Data Ingestion Service",
    description="A generic API ingestion and storage service",
    version="1.0"
)

# Include routes
app.include_router(ingest.router)


@app.get("/")
def home():
    return {
        "message": "Generic Data Ingestion Service is running"
    }