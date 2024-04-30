from fastapi import APIRouter, Depends, HTTPException, Path
from engine import get_db
from sqlalchemy.orm import Session
from engine import models
from engine.schemas import CreateLog, ReturnLog
from datetime import date
from typing import List


log = APIRouter()


@log.post("/logs/{student_id}", response_model=CreateLog)
async def create_log(log: CreateLog, student_id: str = Path(...),
                     db: Session = Depends(get_db)):
    """ Create or update log entries only for today or future dates. """

    student = db.query(models.Student).filter(
        models.Student.id == student_id).first()
    if not student:
        raise HTTPException(
            status_code=404, detail="Student does not have a logbook")

    today = date.today()
    entry_date = log.entry_date if log.entry_date else today

    if entry_date < today:
        raise HTTPException(
            status_code=400, detail="Cannot create log entries for past dates")

    existing_log = db.query(models.LogBook).filter(
        models.LogBook.student_id == student_id,
        models.LogBook.entry_date == entry_date
    ).first()

    if existing_log:
        existing_log.work_description = log.work_description
        existing_log.work_status = log.work_status
    else:
        new_log = models.LogBook(
            student_id=student.id,
            work_description=log.work_description,
            work_status=log.work_status,
            entry_date=entry_date
        )
        db.add(new_log)

    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    return existing_log if existing_log else new_log


@log.get("/logs/{student_id}", response_model=List[ReturnLog])
async def get_student_logs(student_id: str = Path(...),
                           db: Session = Depends(get_db)):
    """ Retrive All Logs By A Student """

    student_logs = db.query(models.LogBook).filter(
        models.LogBook.student_id == student_id).all()
    if not student_logs:
        raise HTTPException(status_code=404, detail="Student Has No Logs")

    return [ReturnLog.from_orm(log) for log in student_logs]


@log.get("/log/{log_date}", response_model=ReturnLog)
async def get_by_date(log_date: date = Path(...),
                      db: Session = Depends(get_db)):
    """ Retrive A Log By Date """

    log = db.query(models.LogBook).filter(
        models.LogBook.entry_date == log_date).first()

    if not log:
        raise HTTPException(
            status_code=404, detail="No Log Entry For That Date")
    return log


@log.put("/logs/{log_id}", response_model=CreateLog)
async def update_log(log: CreateLog, log_id: str = Path(...),
                     db: Session = Depends(get_db)):
    """ Update A Log Entry"""

    log_to_update = db.query(models.LogBook).filter(
        models.LogBook.id == log_id).first()
    if not log_to_update:
        raise HTTPExecption(status=404, detail="Log Not Found")

    today = date.today()

    entry_date = log.entry_date if log.entry_date else today

    if entry_date < today:
        raise HTTPException(
            status_code=400, detail="Cannot create log entries for past dates")

    existing_log = db.query(models.LogBook).filter(
        models.LogBook.student_id == student_id,
        models.LogBook.entry_date == entry_date
    ).first()

    if existing_log:
        existing_log.work_description = log.work_description
        existing_log.work_status = log.work_status
    else:
        log_to_update.work_description = log.work_description
        log_to_update.work_status = log.work_status
        log_to_update.entry_date = entry_date

    try:
        db.commit()
        db.refresh(log_to_update)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    return log_to_update


@log.delete("/logs/{log_id}")
async def delete_log(log_id: str = Path(...),
                     db: Session = Depends(get_db)):
    """ Delete A Log Entry"""

    log_to_delete = db.query(models.LogBook).filter(
        models.LogBook.id == log_id).first()
    if not log_to_delete:
        raise HTTPException(status_code=404, detail="Log Not Found")
    try:
        db.delete(log_to_delete)
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    return {"detail": "Log Deleted Successfully"}
