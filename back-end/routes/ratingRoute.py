from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from config.dB import getDb
import traceback
from services.AuthService import AuthService
from helpers.logger import LOGGER
from helpers.responseMessages import ERRORMESSAGE500, ERRORMESSAGE500DB
from helpers.statusCodes import BAD_REQUEST, OK, INTERNAL_SERVER_ERROR
from schemas.ratingSchema import RatingSchema
from helpers.dtos.responseDto import ResponseDto
from services.ratingService import create, getAll


ratingRoute = APIRouter(
    prefix="/rating", tags=["rating"], dependencies=[Depends(AuthService())]
)


@ratingRoute.post("/")
def createRate(rating: RatingSchema, db: Session = Depends(getDb)):
    response = ResponseDto()
    try:
        response = create(rating, db)
        if response.status == OK:
            return JSONResponse(content=response.toString(), status_code=OK)

        return JSONResponse(content=response.toString(), status_code=BAD_REQUEST)
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


@ratingRoute.get("/")
def getRates(
    page: int = Query(default=1),
    sizePage: int = Query(default=10),
    db: Session = Depends(getDb),
):
    response = ResponseDto()
    try:
        response = getAll(page, sizePage, db)
        if response.status == OK:
            return JSONResponse(content=response.toString(), status_code=OK)

        return JSONResponse(content=response.toString(), status_code=BAD_REQUEST)
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
