from fastapi import APIRouter, Depends, HTTPException, Path
from engine import get_db
from sqlalchemy.orm import Session
from engine import models
from engine.schemas import CreateLog
from datetime import date


log = APIRouter()


@log.post("/log/", response_model=CreateLog)
async def create_log(log: CreateLog, db: Session = Depends(get_db)):
    """ Create log entries only for today or future dates. """

    student = db.query(models.Student).filter(
        models.Student.id == log.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="LogBook Not Found")
    today = date.today()

    entry_date = log.entry_date if log.entry_date else today

    if entry_date < today:
        raise HTTPException(
            status_code=400, detail="Cannot create log entries for past dates")
    try:
        new_log = models.LogBook(student_id=student.id,
                                 work_description=log.work_description,
                                 work_status=log.work_status,
                                 entry_date=entry_date)
        db.add(new_log)
        db.commit()

        return new_log

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
