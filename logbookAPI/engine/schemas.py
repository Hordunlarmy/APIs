from pydantic import BaseModel, validator, EmailStr


class CreateLogBook(BaseModel):
    matric_no: int
    first_name: str
    last_name: str
    email: EmailStr
    school: str
    school_location: str
    department: str
    company: str
    supervisors_first_name: str
    supervisors_last_name: str
