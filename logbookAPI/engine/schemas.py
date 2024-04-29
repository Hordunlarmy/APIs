from pydantic import BaseModel, validator, EmailStr
from datetime import date
from typing import Optional
from enum import Enum


class School(BaseModel):
    name: str
    location: str


class Department(BaseModel):
    name: str


class Company(BaseModel):
    name: str


class Supervisor(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class CreateBook(BaseModel):
    matric_no: str
    first_name: str
    last_name: str
    email: EmailStr
    school: School
    department: Department
    company: Company
    supervisor: Supervisor

    class Config:
        from_attributes = True


class WorkStatus(Enum):
    """ Work Status Model. Options(Completed, In Progress or Not Started)"""
    COMPLETED = "Completed"
    IN_PROGRESS = "In Progress"
    NOT_STARTED = "Not Started"


class CreateLog(BaseModel):
    student_id: str
    work_description: str
    work_status: WorkStatus
    entry_date: Optional[date] = None

    class Config:
        json_encoders = {
            date: lambda v: v.isoformat()
        }
