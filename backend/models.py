import datetime
from .database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Boolean,
    DateTime,
    Float,
    Date,
    Enum,
)


class Account(Base):
    __tablename__ = "accounts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.now(),
        onupdate=datetime.datetime.now(),
        nullable=False,
    )


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"), nullable=True)
    account_id = Column(UUID(as_uuid=True), ForeignKey("accounts.id"), nullable=False)
    name = Column(String, nullable=False)
    sex = Column(Enum("male", "female", name="sex_enum"), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    age = Column(Integer, nullable=False)
    body_weight = Column(Float, nullable=False)
    body_height = Column(Float, nullable=False)
    BBI = Column(Float, nullable=False)
    KKB = Column(Float, nullable=False)
    KKarbo = Column(Float, nullable=False)
    KNasi = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.now(),
        onupdate=datetime.datetime.now(),
        nullable=False,
    )


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    device_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    type = Column(String, nullable=True)
    firmware_version = Column(String, nullable=True)
    status = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.now(),
        onupdate=datetime.datetime.now(),
        nullable=False,
    )


class Log(Base):
    __tablename__ = "logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"), nullable=False)
    weight = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.now(),
        onupdate=datetime.datetime.now(),
        nullable=False,
    )

class Research(Base):
    __tablename__ = "researches"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"), nullable=False)
    weight = Column(Float, nullable=False)
    roll = Column(Float, nullable=False)
    pitch = Column(Float, nullable=False)
    weight_prediction = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now(), nullable=False)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.now(),
        onupdate=datetime.datetime.now(),
        nullable=False,
    )