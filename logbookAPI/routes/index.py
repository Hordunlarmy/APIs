from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

main = APIRouter()


@main.get("/", response_class=HTMLResponse)
async def home():
    """ Returns an html content """

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
