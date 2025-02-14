from fastapi import FastAPI
import sqlite3
from app.database import init_db  # Import the init_db function
from app.routes.workflow_routes import router as workflow_router
from app.routes.report_routes import router as report_router

# Initialize the database
init_db()

app = FastAPI()

# Include routers
app.include_router(workflow_router, prefix="/ingest", tags=["workflow"])
app.include_router(report_router, prefix="/report", tags=["reports"])

@app.get("/")
def read_root():
    return {"message": "Data Engineer Assessment API"}