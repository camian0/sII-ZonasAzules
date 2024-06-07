from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from config.dB import getDb
import traceback
from services.UserService import getUsers, create
from services.AuthService import AuthService
from schemas.User import UserSchema
from helpers.logger import LOGGER
from helpers.responseMessages import ERRORMESSAGE500, ERRORMESSAGE500DB


userRoutes = APIRouter(
    prefix="/users", tags=["users"]#, dependencies=[Depends(AuthService())]
)


@userRoutes.get("/")
def getAll(db: Session = Depends(getDb)):
    try:
        query = getUsers(db)
        if query:
            return JSONResponse(content={"data": query}, status_code=200)

        return JSONResponse(
            content={"message": "No hay usuarios para mostrar."}, status_code=200
        )
    except SQLAlchemyError as e:
        traceBack = traceback.format_exc()
        LOGGER.warning(f"error:{e}\n\n Traceback: {traceBack}")
        return JSONResponse(
            content=ERRORMESSAGE500DB,
            status_code=500,
        )
    except Exception as e:
        traceBack = traceback.format_exc()
        LOGGER.error(f"error:{e}\n\n Traceback: {traceBack}")
        return JSONResponse(
            content=ERRORMESSAGE500,
            status_code=500,
        )


@userRoutes.post("/")
def addUser(user: UserSchema, db: Session = Depends(getDb)):
    try:
        query = create(user, db)
        if query:
            return JSONResponse(
                content={"message": "Usuario agregado correctamente"}, status_code=200
            )

        return JSONResponse(
            content={"message": "No se pudo agregar el usuario"}, status_code=401
        )
    except SQLAlchemyError as e:
        db.rollback()
        traceBack = traceback.format_exc()
        LOGGER.warning(f"error:{e}\n\n Traceback: {traceBack}")
        return JSONResponse(
            content=ERRORMESSAGE500DB,
            status_code=500,
        )
    except Exception as e:
        db.rollback()
        traceBack = traceback.format_exc()
        LOGGER.error(f"error:{e}\n\n Traceback: {traceBack}")
        return JSONResponse(
            content=ERRORMESSAGE500,
            status_code=500,
        )
