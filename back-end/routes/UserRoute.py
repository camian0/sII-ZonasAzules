from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from config.dB import getDb
from models.User import User
from services.UserService import getUsers
from services.AuthService import AuthService

userRoutes = APIRouter(
    prefix="/users", tags=["users"], dependencies=[Depends(AuthService())]
)


@userRoutes.get("/")
def getAll(db: Session = Depends(getDb)):
    query = getUsers(db)
    if query:
        return JSONResponse(content={"data": query}, status_code=200)

    return JSONResponse(content={"No hay usuarios para mostrar."}, status_code=401)
