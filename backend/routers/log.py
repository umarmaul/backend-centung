from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
import uuid
from starlette import status

from ..models import Device, Log, Research
from .device import verify_device
from ..database import get_db

router = APIRouter(
    prefix="/log",
    tags=["log"],
)

class LogRequest(BaseModel):
    weight: float = Field(ge=0, le=1000)
    
class ResearchRequest(BaseModel):
    weight: float
    roll: float
    pitch: float

@router.post("/create-log", status_code=status.HTTP_201_CREATED)
async def create_log(
    log_data: LogRequest,
    db: Session = Depends(get_db),
    device: Device = Depends(verify_device)
):
    new_log = Log(id=uuid.uuid4(), device_id=device.id, weight=log_data.weight)
    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    return {"message": "Log created successfully", "data": new_log}

@router.post("/create-research", status_code=status.HTTP_201_CREATED)
async def create_research(
    research_data: ResearchRequest,
    db: Session = Depends(get_db),
    device: Device = Depends(verify_device)
):
    new_research = Research(
        id=uuid.uuid4(),
        device_id=device.id,
        weight=research_data.weight,
        roll=research_data.roll,
        pitch=research_data.pitch,
        weight_prediction=0
    )
    db.add(new_research)
    db.commit()
    db.refresh(new_research)

    return {"message": "Research created successfully", "data": new_research}

@router.get("/get-logs", status_code=status.HTTP_200_OK)
async def get_logs(
    db: Session = Depends(get_db),
    device: Device = Depends(verify_device)
):
    logs = db.query(Log).filter(Log.device_id == device.id).all()
    return {"data": logs}

@router.get("/get-research", status_code=status.HTTP_200_OK)
async def get_research(
    db: Session = Depends(get_db),
    device: Device = Depends(verify_device)
):
    researches = db.query(Research).filter(Research.device_id == device.id).all()
    return {"data": researches}