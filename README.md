# Generic Data Ingestion Service

## Overview

Generic Data Ingestion Service is a FastAPI-based backend application designed to ingest data from external API sources and store the collected information in PostgreSQL.

The goal of this project is to build a **generic and extensible ingestion pipeline** where new API sources can be added with minimal changes instead of creating separate integrations for every source.

The service accepts API endpoints as input, fetches data dynamically, processes the response, and persists the collected data into a database.

---

# Problem Statement

Modern applications often collect data from multiple external sources such as:

* E-commerce APIs
* Advertisement platforms
* Public APIs
* Business data providers

Building individual integrations for every source increases development and maintenance effort.

This project provides a reusable ingestion framework:

```
External API Sources
          |
          v
FastAPI Ingestion Service
          |
          v
PostgreSQL Database
```

---

# Features

## Core Features

* Accept one or multiple external API endpoints
* Dynamically fetch JSON data from APIs
* Store API responses in PostgreSQL
* Generic ingestion workflow
* FastAPI REST API implementation
* Swagger/OpenAPI documentation
* SQLAlchemy ORM integration
* Service layer architecture
* Database persistence
* External API error handling
* Request timeout handling

---

# Technology Stack

## Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic

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
        ------------------------
        |                      |
        v                      v

 External API Calls       Data Processing
                   |
                   v

          PostgreSQL Storage
```

---

# Architecture Components

## Routes Layer

Location:

```
app/routes/ingest.py
```

Responsibilities:

* Receive ingestion requests
* Validate incoming data
* Return API responses

---

## Service Layer

Location:

```
app/services/ingestion_service.py
```

Responsibilities:

* Execute ingestion workflow
* Call external APIs
* Process API responses
* Store data into database

---

## Database Layer

Location:

```
app/database.py
```

Responsibilities:

* Database connection management
* SQLAlchemy session handling

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
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# How It Works

1. User provides one or more API endpoints.

2. FastAPI receives the ingestion request.

3. The ingestion service calls the configured external APIs.

4. API responses are collected.

5. Data is stored in PostgreSQL.

6. The service returns ingestion status and saved record information.

Example flow:

```
User Request

      |
      v

POST /ingest/

      |
      v

Fetch External API Data

      |
      v

Store Response

      |
      v

Return Result
```

---

# Setup Instructions

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

Windows PowerShell:

```bash
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

# API Documentation

## Ingest External Data

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

## API 1: DummyJSON Products API

Endpoint:

```
https://dummyjson.com/products
```

Purpose:

* Demonstrates product data ingestion
* Validates handling of product-based JSON responses

---

## API 2: JSONPlaceholder Users API

Endpoint:

```
https://jsonplaceholder.typicode.com/users
```

Purpose:

* Demonstrates ingestion of user-based JSON responses
* Shows support for different JSON structures

---

# Database Design

External API responses are stored in PostgreSQL.

Table fields:

| Field      | Description               |
| ---------- | ------------------------- |
| id         | Primary key               |
| name       | API source name           |
| data       | JSON response data        |
| created_at | Record creation timestamp |

JSON storage was selected because different APIs can return different structures. This avoids frequent database schema changes when adding new sources.

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

## Invalid JSON Responses

Example:

```
Invalid API response format
```

These checks prevent external API failures from crashing the application.

---

# Design Decisions

## Generic API Processing

The application does not contain source-specific business logic.

Any JSON-based API endpoint can be provided as input.

---

## Service Layer Pattern

Business logic is separated from API routes.

Benefits:

* Cleaner code structure
* Easier maintenance
* Better scalability

---

## Flexible Data Storage

API responses are stored as JSON.

Advantages:

* Supports different API formats
* Avoids frequent schema changes
* Allows future migration to other storage systems such as object storage

---

# Trade-offs and Assumptions

Current assumptions:

* APIs return JSON responses
* Authentication mechanisms are not implemented in the current version
* Advanced pagination support is limited

These decisions were made to focus on building a flexible ingestion framework within the assignment timeline.

---

# Future Improvements

Possible improvements:

* API authentication support
* Advanced pagination strategies
* Retry mechanism with exponential backoff
* Background processing using Celery
* AWS S3/object storage support
* Data validation improvements
* Unit and integration testing
* Cloud deployment

---

# Testing

The application was tested with:

* Multiple API endpoint ingestion
* Successful data retrieval
* PostgreSQL persistence
* Invalid API URL scenarios
* External API failure scenarios

---

# AI Tools Usage

AI tools were used during development for:

* Debugging implementation issues
* Reviewing architecture decisions
* Improving documentation
* Understanding backend concepts

One example:

During development, AI suggested a possible cause for an API failure. The suggestion was verified by checking FastAPI logs, testing through Swagger UI, and validating PostgreSQL records before applying the correct fix.

All AI-generated suggestions were reviewed, tested, and modified before integration.

---

# Repository

GitHub:

https://github.com/Bhavana1612/generic-data-ingestion-service

---

# Author

Bhavana Kanasani
