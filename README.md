# Generic Data Ingestion Service

A generic and extensible **FastAPI-based Data Ingestion Service** that fetches data from external REST APIs, processes the responses, and stores the ingested data in PostgreSQL.

<<<<<<< HEAD
Generic Data Ingestion Service is a **config-driven FastAPI backend application** that ingests data from external API sources and persists it into PostgreSQL.

The goal of this project is to build a **generic, scalable, and extensible ingestion framework** where adding a new API source requires configuration changes instead of writing new integration code.

The ingestion engine dynamically handles:

* API connection
* Authentication strategy
* Pagination strategy
* Response processing
* Data persistence
=======
This project was developed as part of the **Intentwise AI-Native Software Engineer Take-Home Assignment**.

The main goal of this project is to build a reusable ingestion framework where adding a new API source does not require rewriting the application.

---

# Live Demo

## Swagger Documentation

https://generic-data-ingestion-service-2m78.onrender.com/docs

## Health Endpoint

https://generic-data-ingestion-service-2m78.onrender.com/health
>>>>>>> 99de8211a17ea9f1e9e28cc7f0c805f316484bb2

---

# Problem Statement

<<<<<<< HEAD
Modern applications often consume data from multiple external sources such as:

* Advertisement platforms
* E-commerce APIs
* Business applications
* Public datasets

Creating separate integrations for every API increases development effort and maintenance complexity.

This project provides a reusable ingestion framework where every source is described through configuration.

Adding a new source requires:

```
New API Source
      |
      v
Create Configuration File
      |
      v
Generic Ingestion Engine
      |
      v
Persist Data
```

No source-specific application code changes are required.
=======
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
>>>>>>> 99de8211a17ea9f1e9e28cc7f0c805f316484bb2

---

# Features

## Core Features

<<<<<<< HEAD
* Config-driven API ingestion
* Support for multiple external API sources
* Generic JSON API processing
* PostgreSQL persistence
* SQLAlchemy ORM integration
* FastAPI REST API
* Swagger OpenAPI documentation
* Modular architecture
* Docker-based database setup
* API timeout handling
* External API error handling
* Unit testing support
=======
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
>>>>>>> 99de8211a17ea9f1e9e28cc7f0c805f316484bb2

---

# Technology Stack

## Backend

<<<<<<< HEAD
* Python
=======
* Python 3.11
>>>>>>> 99de8211a17ea9f1e9e28cc7f0c805f316484bb2
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
<<<<<<< HEAD
=======
* Render
>>>>>>> 99de8211a17ea9f1e9e28cc7f0c805f316484bb2

---

# Architecture Components

<<<<<<< HEAD
The application follows a layered and strategy-based architecture.

```
                 Client Request
                       |
                       v
                FastAPI Routes
                       |
                       v
              Ingestion Service
                       |
        --------------------------------
        |              |               |
        v              v               v
   API Connector   Authentication   Pagination
     Strategy       Strategy        Strategy
        |
        v
   External API Source
        |
        v
 PostgreSQL Database
```
=======
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
>>>>>>> 99de8211a17ea9f1e9e28cc7f0c805f316484bb2

---

# Project Structure

```
generic-data-ingestion-service

│
├── app
│   │
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   │
│   ├── client
│   │   └── http_client.py
│   │
│   ├── config
│   │   └── loader.py
│   │
│   ├── connectors
│   │   ├── base.py
│   │   ├── factory.py
│   │   └── json_connector.py
│   │
│   ├── routes
│   │   └── ingest.py
│   │
│   ├── services
│   │   └── ingestion_service.py
│   │
│   ├── strategies
│   │   ├── auth.py
│   │   └── pagination.py
│   │
│   └── storage
│       └── postgres.py
│
├── configs
│   └── sample_source.yaml
│
<<<<<<< HEAD
├── tests
│   └── test_ingestion.py
│
├── Dockerfile
├── docker-compose.yml
=======
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
>>>>>>> 99de8211a17ea9f1e9e28cc7f0c805f316484bb2
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```
<<<<<<< HEAD

---

# Configuration Driven Sources

Each API source is defined using a configuration file.

Example:

`configs/sample_source.yaml`

```yaml
source_name: dummy_products

base_url: https://dummyjson.com

endpoint: /products

authentication:
  type: none

pagination:
  type: none

response:
  format: json
```

The ingestion engine reads this configuration and dynamically determines how to fetch and process data.

Adding a new API source requires creating a new configuration file instead of modifying application logic.
=======
>>>>>>> 99de8211a17ea9f1e9e28cc7f0c805f316484bb2

---

# Application Flow

<<<<<<< HEAD
1. User provides ingestion configuration.
2. FastAPI receives the ingestion request.
3. Configuration loader validates source details.
4. Connector factory selects the required API connector.
5. Authentication and pagination strategies are applied.
6. External API data is fetched.
7. Response data is processed.
8. Data is stored in PostgreSQL.
9. Saved record information is returned.

Flow:

```
Configuration
      |
      v
FastAPI Request
      |
      v
Ingestion Service
      |
      v
External API
      |
      v
Data Processing
      |
      v
PostgreSQL Storage
```
=======
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
>>>>>>> 99de8211a17ea9f1e9e28cc7f0c805f316484bb2

---

# Database Design

<<<<<<< HEAD
=======
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

>>>>>>> 99de8211a17ea9f1e9e28cc7f0c805f316484bb2
## Clone Repository

```bash
git clone https://github.com/Bhavana1612/generic-data-ingestion-service.git
```

<<<<<<< HEAD
=======
Move into project:

```bash
>>>>>>> 99de8211a17ea9f1e9e28cc7f0c805f316484bb2
cd generic-data-ingestion-service
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

<<<<<<< HEAD
### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
=======
Windows:

```bash
venv\Scripts\activate
>>>>>>> 99de8211a17ea9f1e9e28cc7f0c805f316484bb2
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

<<<<<<< HEAD
## Start PostgreSQL Database
=======
## Start PostgreSQL
>>>>>>> 99de8211a17ea9f1e9e28cc7f0c805f316484bb2

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
<<<<<<< HEAD

---

# API Usage

## Ingest Data
=======
>>>>>>> 99de8211a17ea9f1e9e28cc7f0c805f316484bb2

---

<<<<<<< HEAD
```
POST /ingest/
```

Request:

```json
{
  "endpoints": [
    "https://dummyjson.com/products",
    "https://jsonplaceholder.typicode.com/users"
  ]
}
```

Response:

```json
{
  "message": "All API data ingested successfully",
  "saved_records": [
    1,
    2
  ]
}
```

---

# Demo APIs Used

## DummyJSON Products API

```
https://dummyjson.com/products
```

Purpose:

* Demonstrates product data ingestion.

---

## JSONPlaceholder Users API

```
https://jsonplaceholder.typicode.com/users
```

Purpose:

* Demonstrates user data ingestion.

---

# Database Design

The application stores API responses in PostgreSQL using JSON storage.

| Field      | Description           |
| ---------- | --------------------- |
| id         | Primary key           |
| name       | API source name       |
| data       | JSON response payload |
| created_at | Timestamp             |

Using JSON storage allows different API structures without requiring database schema changes.

---

# Error Handling

The application handles:

## Timeout Errors

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

These mechanisms prevent external API failures from crashing the application.

---

# Design Decisions

## Generic API Processing

The application does not contain source-specific business logic.

Any compatible JSON API can be added through configuration.

---

## Service Layer Pattern

Business logic is separated from API routes.

Benefits:

* Cleaner code
* Better maintainability
* Easier testing
* Improved scalability

---

## Strategy-Based Design

Authentication and pagination are isolated using strategy components.

Benefits:

* Easy extension
* Reduced coupling
* Supports future API requirements

---

## Flexible Data Storage

API responses are stored as JSON.

Advantages:

* Supports different API formats
* Avoids frequent schema changes
* Allows future migration to object storage

---

# Trade-offs

Current assumptions:

* APIs return JSON responses
* Advanced authentication providers are not implemented
* Large-scale distributed processing is outside the assignment scope

These decisions focus on building a clean and extensible ingestion framework within the available timeline.

---

# Future Improvements

Possible enhancements:

* OAuth/API key authentication support
* Advanced pagination strategies
* Retry mechanism with exponential backoff
* Background ingestion jobs using Celery
* AWS S3 data storage
* Data validation pipelines
* Monitoring and logging dashboards
* Cloud deployment
* Improved integration testing

---

=======
>>>>>>> 99de8211a17ea9f1e9e28cc7f0c805f316484bb2
# Testing

The application was tested with:

<<<<<<< HEAD
* Multiple API endpoints
* Successful ingestion workflow
* Database persistence
* Invalid API URL handling
* External API failure scenarios

Run tests:

```bash
pytest
```

---

# AI Tools Usage

AI tools were used during development for:

* Debugging assistance
* Documentation improvement
* Exploring design alternatives

All suggestions were manually reviewed, tested, and validated before implementation.

---

=======
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

>>>>>>> 99de8211a17ea9f1e9e28cc7f0c805f316484bb2
# Repository

GitHub:

https://github.com/Bhavana1612/generic-data-ingestion-service

---
<<<<<<< HEAD

# Author

Bhavana Kanasani
=======

# Author

**Bhavana Kanasani**

AI-Native Software Engineer Assignment
Intentwise
>>>>>>> 99de8211a17ea9f1e9e28cc7f0c805f316484bb2
