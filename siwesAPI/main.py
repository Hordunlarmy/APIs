import uvicorn
import routes
from fastapi import FastAPI
from engine import create_db

app = FastAPI()
create_db()

app.include_router(routes.main)
app.include_router(routes.book)
app.include_router(routes.log)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload="True")
