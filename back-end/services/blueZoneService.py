from typing import List
from sqlalchemy.orm import Session, aliased
from sqlalchemy import func, and_, or_

from models.blueZone import BlueZone
from models.reservation import Reservation
from helpers.helpers import queryPaginate
from schemas.blueZoneSchema import BlueZoneSchema
from schemas.blueZonesFilterSchema import BlueZonesFilterSchema
from helpers.dtos.responseDto import ResponseDto
from helpers.statusCodes import BAD_REQUEST, OK
from helpers.responseMessages import BLUE_ZONE_ALREARY_EXIST, BLUE_ZONE_NOT_EXIST, CREATED_BLUE_ZONE_OK, GET_ALL_BLUE_ZONE_FREE, GET_ALL_BLUE_ZONE_OK, UPDATE_BLUE_ZONE_OK

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

def update(blueZoneSchema: BlueZoneSchema, db: Session) -> ResponseDto:
    """
    Método para actualizar una zona azul existente
    Args:
        blueZoneSchema (BlueZoneSchema): esquema que contiene los datos para la actualización de la zona azul
    """
    responseDto = ResponseDto()
    existingBlueZone = db.query(BlueZone).filter_by(id=blueZoneSchema.id).first()
    if not existingBlueZone:
        responseDto.status = BAD_REQUEST
        responseDto.message = BLUE_ZONE_NOT_EXIST
        return responseDto

    existingBlueZone.name = blueZoneSchema.name
    existingBlueZone.description = blueZoneSchema.description
    # Update other attributes as needed

    db.commit()

    responseDto.status = OK
    responseDto.message = UPDATE_BLUE_ZONE_OK
    responseDto.data = existingBlueZone.dict()
    return responseDto

def filter(blueZonesFilterSchema: BlueZonesFilterSchema, db: Session) -> ResponseDto:
    """Método para obtener zonas azules disponibles por área, tipo de vehículo y fechas y horas
    Args:
        blueZonesFilterSchema (BlueZonesFilterSchema): esquema que contiene los datos para la búsqueda
        db (Session): sesión de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        ResponseDto: respuesta generica
    """
    responseDto = ResponseDto()
      # Alias para la tabla de reservaciones
    ReservationAlias = aliased(Reservation)
    
    start_date = blueZonesFilterSchema.start_date,
    finish_date = blueZonesFilterSchema.finish_date,
    
    # Subconsulta para contar las reservaciones por blue_zone_id que no se solapen con el rango especificado
    subquery = db.query(
        ReservationAlias.blue_zone_id,
        func.count(ReservationAlias.id).label('reservation_count')
    ).filter(
        and_(
            or_(
                (ReservationAlias.start_date <= start_date) & (ReservationAlias.finish_date == finish_date),
                (ReservationAlias.start_date >= start_date) & (ReservationAlias.finish_date == finish_date),
                (ReservationAlias.start_date == start_date) & (ReservationAlias.finish_date < finish_date),
                (ReservationAlias.start_date == start_date) & (ReservationAlias.finish_date > finish_date),
                (ReservationAlias.start_date < start_date) & (ReservationAlias.finish_date > finish_date),
                (ReservationAlias.start_date <= start_date) & (ReservationAlias.finish_date < finish_date) & (ReservationAlias.finish_date >= start_date),
                (ReservationAlias.start_date >=  start_date) & (ReservationAlias.finish_date > finish_date) & (ReservationAlias.start_date <= finish_date)
            ),
            ReservationAlias.place_type_id == blueZonesFilterSchema.placeTypeId,
        )
    ).group_by(ReservationAlias.blue_zone_id).subquery()

     # Consulta principal para obtener las zonas azules con reservaciones menores a la cantidad de plazas del tipo solicitado
    zones = db.query(
        BlueZone,
        func.coalesce(subquery.c.reservation_count, 0).label("cantidad_reservas"),
        (BlueZone.total_car_places - func.coalesce(subquery.c.reservation_count, 0)).label("places_free")
    ).outerjoin(
        subquery, BlueZone.id == subquery.c.blue_zone_id,
    ).filter(
            func.coalesce(subquery.c.reservation_count, 0) < BlueZone.total_car_places,
            BlueZone.area_id == blueZonesFilterSchema.areaId
    ).all()

    

    zones_output = [
        {
            "id": zone.id,
            "name": zone.name,
            "address": zone.address,
            "observation": zone.observation,
            "latitude": zone.latitude,
            "longitude": zone.longitude,
            "total_moto_places_free": places_free if blueZonesFilterSchema.placeTypeId == 1 else None,
            "total_car_places_free": places_free if blueZonesFilterSchema.placeTypeId == 2 else None,
            "area_id": zone.area_id
        } for zone, cantidad_reservas, places_free in zones
    ]

    responseDto.status = OK
    responseDto.message = GET_ALL_BLUE_ZONE_FREE
    responseDto.data = zones_output
    return responseDto

def delete(id: int, db: Session) -> ResponseDto:
    """
    Método para eliminar una zona azul existente
    Args:
        id (int): identificador de la zona azul a eliminar
        db (Session): sesión de la base de datos que se recibe desde la ruta que fue llamada

    Returns:
        ResponseDto: respuesta generica
    """
    responseDto = ResponseDto()
    existingBlueZone = db.query(BlueZone).filter_by(id=id).first()
    if not existingBlueZone:
        responseDto.status = BAD_REQUEST
        responseDto.message = BLUE_ZONE_NOT_EXIST
        return responseDto

    db.delete(existingBlueZone)
    db.commit()

    responseDto.status = OK
    responseDto.message = "Blue zone deleted successfully"
    return responseDto
