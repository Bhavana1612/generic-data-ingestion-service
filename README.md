# Generic Data Ingestion Service

A generic and extensible **FastAPI-based Data Ingestion Service** that fetches data from external REST APIs and stores the ingested data in PostgreSQL.

This project was developed as part of the **Intentwise AI-Native Software Engineer Take-Home Assignment**.

The main objective of this project is to design a reusable ingestion pipeline that can work with different API sources without creating separate implementations for every data source.

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

Each external API can have different:

* Endpoints
* Response formats
* Data structures
* Authentication methods
* Pagination approaches

Building separate integrations for every API increases development effort and maintenance complexity.

The goal of this project is to create a common ingestion framework that can fetch data from different API sources and store it reliably.

---

# Solution Overview

The service accepts one or more external API endpoints as input.

The ingestion workflow:

```
External API Sources
          |
          v
FastAPI Ingestion Service
          |
          v
Data Processing Layer
          |
          v
PostgreSQL Database
```

The application:

1. Receives API endpoint details.
2. Fetches data from external APIs.
3. Processes the received JSON response.
4. Stores the data in PostgreSQL.
5. Returns ingestion status and stored information.

---

# Features

## Core Features

* Generic API ingestion workflow
* Support for multiple REST API sources
* Dynamic endpoint handling
* JSON response processing
* PostgreSQL data persistence
* FastAPI REST APIs
* Interactive Swagger documentation
* SQLAlchemy ORM integration
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

# Architecture

The application follows a layered backend architecture.

```
                         Client
                            |
                            v

                    FastAPI Routes

                            |
                            v

                 Ingestion Service Layer

                            |
             --------------------------------
             |                              |
             v                              v

       External API Client            Error Handling

             |
             v

        Data Processing Layer

             |
             v

        PostgreSQL Database
```

---

# Application Components

## API Layer

Location:

```
app/routes/ingest.py
```

Responsibilities:

* Accept ingestion requests
* Validate request data
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
* Communicate with external APIs
* Process API responses
* Store data into database

Keeping business logic separate from routes improves maintainability and scalability.

---

## Database Layer

Location:

```
app/database.py
```

Responsibilities:

* Manage PostgreSQL connection
* Create database sessions
* Handle database operations using SQLAlchemy ORM

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
│ └── services
│     └── ingestion_service.py
│
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

# Application Flow

## Step 1: Client Sends API Endpoint

The client provides one or more external API URLs.

Example:

```json
{
  "endpoints": [
    "https://dummyjson.com/products"
  ]
}
```

---

## Step 2: FastAPI Receives Request

The API layer validates the incoming request using Pydantic models.

---

## Step 3: Fetch External Data

The ingestion service uses HTTP requests to communicate with external APIs.

---

## Step 4: Process Response

The received JSON response is validated and prepared before storage.

---

## Step 5: Store Data

The processed information is stored in PostgreSQL.

---

## Step 6: Return Response

The API returns ingestion status and saved record information.

---

# Demo APIs Used

## 1. DummyJSON Products API

Endpoint:

```
https://dummyjson.com/products
```

Purpose:

Demonstrates ingestion of product-related JSON data.

---

## 2. JSONPlaceholder Users API

Endpoint:

```
https://jsonplaceholder.typicode.com/users
```

Purpose:

Demonstrates ingestion of a different JSON response structure.

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
    "https://dummyjson.com/products",
    "https://jsonplaceholder.typicode.com/users"
  ]
}
```

Example Response:

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

# Database Design

The application stores external API responses in PostgreSQL.

Example structure:

| Field      | Description               |
| ---------- | ------------------------- |
| id         | Primary key               |
| source     | API source name           |
| data       | JSON response payload     |
| created_at | Record creation timestamp |

---

# Why JSON Storage?

External APIs can return different data structures.

Instead of creating separate database tables for every API, JSON storage provides:

* Flexible schema handling
* Support for multiple API formats
* Reduced database migrations
* Easier future integration with new sources

---

# Error Handling

The application handles common external API failures.

## Timeout Handling

Handles cases where an API does not respond within the expected time.

Example:

```
External API request timeout
```

---

## Connection Errors

Handles unavailable external services.

Example:

```
Unable to connect to external API
```

---

## Invalid Responses

Handles invalid or unexpected API responses.

Example:

```
Invalid JSON response
```

---

# Design Decisions

## Generic Processing Workflow

The application avoids source-specific business logic.

The ingestion workflow remains independent from individual API sources.

---

## Layered Architecture

The application separates:

* API routes
* Business logic
* Database operations

Benefits:

* Cleaner code structure
* Easier debugging
* Better maintainability
* Future scalability

---

## Flexible Storage Strategy

JSON-based storage was selected because external APIs can have different schemas.

This allows adding new API sources without frequent database redesign.

---

# Trade-offs

Due to the assignment timeline, the following decisions were made:

* Authentication support is not implemented.
* Advanced pagination handling is not implemented.
* Background processing is not implemented.
* APIs are assumed to return JSON responses.
* Ingestion runs synchronously.

These decisions keep the implementation focused while maintaining a scalable foundation.

---

# Future Improvements

Possible improvements:

* API authentication strategies
* Pagination support
* Retry mechanism with exponential backoff
* Rate limiting
* Background jobs using Celery
* Scheduled ingestion jobs
* AWS S3/object storage support
* Cloud scalability improvements
* Automated integration testing

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

## Start Application

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

* Multiple external API endpoints
* Successful ingestion scenarios
* Database persistence validation
* Invalid API URL handling
* External API failure scenarios

---

# AI Usage

AI tools were used during development for:

* Understanding backend architecture
* Debugging FastAPI and SQLAlchemy issues
* Reviewing implementation decisions
* Improving documentation

Example:

During development, an AI suggestion was reviewed and modified after testing because the initial approach did not provide the required scalability.

The final implementation decisions were verified through:

* Local testing
* API testing using Swagger
* Database validation

All AI-generated suggestions were reviewed before integration.

---

# Repository

GitHub:

https://github.com/Bhavana1612/generic-data-ingestion-service

---

# Author

**Bhavana Kanasani**

AI-Native Software Engineer Assignment
Intentwise
