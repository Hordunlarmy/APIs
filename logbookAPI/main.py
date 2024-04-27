import uvicorn
from fastapi import FastAPI

app = FastAPI()


if __name__ == "__main__":
    run.uvicorn("main:app", reload="True")
