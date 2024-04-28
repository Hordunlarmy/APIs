from pydantic import BaseModel, validator, EmailStr


class CreateBook(BaseModel):
    matric_no: str
    first_name: str
    last_name: str
    email: EmailStr
    school: str
    school_location: str
    department: str
    company: str
    supervisors_first_name: str
    supervisors_last_name: str
    supervisors_email: EmailStr


class CreateLog(BaseModel):
    student_id: str
    work_description: str
    works_status: str
