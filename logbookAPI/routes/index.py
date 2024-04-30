from fastapi import APIRouter, Depends, Query
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from engine import get_db, models
from sqlalchemy.orm import Session
from typing import List, Optional
from engine.schemas import ReturnLog
from datetime import date


main = APIRouter()


@main.get("/", response_class=HTMLResponse)
async def home(db: Session = Depends(get_db)):
    """ Returns an html content """

    student = db.query(models.Student).all()
    supervisor = db.query(models.Supervisor).all()
    for student in student:
        print(student.supervisor)
    for sup in supervisor:
        print(sup.id)
        print(sup.first_name)

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>SIWES Logbook API</title>
    </head>
    <body>
        <h1>MY SIWES LOGBOOK API</h1>
        <p>
        Welcome to the SIWES Logbook API. This platform allows students,
        supervisors, and administrators to manage logbook entries efficiently.
        Use this API to create, read, update, and delete logbook entries,
        track student progress, and oversee work experience documentation.
        </p>
    </body>
    </html>
    """


@main.get("/search/logs", response_model=List[ReturnLog])
async def search_logs(
    start_date: Optional[date] = Query(
        None, description="Start date of the log period"),
    end_date: Optional[date] = Query(
        None, description="End date of the log period"),
    work_status: Optional[str] = Query(
        None, description="Work status of the logs"),
    db: Session = Depends(get_db)
):
    """ Retrieve logs based on date range and work status """

    query = db.query(models.LogBook)

    if start_date and end_date:
        query = query.filter(models.LogBook.entry_date >= start_date,
                             models.LogBook.entry_date <= end_date)
    elif start_date:
        query = query.filter(models.LogBook.entry_date >= start_date)
    elif end_date:
        query = query.filter(models.LogBook.entry_date <= end_date)

    if work_status:
        query = query.filter(models.LogBook.work_status == work_status)

    logs = query.all()
    if not logs:
        raise HTTPException(status_code=404, detail="No log entries found")
    return logs
