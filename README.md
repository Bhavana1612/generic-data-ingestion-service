# Generic Data Ingestion Service

## Overview

Generic Data Ingestion Service is a **config-driven FastAPI backend application** that ingests data from external API sources and persists it into PostgreSQL.

The goal of this project is to build a **generic, scalable, and extensible ingestion framework** where adding a new API source requires configuration changes instead of writing new integration code.

The ingestion engine dynamically handles:

* API connection
* Authentication strategy
* Pagination strategy
* Response processing
* Data persistence

---

# Problem Statement

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

---

# Features

## Core Features

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

---

# Technology Stack

## Backend

* Python
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

---

# Architecture

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
├── tests
│   └── test_ingestion.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

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

---

# How It Works

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

---

# Setup Instructions

## Clone Repository

```bash
git clone https://github.com/Bhavana1612/generic-data-ingestion-service.git

cd generic-data-ingestion-service
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start PostgreSQL Database

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

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# API Usage

## Ingest Data

Endpoint:

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

# Testing

The application was tested with:

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

# Repository

GitHub:

https://github.com/Bhavana1612/generic-data-ingestion-service

---

# Author

Bhavana Kanasani
