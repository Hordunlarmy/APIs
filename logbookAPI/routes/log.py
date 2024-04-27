from fastapi import APIRouter, Depends
from engine import get_db
from sqlalchemy.orm import Session


log_book = APIRouter()


@log_book.post("/create/")
async def create(db: Session = Depends(get_db)):
    """ Create A Log Book"""

    return {"message": "Log Active"}
