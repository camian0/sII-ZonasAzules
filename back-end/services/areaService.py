from sqlalchemy.orm import Session

from models.area import Area
from schemas.areaSchema import AreaSchema
from helpers.statusCodes import BAD_REQUEST, OK
from helpers.responseMessages import AREA_ALREARY_EXIST, CREATED_AREA_OK, GET_ALL_AREAS_TYPE_OK
from helpers.dtos.responseDto import ResponseDto


def getAllAreas(db: Session) -> ResponseDto:
    """
    Método para obtener todas las areas(sectores)

    Args:
        db (Session): sesion de la base de datos

    Returns:
        ResponseDto: El método devuelve una lista de objetos de tipo Area, objetos de tipo clave valor
    """
    responseDto = ResponseDto()

    query = db.query(Area).all()

    areas = [i.dict() for i in query]
    responseDto.status = OK
    responseDto.message = GET_ALL_AREAS_TYPE_OK
    responseDto.data = areas
    return responseDto


def createArea(areaSchema: AreaSchema, db: Session) -> ResponseDto:
    """
    Método para crear un área
    Args:
        areaSchema (AreaSchema): esquema que contiene los datos para la creación del área
        db (Session): sesión de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        ResponseDto: área creada
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
