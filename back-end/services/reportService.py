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


def total_revenue(db: Session, report: reportSchema) -> ResponseDto:
    responseDto = ResponseDto()
    
    start_date = datetime.strptime(report.start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(report.end_date, "%Y-%m-%d").date()

    reservations = db.query(Reservation).filter(
        Reservation.zone_id == report.zone_id,
        Reservation.date >= start_date,
        Reservation.date <= end_date
    ).all()

    total_revenue = sum(reservation.total_price for reservation in reservations)
    report_data = {
        "total_revenue": total_revenue,
        "zone_id": report.zone_id
    }

    responseDto.data = report_data
    responseDto.status = OK
    responseDto.message = GENERATE_REPORT_OK
    responseDto.data = report_data
    return responseDto