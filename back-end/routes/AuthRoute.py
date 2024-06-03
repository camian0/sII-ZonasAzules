from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from config.dB import getDb
from schemas.UserAuthSchema import UserAuthSchema
from services.LoginService import login

authRoute = APIRouter(prefix="/auth", tags=["auth"])


@authRoute.post("/")
def logIn(user: UserAuthSchema, db: Session = Depends(getDb)):
    try:
        query = login(user, db)
        if query:
            return JSONResponse(content={"token": query}, status_code=200)

        return JSONResponse(
            content={"message": "Por favor verifica los datos ingresados"},
            status_code=401,
        )
    except Exception as e:
        return JSONResponse(
            content={
                "message": "Error interno en el servidor, no se pudo procesar la solicitud"
            },
            status_code=500,
        )
