from sqlalchemy.orm import Session

from models.reservation import Reservation
from helpers.helpers import queryPaginate
from schemas.reservationSchema import ReservationSchema
from helpers.dtos.responseDto import ResponseDto
from helpers.statusCodes import OK
from helpers.responseMessages import CREATED_RESERVATION_OK, GET_ALL_RESERVATION_OK

def get(db: Session, page: int, sizePage: int) -> ResponseDto:
    responseDto = ResponseDto()
    query = db.query(Reservation)
    res = queryPaginate(query, page, sizePage)
    
    reservations = [i.dict() for i in res]
    responseDto.status = OK
    responseDto.message = GET_ALL_RESERVATION_OK
    responseDto.data = reservations
    return responseDto




def create(reservationSchema: ReservationSchema, db: Session) -> ResponseDto:
    """
    Método para crear una reservación
    Args:
        reservationSchema (ReservationSchema): esquema que contiene los datos para la creación de una reservación
        db (Session): sesión de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        ResponseDto: respuesta generica
    """
    responseDto = ResponseDto()

    newReservation = Reservation(**reservationSchema.__dict__)
    db.add(newReservation)
    db.commit()
    db.refresh(newReservation)

    responseDto.status = OK
    responseDto.message = CREATED_RESERVATION_OK
    responseDto.data = newReservation.dict()
    return responseDto
