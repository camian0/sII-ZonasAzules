from sqlalchemy.orm import Session
from datetime import datetime

from models.reservation import Reservation
from models.blueZone import BlueZone
from helpers.helpers import queryPaginate
from schemas.reservationSchema import ReservationSchema
from helpers.dtos.responseDto import ResponseDto
from helpers.statusCodes import OK, BAD_REQUEST
from helpers.responseMessages import (CREATED_RESERVATION_OK, GET_ALL_RESERVATION_OK, 
                                    RESERVATION_ALREADY_EXIST,
                                    BLUE_ZONE_ALREARY_EXIST,
                                    NO_SPACE_AVAILABLE,
                                    NOT_FOUND_RESERVATION,
                                    DELETED_RESERVATION_OK,
                                    NOT_FOUND_USER
                                    )
def get(db: Session, page: int, sizePage: int) -> ResponseDto:
    responseDto = ResponseDto()
    query = db.query(Reservation)
    res = queryPaginate(query, page, sizePage)
    
    reservations = [i.dict() for i in res]
    responseDto.status = OK
    responseDto.message = GET_ALL_RESERVATION_OK
    responseDto.data = reservations
    return responseDto


def getByUserId(user_id: int, db: Session, page: int = 1, sizePage: int = 10) -> ResponseDto:
    """
    Método para obtener reservaciones por ID de usuario
    Args:
        user_id (int): ID del usuario
        db (Session): sesión de la base de datos que se recibe desde la ruta que fue llamada
        page (int): número de página para la paginación
        sizePage (int): tamaño de página para la paginación

    Returns:
        ResponseDto: respuesta generica
    """
    responseDto = ResponseDto()
    query = db.query(Reservation).filter_by(user_id=user_id)
    res = queryPaginate(query, page, sizePage)

    if not res:
        responseDto.status = BAD_REQUEST
        responseDto.message = NOT_FOUND_USER
        return responseDto


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

    # Verificar si ya existe una reserva con el mismo ID
    responseDto = ResponseDto()
    existReserva = db.query(Reservation).filter_by(id=reservationSchema.id).first()
    if existReserva:
        responseDto.status = BAD_REQUEST
        responseDto.message = RESERVATION_ALREADY_EXIST
        return responseDto
    
     # Obtener la zona azul
    blueZone = db.query(BlueZone).filter_by(id=reservationSchema.blue_zone_id).first()
    if not blueZone:
        responseDto.status = BAD_REQUEST
        responseDto.message = BLUE_ZONE_ALREARY_EXIST
        return responseDto
    
    # Contar el número de reservaciones activas en el mismo horario
    overlapping_reservations = db.query(Reservation).filter(
        Reservation.blue_zone_id == reservationSchema.blue_zone_id,
        Reservation.start_date < reservationSchema.finish_date,
        Reservation.finish_date > reservationSchema.start_date
    ).count()

    # Verificar el tipo de lugar y la capacidad
    if reservationSchema.place_type_id == 1:  # Asumiendo que 1 es para autos
        total_places = blueZone.total_car_places
    else:  # Asumiendo que cualquier otro valor es para motos
        total_places = blueZone.total_moto_places

    if overlapping_reservations >= total_places:
        responseDto.status = BAD_REQUEST
        responseDto.message = NO_SPACE_AVAILABLE
        return responseDto
    
    


    # Convertir las cadenas a objetos datetime
    start_date = datetime.strptime(reservationSchema.start_date, '%Y-%m-%d %H:%M:%S')
    finish_date = datetime.strptime(reservationSchema.finish_date, '%Y-%m-%d %H:%M:%S')
     # Calcular la diferencia en horas entre start_date y finish_date
    

    duration = finish_date - start_date
    duration_in_hours = duration.total_seconds() / 3600
    if reservationSchema.place_type_id==1:
        total = duration_in_hours * blueZone.price_car
    else:
        total = duration_in_hours * blueZone.price_moto

    
    newReservation = Reservation(
            start_date=start_date,
            finish_date=finish_date,
            plate=reservationSchema.plate,
            user_id=reservationSchema.user_id,
            place_type_id=reservationSchema.place_type_id,
            blue_zone_id=reservationSchema.blue_zone_id,
            total_price=total
        )
    db.add(newReservation)
    db.commit()
    db.refresh(newReservation)

    responseDto.status = OK
    responseDto.message = CREATED_RESERVATION_OK
    responseDto.data = newReservation.dict()
    return responseDto

def delete(reservationId: str, db: Session) -> ResponseDto:
    """
    Método para eliminar una reserva
    Args:
        reservationId (str): id de la reserva a eliminar
        db (Session): sesión de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        ResponseDto: respuesta generica
    """
    responseDto = ResponseDto()
    reservation = db.query(Reservation).filter_by(id=reservationId).first()
    if not reservation:
        responseDto.status = BAD_REQUEST
        responseDto.message = NOT_FOUND_RESERVATION
        return responseDto

    db.delete(reservation)
    db.commit()

    responseDto.status = OK
    responseDto.message = DELETED_RESERVATION_OK
    responseDto.data = reservation.dict()
    return responseDto

