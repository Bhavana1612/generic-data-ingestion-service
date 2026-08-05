# Generic Data Ingestion Service

A generic and extensible **FastAPI-based Data Ingestion Service** that fetches data from external REST APIs, processes the responses, and stores the ingested data in PostgreSQL.

This project was developed as part of the **Intentwise AI-Native Software Engineer Take-Home Assignment**.

The main goal of this project is to build a reusable ingestion framework where adding a new API source does not require rewriting the application.

---

# Live Demo

## Swagger Documentation

https://generic-data-ingestion-service-2m78.onrender.com/docs

## Health Endpoint

https://generic-data-ingestion-service-2m78.onrender.com/health

---

# Problem Statement

Modern applications frequently need to collect data from multiple external sources such as:

* E-commerce platforms
* Advertisement APIs
* Public datasets
* Business applications

Each external API may have different:

* Endpoints
* Response structures
* Authentication mechanisms
* Pagination approaches

Creating separate integrations for every API increases development effort and maintenance complexity.

The objective of this project is to design a common ingestion framework that can communicate with different API sources and store the collected data reliably.

---

# Solution Overview

The service accepts external API configurations as input and dynamically ingests data.

The application follows a connector-based architecture to keep API-specific logic separated from the core ingestion workflow.

## High-Level Architecture

```
                         Client
                            |
                            |
                            v

                    FastAPI API Layer

                            |
                            |
                            v

                 Ingestion Service Layer

                            |
                            |
                            v

                    Connector Factory

                 -------------------------
                 |                       |
                 v                       v

          JSON Connector          Future Connectors

                 |
                 |
                 v

              PostgreSQL Database
```

## Workflow

1. Client provides API endpoint configuration.
2. FastAPI validates incoming request.
3. Connector Factory selects the required connector.
4. Connector fetches data from external API.
5. Response data is normalized.
6. Data is persisted into PostgreSQL.
7. Ingestion result is returned.

The ingestion service remains independent of individual API implementations.

---

# Features

## Core Features

* Generic REST API ingestion
* Multiple external API support
* Connector-based architecture
* Dynamic endpoint handling
* JSON response processing
* PostgreSQL persistence
* SQLAlchemy ORM integration
* FastAPI REST APIs
* Swagger OpenAPI documentation
* Pydantic request validation
* Service layer architecture
* External API error handling
* Request timeout handling
* Database session management

---

# Technology Stack

## Backend

* Python 3.11
* FastAPI
* SQLAlchemy
* Pydantic
* HTTPX

## Database

* PostgreSQL

## Tools

* Docker
* Docker Compose
* Swagger UI
* Git
* GitHub
* Render

---

# Architecture Components

## API Layer

Location:

```
app/routes/ingest.py
```

Responsibilities:

* Accept ingestion requests
* Validate input data
* Trigger ingestion workflow
* Return API responses

---

## Service Layer

Location:

```
app/services/ingestion_service.py
```

Responsibilities:

* Execute ingestion workflow
* Communicate with connectors
* Process API responses
* Store data into database

The service layer keeps business logic separated from API routes.

---

## Connector Layer

Location:

```
app/connectors/
```

The connector layer provides extensibility for different API formats.

Base interface:

```
BaseConnector

    |
    |
    +-- fetch()

    +-- normalize()
```

Current implementation:

## JSON Connector

Location:

```
app/connectors/json_connector.py
```

Responsibilities:

* Fetch JSON responses from REST APIs
* Handle HTTP communication
* Normalize API responses

Future connectors can be added without modifying the ingestion service:

Examples:

* Authentication based APIs
* Pagination APIs
* CSV sources
* Cloud storage connectors

---

# Project Structure

```
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
│ │   └── ingest.py
│
│ ├── services
│ │   └── ingestion_service.py
│
│ ├── connectors
│ │   ├── base.py
│ │   ├── factory.py
│ │   └── json_connector.py
│
│ ├── storage
│ │   └── postgres.py
│
│ └── strategies
│     ├── auth.py
│     └── pagination.py
│
├── tests
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# Application Flow

## Step 1: Client Sends API Configuration

Example request:

```json
{
  "endpoints": [
    {
      "url": "https://dummyjson.com/products",
      "connector_type": "json"
    }
  ]
}
```

---

## Step 2: Request Validation

FastAPI validates the request using Pydantic models.

---

## Step 3: Connector Selection

Connector Factory selects the required connector based on:

```
connector_type
```

Example:

```
json  ---> JSONConnector
```

---

## Step 4: Data Fetching

The connector communicates with the external API and retrieves data.

---

## Step 5: Data Processing

The response is normalized into a consistent format.

---

## Step 6: Database Storage

Processed data is stored in PostgreSQL.

---

# Demo APIs Used

## 1. DummyJSON Products API

Endpoint:

```
https://dummyjson.com/products
```

Purpose:

Demonstrates ingestion of product JSON data.

---

## 2. JSONPlaceholder Users API

Endpoint:

```
https://jsonplaceholder.typicode.com/users
```

Purpose:

Demonstrates ingestion from a different JSON response structure.

---

# API Documentation

## Health Check

```
GET /health
```

---

## Ingest Data

```
POST /ingest/
```

Example Request:

```json
{
  "endpoints": [
    {
      "url": "https://dummyjson.com/products",
      "connector_type": "json"
    }
  ]
}
```

Example Response:

```json
{
  "message": "All API data ingested successfully",
  "saved_records": [
    12
  ]
}
```

This confirms:

* External API communication successful
* Connector execution successful
* Response processing completed
* PostgreSQL persistence successful

---

# Database Design

The application stores external API responses in PostgreSQL.

## Table Structure

| Field      | Description               |
| ---------- | ------------------------- |
| id         | Primary key               |
| name       | API source identifier     |
| data       | JSON response payload     |
| created_at | Record creation timestamp |

---

# Storage Strategy

External APIs can return different data structures.

Instead of creating separate tables for every API, JSON storage provides:

* Flexible schema handling
* Support for multiple API formats
* Reduced database migrations
* Easier future integration

---

# Error Handling

The application handles common external API failures.

## Timeout Handling

Example:

```
External API request timeout
```

## Connection Errors

Example:

```
Unable to connect to external API
```

## Invalid Responses

Example:

```
Invalid JSON response
```

These failures are handled without crashing the application.

---

# Design Decisions

## Generic Processing Workflow

The application avoids source-specific business logic.

Adding a new API source requires creating a new connector instead of modifying existing ingestion logic.

---

## Layered Architecture

The application separates:

* API routes
* Business logic
* Connector logic
* Database operations

Benefits:

* Cleaner code structure
* Easier debugging
* Better maintainability
* Future scalability

---

# Trade-offs

Due to the assignment timeline, some advanced features were intentionally limited.

Implemented:

* Generic ingestion workflow
* Connector architecture
* Database persistence
* API validation
* Error handling

Not implemented:

* Automatic authentication detection
* Advanced pagination strategies
* Background workers
* Retry queues
* Rate limiting

These features can be added without changing the core architecture.

---

# Future Improvements

Possible improvements:

* OAuth/API key authentication support
* Pagination connectors
* Retry mechanism with exponential backoff
* Rate limiting
* Background processing using Celery
* Scheduled ingestion jobs
* AWS S3/object storage support
* Database migrations using Alembic
* More automated testing

---

# Running Locally

## Clone Repository

```bash
git clone https://github.com/Bhavana1612/generic-data-ingestion-service.git
```

Move into project:

```bash
cd generic-data-ingestion-service
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start PostgreSQL

Using Docker:

```bash
docker compose up -d
```

---

## Run Application

```bash
uvicorn app.main:app --reload
```

Application:

```
http://127.0.0.1:8000
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

# Testing

The application was tested with:

* External API ingestion
* Database persistence
* Successful ingestion scenarios
* Invalid API URL handling
* External API failure scenarios

---

# AI Usage

AI tools were used during development for:

* Understanding backend architecture
* Debugging FastAPI and SQLAlchemy issues
* Reviewing design decisions
* Improving documentation

Example:

An initial approach considered storing complete API responses as a single JSON document.

After reviewing scalability concerns, the design was improved by separating connector logic and ingestion workflow.

All AI suggestions were manually verified using:

* Swagger testing
* Database validation
* Local execution

---

# Repository

GitHub:

https://github.com/Bhavana1612/generic-data-ingestion-service

---

# Author

**Bhavana Kanasani**

AI-Native Software Engineer Assignment
Intentwise
