from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# from schemas.auth import User
# from models.auth import User as UserModel
# from services.users import get_user_inDB, get_user_by_username, create_new_user

# from config.jwt_depends import JWTBearer

from sqlalchemy.orm import Session
from config.db import get_db

from models.blueZone import BlueZone
from models.menu import Menu
from models.role import Role
from models.roleMenu import RoleMenu
from models.area import Area
from schemas.searchBlueZoneSchema import SearchBlueZoneSchema



search_blue_zone_router = APIRouter(prefix="/search")


# Ruta de obtención de la base de datos #TODO: Conectar a la base de datos y obtener la información.
@search_blue_zone_router.post("/")
def get(searchBlueZone: SearchBlueZoneSchema, db:Session = Depends(get_db)):
    zone = db.query(BlueZone).filter(BlueZone.id == searchBlueZone.id).first()   
    if zone:
        outZone = SearchBlueZoneSchema(**zone.__dict__)
        return JSONResponse(content=outZone, status_code=200)
        # return outZone
    else:
         return JSONResponse(content={"message": "Zona no encontrada"}, status_code=200)

    # out_users = get_user_inDB(db)

    # return JSONResponse(content=jsonable_encoder({"test":"hello"}), status_code=200)
