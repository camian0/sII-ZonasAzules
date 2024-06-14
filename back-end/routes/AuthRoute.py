from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from config.dB import getDb
import traceback
from schemas.UserAuthSchema import UserAuthSchema
from services.LoginService import login
from helpers.logger import LOGGER
from helpers.responseMessages import ERRORMESSAGE500, ERRORMESSAGE500DB
from helpers.statusCodes import NO_AUTHOTIZED, INTERNAL_SERVER_ERROR, OK, BAD_REQUEST
from helpers.dtos.responseDto import ResponseDto
from models.authUser import AuthUser
from schemas.UserAuthSchema import UserAuthSchema
from models.role import Role
from services.AuthService import AuthService
from services.AuthService import getMenus

 

authRoute = APIRouter(prefix="/auth", tags=["auth"])


@authRoute.post("/")
def logIn(user: UserAuthSchema, db: Session = Depends(getDb)):
    try:        
        responseDto = login(user, db)
        if responseDto.status == OK:
            return JSONResponse(content=responseDto.toString(), status_code=OK)

        return JSONResponse(content=responseDto.toString(), status_code=BAD_REQUEST)
        
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


@authRoute.get("/menu", dependencies=[Depends(AuthService())])
def menus(email: str, db: Session = Depends(getDb)):
    try:
        responseDto = getMenus(email, db)
        if responseDto.status == OK:
            return JSONResponse(content=responseDto.toString(), status_code=OK)

        return JSONResponse(content=responseDto.toString(), status_code=BAD_REQUEST)   

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

