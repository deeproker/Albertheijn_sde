from fastapi import APIRouter, Query, HTTPException
from datetime import date
from app.services.report_service import get_weekly_cost, get_running_cost

router = APIRouter()

@router.get("/weekly-cost")
async def weekly_cost():
    return get_weekly_cost()

@router.get("/running-cost")
async def running_cost(
    start_date: str = Query(..., description="Start date in YYYY-MM-DD format"),
    end_date: str = Query(..., description="End date in YYYY-MM-DD format")
):
    try:
        start = date.fromisoformat(start_date)
        end = date.fromisoformat(end_date)
    except ValueError:
        raise HTTPException(400, detail="Invalid date format. Use YYYY-MM-DD.")
    if start > end:
        raise HTTPException(400, detail="Start date must be before end date.")
    return get_running_cost(start, end)