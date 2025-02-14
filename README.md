# Albertheijn_sde
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

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
