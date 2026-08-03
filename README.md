# Generic Data Ingestion Service

A FastAPI based data ingestion and storage service.

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Swagger OpenAPI

## Run Project

Start PostgreSQL:

docker compose up -d

Activate environment:

.\venv\Scripts\Activate.ps1

Run API:

uvicorn app.main:app --reload

Swagger:

http://127.0.0.1:8000/docs

## APIs

POST /ingest/
- Accepts JSON data
- Stores ingestion records

GET /ingest/
- Fetches ingested data
