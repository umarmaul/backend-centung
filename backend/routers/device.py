from pydantic import BaseModel, Field
from fastapi import APIRouter, Header, Depends, HTTPException
from sqlalchemy.orm import Session
from hashlib import sha256
from starlette import status

from ..database import get_db
from ..models import Device

router = APIRouter(
    prefix="/device",
    tags=["device"],
)

class DeviceRegistration(BaseModel):
    device_name: str = Field(min_length=1, max_length=20)
    device_password: str = Field(min_length=3, max_length=20)
    type: str = Field(min_length=1, max_length=20)
    firmware_version: str = Field(min_length=1, max_length=10)
    status: bool

def verify_device(
    db: Session = Depends(get_db),
    x_device_name: str = Header(...),
    x_device_password: str = Header(...)
):
    device = db.query(Device).filter(Device.device_name == x_device_name).first()
    if device and device.hashed_password == sha256(x_device_password.encode()).hexdigest():
        return device
    raise HTTPException(status_code=401, detail="Unauthorized")


@router.get("/verify-device/", status_code=status.HTTP_200_OK)
async def check_device(
    device: Device = Depends(verify_device)
):
    return {"message": "Device verified successfully", "data": device}

@router.post("/register-device/", status_code=status.HTTP_201_CREATED)
async def register_device(
    device_data: DeviceRegistration,
    db: Session = Depends(get_db),
):
    new_device = Device(
        device_name=device_data.device_name,
        hashed_password=sha256(device_data.device_password.encode()).hexdigest(),
        type=device_data.type,
        firmware_version=device_data.firmware_version,
        status=device_data.status
    )
    db.add(new_device)
    db.commit()
    db.refresh(new_device)

    return {"message": "Device registered successfully", "data": new_device}