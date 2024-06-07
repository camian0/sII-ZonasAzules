from sqlalchemy.orm import Session

from models.placeType import PlaceType
from schemas.placeTypeSchema import PlaceTypeSchema
from helpers.statusCodes import BAD_REQUEST, OK
from helpers.responseMessages import PLACE_TYPE_ALREARY_EXIST, CREATED_PLACE_TYPE_OK, GET_ALL_PLACE_TYPE_OK
from helpers.dtos.responseDto import ResponseDto


def get(db: Session) -> ResponseDto:
    """
    Método para obtener todas los tipos de plazas

    Args:
        db (Session): sesion de la base de datos

    Returns:
        ResponseDto: respuesta generica
    """
    responseDto = ResponseDto()

    query = db.query(PlaceType).order_by("id").all()

    placeTypes = [i.dict() for i in query]
    responseDto.status = OK
    responseDto.message = GET_ALL_PLACE_TYPE_OK
    responseDto.data = placeTypes
    return responseDto


def create(placeTypeSchema: PlaceTypeSchema, db: Session) -> ResponseDto:
    """
    Método para crear un tipo de plaza
    Args:
        placeTypeSchema (PlaceTypeSchema): esquema que contiene los datos para la creación del tipo de plaza
        db (Session): sesión de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        ResponseDto: respuesta generica
    """
    responseDto = ResponseDto()
    existPlaceType = db.query(PlaceType).filter_by(name=placeTypeSchema.name).first()
    if existPlaceType:
        responseDto.status = BAD_REQUEST
        responseDto.message = PLACE_TYPE_ALREARY_EXIST
        return responseDto

    newPlaceType = PlaceType(**placeTypeSchema.__dict__)
    db.add(newPlaceType)
    db.commit()
    db.refresh(newPlaceType)

    responseDto.status = OK
    responseDto.message = CREATED_PLACE_TYPE_OK
    responseDto.data = newPlaceType.dict()
    return responseDto
