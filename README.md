# Generic Data Ingestion Service

A generic and extensible **FastAPI-based Data Ingestion Service** that ingests data from external REST APIs and stores the collected data in PostgreSQL.

This project was developed as part of the **Intentwise AI-Native Software Engineer Take-Home Assignment**.

The goal of this project is to build a reusable ingestion framework where adding a new API source does not require rewriting the application logic.

---

# Live Demo

## Swagger API Documentation

https://generic-data-ingestion-service-2m78.onrender.com/docs

## Health Check

https://generic-data-ingestion-service-2m78.onrender.com/health

---

# Problem Statement

Modern applications need to collect data from multiple external sources such as:

- E-commerce APIs
- Advertisement platforms
- Business applications
- Public datasets

Each external API may have different:

- Endpoints
- Response formats
- Authentication mechanisms
- Pagination approaches

Creating separate integrations for every API increases development effort and maintenance complexity.

This project provides a generic ingestion pipeline that can connect with different APIs and store the received data reliably.

---

# Solution Overview

The service accepts an API URL and connector type from the client.

The ingestion workflow:


Client Request
|
v
FastAPI API Layer
|
v
Ingestion Service
|
v
Connector Strategy
|
v
External API
|
v
PostgreSQL Database


The design keeps source-specific logic separated from the core ingestion workflow.

---

# Features

## Core Features

- Generic REST API ingestion
- Multiple API source support
- Connector-based architecture
- JSON API processing
- PostgreSQL persistence
- SQLAlchemy ORM integration
- FastAPI REST APIs
- Swagger OpenAPI documentation
- Pydantic request validation
- Service layer architecture
- Job tracking
- Record retrieval
- API timeout handling
- External API error handling
- Docker database setup

---

# Technology Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- HTTPX

## Database

- PostgreSQL

## Tools

- Docker
- Docker Compose
- Swagger UI
- Git
- GitHub
- Render

---

# Architecture

The application follows a layered architecture:

             Client
               |
               v

          FastAPI Routes

               |
               v

      Ingestion Service Layer

               |
      ---------------------
      |                   |
      v                   v

Connector Strategy PostgreSQL Storage

      |
      v

External API Source


---

# Project Structure


generic-data-ingestion-service

│
├── app
│ │
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ │
│ ├── client
│ │ └── http_client.py
│ │
│ ├── config
│ │ └── loader.py
│ │
│ ├── connectors
│ │ ├── base.py
│ │ ├── factory.py
│ │ └── json_connector.py
│ │
│ ├── routes
│ │ └── ingest.py
│ │
│ ├── services
│ │ └── ingestion_service.py
│ │
│ ├── strategies
│ │ ├── auth.py
│ │ └── pagination.py
│ │
│ └── storage
│ └── postgres.py
│
├── tests
│ └── test_ingestion.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


---

# How It Works

1. Client provides API URL and connector type.
2. FastAPI validates the request.
3. Connector strategy is selected.
4. External API data is fetched.
5. Response data is processed.
6. Data is stored in PostgreSQL.
7. Job details and records can be retrieved.

Flow:


POST Request

  |
  v

Validate Input

  |
  v

Select Connector

  |
  v

Fetch External Data

  |
  v

Store Records

  |
  v

Return Job Information


---

# Supported Connector Types

## Simple JSON Connector

Used for APIs returning normal JSON responses.

Example:


simple_json


## Offset Pagination Connector

Used for APIs supporting offset pagination.

Example:


offset_pagination


---

# API Documentation

## Health Check

### Endpoint


GET /health


Example Response:

```json
{
  "status": "healthy"
}
Ingest Data
Endpoint
POST /api/ingest

Request:

{
  "url": "https://dummyjson.com/products",
  "connector_type": "simple_json"
}

Response:

{
  "id": "3b872983-4f2b-42c1-8d64-3c280bdff21f",
  "source": "dummyjson.com",
  "records_ingested": 1
}
Get Jobs
Endpoint
GET /api/jobs

Returns all ingestion jobs.

Example:

{
  "jobs": [
    {
      "id": "job-id",
      "source_name": "dummyjson.com",
      "source_url": "https://dummyjson.com/products",
      "status": "completed",
      "record_count": 1
    }
  ]
}
Get Job Details
Endpoint
GET /api/jobs/{job_id}

Returns information about a specific ingestion job.

Get Stored Records
Endpoint
GET /api/jobs/{job_id}/records

Returns the records stored for the selected ingestion job.

Demo API Used
DummyJSON Products API

Endpoint:

https://dummyjson.com/products

Purpose:

Demonstrates ingestion of external JSON product data.

Database Design

The application stores API responses in PostgreSQL.

Field	Description
id	Primary key
job_id	Related ingestion job
payload	JSON response data
created_at	Timestamp

JSON storage allows different API response structures without database schema changes.

Error Handling

The application handles:

Timeout Errors
External API request timeout
Connection Errors
Unable to connect to external API
Validation Errors
Missing required fields

Failures are handled without crashing the application.

Design Decisions
Generic Processing

The application avoids source-specific business logic.

New API sources can be supported by adding connector implementations instead of changing the ingestion workflow.

Service Layer Pattern

Business logic is separated from API routes.

Benefits:

Cleaner code
Easier maintenance
Better testing
Improved scalability
Flexible Data Storage

API responses are stored as JSON.

Advantages:

Supports different API structures
Avoids frequent schema changes
Easier future migration to object storage
Trade-offs

Current assumptions:

APIs return JSON responses
Advanced authentication providers are not implemented
Large-scale distributed processing is outside the assignment scope
Future Improvements

Possible enhancements:

OAuth/API key authentication
Advanced pagination strategies
Retry mechanism with exponential backoff
Rate limiting
Background jobs using Celery
Scheduled ingestion
AWS S3 integration
Monitoring and logging
Improved integration testing
Running Locally
Clone Repository
git clone https://github.com/Bhavana1612/generic-data-ingestion-service.git

Move into project:

cd generic-data-ingestion-service
Create Virtual Environment
python -m venv venv

Activate:

Windows PowerShell:

.\venv\Scripts\Activate.ps1
Install Dependencies
pip install -r requirements.txt
Start PostgreSQL

Using Docker:

docker compose up -d
Run Application
uvicorn app.main:app --reload

Application:

http://127.0.0.1:8000

Swagger:

http://127.0.0.1:8000/docs
Testing

The application was tested with:

Successful API ingestion
Multiple API requests
Database persistence
Invalid URL handling
Validation failures
External API errors

Run tests:

pytest
AI Tools Usage

AI tools were used during development for:

Debugging assistance
Architecture discussions
Documentation improvement
Understanding backend best practices

All suggestions were manually verified through:

Swagger testing
API validation
Database checks
Local execution
Repository

GitHub:

https://github.com/Bhavana1612/generic-data-ingestion-service

Author

Bhavana Kanasani

AI-Native Software Engineer Assignment
Intentwise
