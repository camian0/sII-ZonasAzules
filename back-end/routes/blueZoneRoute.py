from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from config.dB import getDb
import traceback
from services.AuthService import AuthService
from helpers.logger import LOGGER
from helpers.responseMessages import ERRORMESSAGE500, ERRORMESSAGE500DB
from services.blueZoneService import get
from schemas.pageSchema import PageSchema


blueZoneRoute = APIRouter(
    prefix="/blue-zone", tags=["Blue Zone"], dependencies=[Depends(AuthService())]
)


@blueZoneRoute.get("/")
def getBlueZones(page: PageSchema, db: Session = Depends(getDb)):
    try:
        query = get(db, page=page.page, sizePage=page.sizePage)
        if query:
            return JSONResponse(content={"data": query}, status_code=200)

        return JSONResponse(
            content={"message": "No hay zonas azules para mostrar."}, status_code=200
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
