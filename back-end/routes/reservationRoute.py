from fastapi import APIRouter, Query, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from config.dB import getDb
import traceback
from services.AuthService import AuthService
from helpers.logger import LOGGER
from helpers.responseMessages import ERRORMESSAGE500, ERRORMESSAGE500DB
from helpers.statusCodes import BAD_REQUEST, OK, INTERNAL_SERVER_ERROR
from services.reservationService import get, create
from schemas.reservationSchema import ReservationSchema
from helpers.dtos.responseDto import ResponseDto
from pydantic import ValidationError


reservationRoute = APIRouter(
    prefix="/reservations", tags=["Reservations"], dependencies=[Depends(AuthService())]
)


@reservationRoute.get("/")
def getReservations(page: int = Query(default=1), sizePage: int = Query(default=10), db: Session = Depends(getDb)):
    try:
        responseDto = get(db, page=page, sizePage=sizePage)
        if responseDto.status == OK:
            return JSONResponse(content=responseDto.toString(), status_code=200)

        return JSONResponse(
            content=responseDto.toString(), status_code=200
        )
    except SQLAlchemyError as e:
        traceBack = traceback.format_exc()
        LOGGER.warning(f"error:{e}\n\n Traceback: {traceBack}")

        responseDto = ResponseDto()
        responseDto.status = INTERNAL_SERVER_ERROR
        responseDto.message = ERRORMESSAGE500DB
        return JSONResponse(
            content=responseDto.toString(),
            status_code=INTERNAL_SERVER_ERROR,
        )
    except Exception as e:
        traceBack = traceback.format_exc()
        LOGGER.error(f"error:{e}\n\n Traceback: {traceBack}")

        responseDto = ResponseDto()
        responseDto.status = INTERNAL_SERVER_ERROR
        responseDto.message = ERRORMESSAGE500
        return JSONResponse(
            content=responseDto.toString(),
            status_code=INTERNAL_SERVER_ERROR,
        )


@reservationRoute.post("/")
def createReservations(reservationSchema: ReservationSchema, db: Session = Depends(getDb)):
    try:
        responseDto = create(reservationSchema, db)
        if responseDto.status == OK:
            return JSONResponse(content=responseDto.toString(), status_code=OK)

        return JSONResponse(content=responseDto.toString(), status_code=BAD_REQUEST)

    except SQLAlchemyError as e:
        db.rollback()
        traceBack = traceback.format_exc()
        LOGGER.warning(f"error:{e}\n\n Traceback: {traceBack}")

        responseDto = ResponseDto()
        responseDto.status = INTERNAL_SERVER_ERROR
        responseDto.message = ERRORMESSAGE500DB
        return JSONResponse(
            content=responseDto.toString(),
            status_code=INTERNAL_SERVER_ERROR,
        )
    
    except Exception as e:
        db.rollback()
        traceBack = traceback.format_exc()
        LOGGER.error(f"error:{e}\n\n Traceback: {traceBack}")

        responseDto = ResponseDto()
        responseDto.status = INTERNAL_SERVER_ERROR
        responseDto.message = ERRORMESSAGE500
        return JSONResponse(
            content=responseDto.toString(),
            status_code=INTERNAL_SERVER_ERROR,
        )
