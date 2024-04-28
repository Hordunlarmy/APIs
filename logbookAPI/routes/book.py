from fastapi import APIRouter, Depends, HTTPException
from engine import get_db
from sqlalchemy.orm import Session
from engine import models
from engine.schemas import CreateBook


book = APIRouter()


@book.post("/create/", response_model=CreateBook)
async def create(student: CreateBook, db: Session = Depends(get_db)):
    """ Create A Log Book """

    try:
        school = db.query(models.School).filter(
            models.School.name == student.school).first()
        if not school:
            school = models.School(name=student.school,
                                   location=student.school_location)
            db.add(school)
            db.flush()

        department = db.query(models.Department).filter(
            models.Department.name == student.department,
            models.Department.school == school).first()
        if not department:
            department = models.Department(
                name=student.department, school=school)
            db.add(department)
            db.flush()

        company = db.query(models.Company).filter(
            models.Company.name == student.company).first()
        if not company:
            company = models.Company(name=student.company)
            db.add(company)
            db.flush()

        supervisor = db.query(models.Supervisor).filter(
            models.Supervisor.email == student.supervisors_email).first()
        if not supervisor:
            supervisor = models.Supervisor(
                first_name=student.supervisors_first_name,
                last_name=student.supervisors_last_name,
                email=student.supervisors_email,
                company=company)
            db.add(supervisor)
            db.flush()

        new_student = models.Student(
            matric_no=student.matric_no,
            first_name=student.first_name,
            last_name=student.last_name,
            email=student.email,
            school=school,
            department=department,
            company=company,
            supervisor=supervisor)
        db.add(new_student)

        # Commit all changes
        db.commit()

        return student

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
