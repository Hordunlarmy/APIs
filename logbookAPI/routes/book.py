from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from engine import get_db
from sqlalchemy.orm import Session
from engine import models, schemas
from engine.schemas import CreateBook


book = APIRouter()


@book.post("/book/", response_model=CreateBook)
async def create_a_book(student: CreateBook, db: Session = Depends(get_db)):
    """ Create A Log Book """

    try:
        school = db.query(models.School).filter(
            models.School.name == student.school.name).first()
        if not school:
            school = models.School(name=student.school.name,
                                   location=student.school.location)
            db.add(school)
            db.flush()

        department = db.query(models.Department).filter(
            models.Department.name == student.department.name,
            models.Department.school == school).first()
        if not department:
            department = models.Department(
                name=student.department.name, school=school)
            db.add(department)
            db.flush()

        company = db.query(models.Company).filter(
            models.Company.name == student.company.name).first()
        if not company:
            company = models.Company(name=student.company.name)
            db.add(company)
            db.flush()

        supervisor = db.query(models.Supervisor).filter(
            models.Supervisor.email == student.supervisor.email).first()
        if not supervisor:
            supervisor = models.Supervisor(
                first_name=student.supervisor.first_name,
                last_name=student.supervisor.last_name,
                email=student.supervisor.email,
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


@book.get("/books/", response_class=JSONResponse)
async def get_all_books(db: Session = Depends(get_db)):
    """ Get A List Of All Student LogBooks """

    students = db.query(models.Student).all()
    print(students)
    if not students:
        raise HTTPException(status_code=404, detail="LogBook Not Found")
    results = []
    for student in students:
        student_data = {
            "student_id": student.id,
            "school_id": student.school_id,
            "department_id": student.department_id,
            "company_id": student.company_id,
            "supervisor_id": student.supervisor_id,
            "matric_no": student.matric_no,
            "student_name": student.last_name + " " + student.first_name,
            "email": student.email,
            "logs": student.logbooks
        }
        results.append(student_data)
        return results
