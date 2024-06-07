from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from config.dB import getDb
import traceback
from schemas.UserAuthSchema import UserAuthSchema
from services.LoginService import login
from helpers.logger import LOGGER
from helpers.responseMessages import ERRORMESSAGE500, ERRORMESSAGE500DB, VERIFY_INFO
from helpers.statusCodes import BAD_REQUEST, NO_AUTHOTIZED, OK, INTERNAL_SERVER_ERROR
from helpers.dtos.responseDto import ResponseDto

authRoute = APIRouter(prefix="/auth", tags=["auth"])


@authRoute.post("/")
def logIn(user: UserAuthSchema, db: Session = Depends(getDb)):
    try:
        responseDto = login(user, db)
        if responseDto != None:
            return JSONResponse(content={"token": responseDto}, status_code=200)

        responseDto = ResponseDto()
        responseDto.status = NO_AUTHOTIZED
        responseDto.message = VERIFY_INFO
        return  JSONResponse(
            content=responseDto.toString(), 
            status_code=NO_AUTHOTIZED
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
