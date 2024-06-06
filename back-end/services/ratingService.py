from sqlalchemy.orm import Session

from models.rating import Rating
from schemas.ratingSchema import RatingSchema
from helpers.statusCodes import OK
from helpers.dtos.responseDto import ResponseDto


def create(rating: RatingSchema, db: Session) -> ResponseDto:
    """
    Funcion para crear una valoración

    Args:
        rating (RatingSchema): informacion para crear una valoracion de un objeto RatingSchema
        db (Session): Sesion de la base de datos

    Returns:
        _type_: devuelve un objeto response dto con los resultados de la transacción
    """
    response = ResponseDto()

    newRating = Rating(**rating.__dict__)
    db.add(newRating)
    db.commit()
    db.refresh(newRating)

    response.status = OK
    response.message = "Puntuacion agregada con éxito"
    response.data = newRating.dict()
    return response
