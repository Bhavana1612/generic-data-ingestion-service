# Generic Data Ingestion Service

## Overview

Generic Data Ingestion Service is a FastAPI-based backend application that can ingest data from multiple external API sources and store the collected data in a PostgreSQL database.

The main objective of this project is to create a **generic, scalable, and extensible data ingestion pipeline** where adding a new API source does not require rewriting the application.

The service accepts one or more API endpoints as input, dynamically fetches data, processes the response, and persists the information into a database.

---

# Problem Statement

Modern applications often need to collect data from different external sources such as:

- E-commerce APIs
- Advertisement platforms
- Public datasets
- Business APIs

Building separate integrations for every source increases maintenance complexity.

This project provides a common ingestion framework:


External API Sources
|
|
v
FastAPI Ingestion Service
|
|
v
PostgreSQL Database


---

# Features

## Core Features

- Accept one or multiple external API endpoints
- Dynamically fetch data from APIs
- Store API responses in PostgreSQL
- Generic ingestion workflow
- FastAPI REST APIs
- Swagger OpenAPI documentation
- Dockerized database setup
- SQLAlchemy ORM integration
- Service layer architecture
- API timeout handling
- External API error handling


---

# Technology Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic

## Database

- PostgreSQL

## Tools

- Docker
- Docker Compose
- Swagger UI
- Git
- GitHub


---

# Architecture

The application follows a layered backend architecture.

          Client
             |
             |
             v

      FastAPI Routes

             |

             v

   Ingestion Service Layer

             |

    ------------------

    |                |

    v                v

External APIs Data Processing

             |

             v

      PostgreSQL Database


## Architecture Components


### Routes Layer

Location:


app/routes/ingest.py


Responsibilities:

- Receive API requests
- Validate input
- Return responses


### Service Layer

Location:


app/services/ingestion_service.py


Responsibilities:

- Fetch external API data
- Handle failures
- Store data into database


### Database Layer

Location:


app/database.py


Responsibilities:

- Database connection
- SQLAlchemy session management


---

# Project Structure


generic-data-ingestion-service

│
├── app
│
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│
│ ├── routes
│ │ └── ingest.py
│
│ └── services
│ └── ingestion_service.py
│
├── docker-compose.yml
├── requirements.txt
└── README.md



---

# How It Works


1. User provides one or more API endpoints.

2. FastAPI receives the ingestion request.

3. The ingestion service calls external APIs.

4. API responses are collected.

5. Data is stored in PostgreSQL.

6. Saved record IDs are returned to the client.


Example flow:


User Request
|
v
POST /ingest/
|
v
Fetch External API Data
|
v
Save Data
|
v
Return Database IDs



---

# Setup Instructions


## Clone Repository

```bash
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
Start PostgreSQL Database

Using Docker:

docker compose up -d
Run Application
uvicorn app.main:app --reload

Application:

http://127.0.0.1:8000

Swagger Documentation:

http://127.0.0.1:8000/docs
API Documentation
Ingest External Data

Endpoint:

POST /ingest/

Request:

{
  "endpoints": [
    "https://dummyjson.com/products",
    "https://jsonplaceholder.typicode.com/users"
  ]
}

Response:

{
  "message": "All API data ingested successfully",
  "saved_records": [
    1,
    2
  ]
}
Demo APIs Used
API 1

DummyJSON Products API

https://dummyjson.com/products

Purpose:

Demonstrates product data ingestion.

API 2

JSONPlaceholder Users API

https://jsonplaceholder.typicode.com/users

Purpose:

Demonstrates user data ingestion.

Database Design

The application stores external API responses in PostgreSQL.

Fields:

Field	Description
id	Primary key
name	API source name
data	JSON response
created_at	Timestamp

JSON storage allows different API structures without changing database schema.

Error Handling

The application handles:

Timeout Errors

Example:

Request timeout
Connection Errors

Example:

Unable to connect to external API
Invalid JSON Responses

Example:

Invalid JSON response

This prevents failures from crashing the application.

Design Decisions
Generic API Processing

The application does not contain source-specific logic.

Any JSON API endpoint can be provided as input.

Service Layer Pattern

Business logic is separated from routes.

Benefits:

Cleaner code
Easier maintenance
Better scalability
Flexible Data Storage

JSON responses are stored directly.

Advantages:

Supports different API formats
Avoids schema changes
Easier future migration to object storage
Trade-offs

Current assumptions:

APIs return JSON responses
Authentication is not implemented
Pagination handling is limited

These decisions were made to focus on building a flexible ingestion framework within the assignment timeline.

Future Improvements

Possible improvements:

API authentication support
Pagination support
Retry mechanism
Background jobs using Celery
AWS S3 object storage support
Data validation improvements
Unit and integration tests
Cloud deployment
Testing

The application was tested with:

Multiple API endpoints
Successful ingestion flow
Database persistence
Invalid API URL handling
External API failure scenarios
AI Tools Usage

AI tools were used during development for:

Debugging errors
Reviewing architecture decisions
Improving documentation
Understanding backend best practices

One incorrect AI suggestion was related to identifying the cause of an API failure.

The suggestion was verified by:

Checking FastAPI logs
Testing through Swagger
Validating PostgreSQL records

The final implementation was manually tested and verified.

Repository

GitHub:

https://github.com/Bhavana1612/generic-data-ingestion-service

Author

Bhavana Kanasani


After pasting:

Run:

```powershell
git status

Then send me the output. We will commit and push the README.
## AI Usage

AI tools were used during development for:
- Designing the ingestion service architecture
- Debugging FastAPI, SQLAlchemy, Docker, and deployment issues
- Improving documentation

One example:
During development, AI suggested an initial approach that did not fully match the production deployment requirements. I verified the behavior by testing locally and on Render, then corrected the implementation using environment-based configuration.

All AI-generated suggestions were reviewed, tested, and modified before integration.
