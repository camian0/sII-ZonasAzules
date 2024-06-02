from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from config.dB import getDb
from schemas.UserAuthSchema import UserAuthSchema
from services.LoginService import login
from services.AuthService import AuthService

authRoute = APIRouter(
    prefix="/auth", tags=["auth"], dependencies=[Depends(AuthService())]
)


@authRoute.post("/")
def logIn(user: UserAuthSchema, db: Session = Depends(getDb)):
    query = login(user, db)
    if query:
        return JSONResponse(content={"token": query}, status_code=200)

    return JSONResponse(
        content={"Por favor verifica los datos ingresados"}, status_code=401
    )
