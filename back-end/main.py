from typing import Union

from fastapi import FastAPI

# from config.db import Base, engine
from config.db import Base

app = FastAPI()
# Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}