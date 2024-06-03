from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from config.dB import getDb
from schemas.UserAuthSchema import UserAuthSchema
from services.LoginService import login
from helpers.logger import LOGGER
from helpers.errorMessages import ERRORMESSAGE500

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
    except SQLAlchemyError as e:
        LOGGER.critical(e)
        return JSONResponse(
            content=ERRORMESSAGE500,
            status_code=500,
        )
    except Exception as e:
        LOGGER.error(e)
        return JSONResponse(
            content=ERRORMESSAGE500,
            status_code=500,
        )
