from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from config.dB import getDb
import traceback
from schemas.CreditCardSchema import CreditCardSchema
from services.UserService import getUsers, create
from services.CardService import CardService
from helpers.logger import LOGGER
from helpers.errorMessages import ERRORMESSAGE500, ERRORMESSAGE500DB


userRoutes = APIRouter(
    prefix="/creditcard", tags=["creditcard"], dependencies=[Depends(CardService())]
)


@userRoutes.get("/")
def getAll(db: Session = Depends(getDb)):
    try:
        query = getUsers(db)
        if query:
            return JSONResponse(content={"data": query}, status_code=200)

        return JSONResponse(
            content={"message": "No hay Tarjetas de Credito para mostrar."}, status_code=200
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

'''
@userRoutes.post("/")
def addCard(user: CreditCardSchema, db: Session = Depends(getDb)):
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
'''