from typing import Union
from fastapi import FastAPI
from config.DB import Base, engine

from routes.AuthRoute import authRouter

# Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(authRouter)


@app.get("/")
def read_root():
    return {"Hello": "World"}
