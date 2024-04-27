import uuid
from sqlalchemy import (Column, String, Text, DateTime,
                        ForeignKey, Integer, func)
from sqlalchemy.orm import relationship, backref
from datetime import datetime
from engine import Base


class Student(Base):
    __tablename__ = "student"
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    matric_no = Column(Integer, unique=True, nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    logs = relationship("LogBook", backref=backref(
        "student", lazy='joined'), cascade="all, delete-orphan")

    def __repr__(self):
        return f"Student('{self.first_name} {self.last_name}', '{self.email}')"


class School(Base):
    __tablename__ = "school"
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    name = Column(String(120), nullable=False)
    location = Column(String(120), nullable=False)

    def __repr__(self):
        return f"School('{self.name}', '{self.location}')"


class Department(Base):
    __tablename__ = "department"
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    name = Column(String(120), nullable=False)
    school_id = Column(String(36), ForeignKey('school.id'), nullable=False)

    def __repr__(self):
        return f"Department('{name}')"


class Company(Base):
    __tablename__ = "company"
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    name = Column(String(120), nullable=False)

    def __repr__(self):
        return f"Company('{name}')"


class Supervisor(Base):
    __tablename__ = "supervisor"
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    full_name = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    company_id = Column(String(36), ForeignKey('company.id'), nullable=False)
    company = relationship("Company", backref=backref(
        "supervisors", lazy='dynamic'))

    def __repr__(self):
        return f"Supervisor('{self.full_name}', '{self.email}')"


class LogBook(Base):
    __tablename__ = "logbook"
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    work_description = Column(String(100), nullable=False)
    work_status = Column(Text, nullable=False)
    date_posted = Column(DateTime, default=func.now())
    student_id = Column(String(36), ForeignKey(
        'student.id', ondelete='CASCADE'), nullable=False)
    supervisor_id = Column(String(36), ForeignKey(
        'supervisor.id'), nullable=False)
    supervisor = relationship("Supervisor", backref="logbooks")

    def __repr__(self):
        return f"LogBook('{self.work_description}', '{self.date_posted}')"
