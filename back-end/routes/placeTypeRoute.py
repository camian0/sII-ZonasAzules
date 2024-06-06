from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from config.dB import getDb
import traceback
from services.placeTypeService import getAllplaceTypes, createPlaceType
from services.AuthService import AuthService
from schemas.placeTypeSchema import PlaceTypeSchema
from helpers.logger import LOGGER
from helpers.responseMessages import ERRORMESSAGE500, ERRORMESSAGE500DB
from helpers.statusCodes import BAD_REQUEST, OK, INTERNAL_SERVER_ERROR
from helpers.dtos.responseDto import ResponseDto


placeTypeRoute = APIRouter(
    prefix="/place-types", tags=["tipo-plazas"], dependencies=[Depends(AuthService())]
)


@placeTypeRoute.get("/")
def getAll(db: Session = Depends(getDb)):
    try:
        responseDto = getAllplaceTypes(db)
        if responseDto.status == OK:
            return JSONResponse(content=responseDto.toString(), status_code=200)

        return JSONResponse(content=responseDto.toString(), status_code=OK)
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


@placeTypeRoute.post("/")
def create(PlaceTypeSchema: PlaceTypeSchema, db: Session = Depends(getDb)):
    try:
        responseDto = createPlaceType(PlaceTypeSchema, db)
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
