import uuid
from sqlalchemy import (Column, String, Text, Date,
                        ForeignKey, Integer, func)
from sqlalchemy.types import Enum
from .schemas import WorkStatus
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from engine import Base


class Student(Base):
    __tablename__ = "student"
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    matric_no = Column(String(20), unique=True, nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    school_id = Column(String(36), ForeignKey('school.id'))
    school = relationship("School", backref="students")
    department_id = Column(String(36), ForeignKey('department.id'))
    department = relationship("Department", backref="students")
    company_id = Column(String(36), ForeignKey('company.id'))
    company = relationship("Company", backref="students")
    supervisor_id = Column(String(36), ForeignKey('supervisor.id'))
    supervisor = relationship("Supervisor", backref="students")

    def __repr__(self):
        return f"Student('{self.first_name} {self.last_name}', '{self.email}')"


class School(Base):
    __tablename__ = "school"
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    name = Column(String(120), unique=True, nullable=False)
    location = Column(String(120), nullable=False)

    def __repr__(self):
        return f"School('{self.name}', '{self.location}')"


class Department(Base):
    __tablename__ = "department"
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    name = Column(String(120), nullable=False)
    school_id = Column(String(36), ForeignKey('school.id'), nullable=False)
    school = relationship("School", backref="departments")

    def __repr__(self):
        return f"Department('{self.name}')"


class Company(Base):
    __tablename__ = "company"
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    name = Column(String(120), nullable=False)

    def __repr__(self):
        return f"Company('{self.name}')"


class Supervisor(Base):
    __tablename__ = "supervisor"
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    company_id = Column(String(36), ForeignKey('company.id'), nullable=False)
    company = relationship("Company", backref="supervisors")

    def __repr__(self):
        return (
            f"Supervisor('{self.first_name}', '{self.last_name}')")


class LogBook(Base):
    __tablename__ = "logbook"
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    student_id = Column(String(36), ForeignKey(
        'student.id', ondelete='CASCADE'), nullable=False)
    work_description = Column(Text)
    work_status = Column(Enum(WorkStatus,
                              values_callable=lambda obj: [
                                  e.value for e in obj]),
                         nullable=False)
    entry_date = Column(Date, default=func.current_date())
    student = relationship("Student", backref="logbooks")

    def __repr__(self):
        return f"LogBook('{self.work_description}', '{self.date_posted}')"
