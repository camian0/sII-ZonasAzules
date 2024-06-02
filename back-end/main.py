from typing import Union
from fastapi import FastAPI
from config.DB import Base, engine

from routes.AuthRoute import authRouter
from models.AuthUser import AuthUser
from models.User import User
from models.Role import Role
from routes.UserRoute import userRoutes


def create_dbs():
    Role.__table__.create(bind=engine, checkfirst=True)
    AuthUser.__table__.create(bind=engine, checkfirst=True)
    User.__table__.create(bind=engine, checkfirst=True)


Base.metadata.create_all(bind=engine)
create_dbs()

app = FastAPI()
app.include_router(authRouter)
app.include_router(userRoutes)


@app.get("/")
def read_root():
    return {"Hello": "World"}
