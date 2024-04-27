from pydantic import BaseModel, validator, EmailStr


class CreatLogBook(BaseModel):
    matric_no: int
    first_name: str
    last_name: str
    email: EmailStr
    school: str
    department: str
    company: str
    supervisor: str
