from pydantic import BaseModel, validator

class WorkflowItem(BaseModel):
    id: str
    project: int
    team: str
    ts_start: int
    duration: int
    runner_id: int
    name: str
    success: int

    @validator('ts_start', pre=True)
    def parse_ts_start(cls, v):
        if isinstance(v, str):
            return int(v)
        return v

    @validator('success')
    def validate_success(cls, v):
        if v not in (0, 1):
            raise ValueError('success must be 0 or 1')
        return v