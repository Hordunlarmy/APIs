from fastapi import APIRouter, Depends, HTTPException
from engine import get_db
from sqlalchemy.orm import Session
from engine import models
from engine.schemas import CreateLog


log = APIRouter()


@log.post("/create/", response_model=CreateLog)
async def create_log(db: Session = Depends(get_db)):
    """ create log entries"""

    return {"message": "New_Log"}
