from sqlalchemy.orm import Session

from models.area import Area
from schemas.areaSchema import AreaSchema
from helpers.statusCodes import BAD_REQUEST, OK
from helpers.responseMessages import (
    AREA_ALREARY_EXIST,
    CREATED_AREA_OK,
    GET_ALL_AREAS_TYPE_OK,
    NOT_FOUND_AREA,
    DELETED_AREA_OK,
    UPDATE_AREA_OK
)
from helpers.dtos.responseDto import ResponseDto
from helpers.helpers import queryPaginate


def get(page, sizePage, db: Session) -> ResponseDto:
    """
    Método para obtener todas las areas(sectores)

    Args:
        page (_type_): numero de página
        sizePage (_type_): registros por página
        db (Session): sesion de la base de datos

    Returns:
        ResponseDto: respuesta generica
    """
    responseDto = ResponseDto()

    query = db.query(Area)
    res = queryPaginate(query, page, sizePage)

    areas = [i.dict() for i in res]
    responseDto.status = OK
    responseDto.message = GET_ALL_AREAS_TYPE_OK
    responseDto.data = areas
    return responseDto


def getName(areaName: str, db: Session) -> ResponseDto:
    """
    Método para obtener una Area por el número
    Args:
        areaSchema (str): nombre del Area
        db (Session): sesión de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        ResponseDto: respuesta generica
    """
    responseDto = ResponseDto()
    existArea = db.query(Area).filter_by(name=areaName).first()
    if not existArea:
        responseDto.status = BAD_REQUEST
        responseDto.message = NOT_FOUND_AREA
        return responseDto
    
    responseDto.status = OK
    responseDto.message = GET_ALL_AREAS_TYPE_OK
    responseDto.data = existArea.dict()
    return responseDto


def create(areaSchema: AreaSchema, db: Session) -> ResponseDto:
    """
    Método para crear un área
    Args:
        areaSchema (AreaSchema): esquema que contiene los datos para la creación del área
        db (Session): sesión de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        ResponseDto: respuesta generica
    """
    responseDto = ResponseDto()
    existArea = db.query(Area).filter_by(name=areaSchema.name).first()
    if existArea:
        responseDto.status = BAD_REQUEST
        responseDto.message = AREA_ALREARY_EXIST
        return responseDto

    newArea = Area(**areaSchema.__dict__)
    db.add(newArea)
    db.commit()
    db.refresh(newArea)

    responseDto.status = OK
    responseDto.message = CREATED_AREA_OK
    responseDto.data = newArea.dict()
    return responseDto

def delete(areaName: str, db: Session) -> ResponseDto:
    """
    Método para eliminar un area
    Args:
        areaName (str): nombre del area a eliminar
        db (Session): sesión de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        ResponseDto: respuesta generica
    """
    responseDto = ResponseDto()
    area = db.query(Area).filter_by(name=areaName).first()
    if not area:
        responseDto.status = BAD_REQUEST
        responseDto.message = NOT_FOUND_AREA
        return responseDto

    db.delete(area)
    db.commit()

    responseDto.status = OK
    responseDto.message = DELETED_AREA_OK
    responseDto.data = area.dict()
    return responseDto

def update(areaName: str, newAreaName: str, db: Session, ) -> ResponseDto:
    """
    Método para actualizar el nombre de una Área
    Args:
        areaName (str): nombre actual del Área
        newAreaName (str): nuevo nombre para el Área
        db (Session): sesión de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        ResponseDto: respuesta generica
    """
    responseDto = ResponseDto()
    existArea = db.query(Area).filter_by(name=areaName).first()
    if not existArea:
        responseDto.status = BAD_REQUEST
        responseDto.message = NOT_FOUND_AREA
        return responseDto

    existArea.name = newAreaName
    db.commit()
    db.refresh(existArea)

    responseDto.status = OK
    responseDto.message = UPDATE_AREA_OK
    responseDto.data = existArea.dict()
    return responseDto