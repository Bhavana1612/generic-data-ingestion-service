# Generic Data Ingestion Service

A generic and extensible **FastAPI-based Data Ingestion Service** that ingests data from external REST APIs and stores the collected data reliably.

This project was developed as part of the **Intentwise AI-Native Software Engineer Take-Home Assignment**.

The main goal is to build a reusable ingestion framework where adding a new API source does not require rewriting the application logic.

---

# Live Demo

## Hosted API

https://generic-data-ingestion-service-2m78.onrender.com

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

Different APIs may have different:

- Response formats
- Authentication mechanisms
- Pagination approaches
- Data structures

Building separate integrations for every API increases development and maintenance effort.

This project provides a generic ingestion pipeline that can connect with external APIs, process responses, and persist data without source-specific application changes.

---

# Solution Overview

The service accepts an external API endpoint and connector type.

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


The design separates source-specific logic from the main ingestion workflow.

---

# Features

## Core Features

- Generic REST API ingestion
- External API data fetching
- Connector-based architecture
- JSON API processing
- PostgreSQL persistence
- SQLAlchemy ORM integration
- FastAPI REST endpoints
- Swagger OpenAPI documentation
- Request validation using Pydantic
- Job tracking
- Record retrieval
- API error handling
- Timeout handling
- Docker database support

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

    -------------------------

    |                       |

    v                       v

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
7. Job details and stored records can be retrieved.

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

Used for APIs returning standard JSON responses.

Example:


simple_json


## Offset Pagination Connector

Used for APIs supporting offset and limit pagination.

Example:


offset_pagination


The connector design allows new authentication or pagination strategies to be added without modifying the ingestion workflow.

---

# API Documentation

## Health Check

Endpoint:


GET /health


Example:

```json
{
  "status": "healthy"
}
Ingest Data

Endpoint:

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

Endpoint:

GET /api/jobs

Returns all ingestion jobs.

Example:

{
  "jobs": [
    {
      "source_name": "dummyjson.com",
      "status": "completed",
      "record_count": 1
    }
  ]
}
Get Job Details

Endpoint:

GET /api/jobs/{job_id}

Returns information about a specific ingestion execution.

Get Stored Records

Endpoint:

GET /api/jobs/{job_id}/records

Returns records stored for a specific ingestion job.

Public APIs Used

The service is designed to support multiple external APIs through a connector-based architecture.

API 1: DummyJSON Products API

Endpoint:

https://dummyjson.com/products

Authentication:

None

Response:

JSON

Purpose:

Demonstrates ingestion of a simple public REST API.

Connector:

simple_json
API 2: Offset Pagination APIs

The service supports APIs that provide paginated responses.

Supported pagination style:

offset_pagination

Characteristics:

Offset based fetching
Limit based fetching
Multiple pages can be processed

The ingestion workflow remains unchanged when adding new sources.

Database Design

The application stores external API responses in PostgreSQL.

Records are stored using a flexible JSON payload approach.

Example structure:

Field	Description
id	Primary key
job_id	Related ingestion job
payload	JSON response data
created_at	Timestamp

Advantages:

Supports different API schemas
Avoids creating new tables for every API
Easier integration of new sources

Tradeoff:

Complex field queries require JSON operations.
Error Handling

The application handles:

Timeout Errors

External API request timeout.

Connection Errors

Unable to connect to external API.

Validation Errors

Missing or incorrect request fields.

Failures are handled without crashing the application.

Key Design Decisions
Generic Storage

Instead of creating API-specific database tables, raw API responses are stored as JSON.

Benefits:

Supports unknown API structures
Avoids database migrations
Makes adding new APIs easier
Connector Based Architecture

Source-specific processing is isolated inside connectors.

The core ingestion service does not contain API-specific logic.

Adding a new source requires:

Adding connector configuration
Adding a new strategy only if a new API pattern is introduced
Tradeoffs and Assumptions

Current assumptions:

APIs return JSON responses
Authentication strategies are limited
Large distributed processing is outside assignment scope
Database storage is the primary destination

Possible improvements:

OAuth authentication
More pagination strategies
Retry mechanism with exponential backoff
Background workers
S3 storage integration
Monitoring and metrics
Running Locally
Clone Repository
git clone https://github.com/Bhavana1612/generic-data-ingestion-service.git

Move into project:

cd generic-data-ingestion-service
Create Virtual Environment
python -m venv venv

Activate:

Windows:

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
Verification

The application was verified using:

✅ Render deployed endpoint
✅ Swagger API testing
✅ External API ingestion
✅ PostgreSQL persistence
✅ Invalid request validation
✅ Job retrieval APIs
✅ Record retrieval APIs

Testing

Tested scenarios:

Successful API ingestion
Invalid request validation
Database persistence
External API failures
Multiple ingestion requests

Run tests:

pytest
AI Tools Usage

AI tools were used during development for:

Debugging implementation issues
Reviewing architecture decisions
Improving documentation
Understanding backend best practices

All AI-generated suggestions were manually verified through:

Swagger API testing
Running the application locally
Checking database persistence

One issue identified during development:

An initial request schema mismatch caused HTTP 422 validation errors while testing the ingestion endpoint.

The issue was identified through Swagger API responses and fixed by aligning the request model with the API contract.

Repository

GitHub:

https://github.com/Bhavana1612/generic-data-ingestion-service

Author

Bhavana Kanasani

AI-Native Software Engineer Assignment
Intentwise
