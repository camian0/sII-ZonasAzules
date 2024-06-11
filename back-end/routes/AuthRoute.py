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
from models.authUser import AuthUser
from schemas.UserAuthSchema import UserAuthSchema
from models.role import Role
from helpers.Role import MantainRole
from services.AuthService import AuthService


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


@authRoute.post("/menu", dependencies=[Depends(AuthService())])
def menus(email: str, db: Session = Depends(getDb)):
    try:
        user = db.query(AuthUser).filter(email == AuthUser.email).first()
        role = user.role
        menus = Role.getMenus(role)
        return JSONResponse(content={"permits": menus}, status_code=200)
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
