from typing import List
from sqlalchemy.orm import Session

from models.blueZone import BlueZone
from helpers.helpers import queryPaginate
from schemas.blueZoneSchema import BlueZoneSchema
from helpers.dtos.responseDto import ResponseDto
from helpers.statusCodes import BAD_REQUEST, OK
from helpers.responseMessages import BLUE_ZONE_ALREARY_EXIST, CREATED_BLUE_ZONE_OK, GET_ALL_BLUE_ZONE_OK

def get(db: Session, page: int, sizePage: int) -> ResponseDto:
    responseDto = ResponseDto()
    query = db.query(BlueZone)
    res = queryPaginate(query, page, sizePage)
    
    zones = [i.dict() for i in res]
    responseDto.status = OK
    responseDto.message = GET_ALL_BLUE_ZONE_OK
    responseDto.data = zones
    return responseDto



def create(blueZoneSchema: BlueZoneSchema, db: Session) -> ResponseDto:
    """
    Método para crear una zona azul
    Args:
        blueZoneSchema (BlueZoneSchema): esquema que contiene los datos para la creación del zona azul
        db (Session): sesión de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        ResponseDto: respuesta generica
    """
    responseDto = ResponseDto()
    existBlueZone = db.query(BlueZone).filter_by(name=blueZoneSchema.name).first()
    if existBlueZone:
        responseDto.status = BAD_REQUEST
        responseDto.message = BLUE_ZONE_ALREARY_EXIST
        return responseDto

    newBlueZone = BlueZone(**blueZoneSchema.__dict__)
    db.add(newBlueZone)
    db.commit()
    db.refresh(newBlueZone)

    responseDto.status = OK
    responseDto.message = CREATED_BLUE_ZONE_OK
    responseDto.data = newBlueZone.dict()
    return responseDto
