from typing import List
from sqlalchemy.orm import Session
from schemas.reportSchema import reportSchema
from helpers.dtos.responseDto import ResponseDto
from helpers.statusCodes import BAD_REQUEST, OK
from helpers.responseMessages import GENERATE_REPORT_OK
from datetime import datetime
from typing import List
from sqlalchemy.orm import Session
from schemas.reportSchema import reportSchema
from helpers.dtos.responseDto import ResponseDto
from helpers.statusCodes import BAD_REQUEST, OK
from helpers.responseMessages import GENERATE_REPORT_OK
from models.reservation import Reservation


def total_revenue(report: reportSchema, db: Session) -> ResponseDto:
    responseDto = ResponseDto()
    
    start_date = datetime.strptime(report.startDate, '%Y-%m-%d %H:%M:%S')
    end_date = datetime.strptime(report.endDate, '%Y-%m-%d %H:%M:%S')

    reservations = db.query(Reservation).filter(
        Reservation.blue_zone_id == report.idZone,
        Reservation.start_date >= start_date,
        Reservation.start_date < end_date
    ).all()

    total_revenue = sum(reservation.total_price for reservation in reservations)
    report_data = {
        "total_revenue": total_revenue,
        "zone_id": report.idZone
    }

    responseDto.data = report_data
    responseDto.status = OK
    responseDto.message = GENERATE_REPORT_OK
    responseDto.data = report_data
    return responseDto