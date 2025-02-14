from fastapi import APIRouter, HTTPException
from app.models.workflow import WorkflowItem
from app.services.workflow_service import insert_workflows

router = APIRouter()

@router.post("/workflow")
async def ingest_workflow(workflows: list[WorkflowItem]):
    try:
        insert_workflows(workflows)
        return {"message": f"Inserted {len(workflows)} workflows"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))