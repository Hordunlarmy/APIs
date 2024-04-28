from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from engine import get_db, models
from sqlalchemy.orm import Session

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
