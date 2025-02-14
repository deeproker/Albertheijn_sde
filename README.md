# Albertheijn Project

Similar project was done to capture the Pyspark logs (Running on Databricks) using below flow in my current project:

Databricks Jobs (Instrumentation of OTEL Call) -- > Opentelemetry POD Running on Openshift Cluster -- > Splunk (Logs , Traces and Metrics)
For centralised Observability using Splunks Visualization

## Further Enhancement in Current API Call -- > Perform Server side Caching capabilities for last 30 min (Already queried workflows runs) to save cost and improve performance of API.

## Manage the API in a API Gateway for security and balance the traffic using Load balancer traffic towards it.

# FastAPI Workflow Management Application

## Overview

This is a FastAPI application designed for managing workflows. The application allows teams to ingest workflow data, generate reports on workflow costs, and track metrics using a SQLite database. 

## Features

- Ingest workflow data via a RESTful API.
- Generate weekly cost reports for workflows executed by each team.
- Calculate running total costs between specified dates.
- Simple and efficient design with a focus on clean architecture and testability.

## Technologies Used

- Python 3.9+
- FastAPI
- SQLite (or any other SQL database)
- Pydantic for data validation
- Docker for containerization

## Prerequisites

Before you begin, ensure you have the following installed:

- [Python 3.9 or higher](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started) (optional, if you wish to run the app in a container)

## Installation

pip install -r app/requirements.txt

## Folder Structure

├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── workflow.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── workflow_service.py
│   │   └── report_service.py
│   └── routes/
│       ├── __init__.py
│       └── workflow_routes.py
├── tests/
│   ├── __init__.py
│   ├── test_workflow.py
│   └── test_reports.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml

## Ways to start App 

## Option 1: 

uvicorn app.main:app --reload
App will be reachable at http://127.0.0.1:8000

## Option 2:
docker-compose up --build 

## Testing API 

Step 1: 

curl -X POST "http://127.0.0.1:8000/ingest/workflow" -H "Content-Type: application/json" -d '[
  {
    "id": "16081779-b239-4b9e-a61b-2f4d8f202667",
    "project": 1,
    "team": "team-1",
    "ts_start": 1735689661,
    "duration": 62,
    "runner_id": 3,
    "name": "BUILD",
    "success": 1
  }
]'
{"message":"Inserted 1 workflows"}

Step 2:

curl "http://127.0.0.1:8000/report/weekly-cost"                                               
[{"team":"team-1","week":"2025-00","total_cost":0.004}]% 

Step 3:

curl "http://127.0.0.1:8000/report/running-cost?start_date=2025-01-01&end_date=2025-01-03"    
[{"date":"2025-01-01","running_total":0.004},{"date":"2025-01-02","running_total":0.004},{"date":"2025-01-03","running_total":0.004}]% 

## Unittest

python -m unittest discover -s tests
