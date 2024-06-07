from pydantic import BaseModel, field_validator
from datetime import datetime


class ReservationSchema(BaseModel):
    id: int
    start_date: str
    finish_date: str
    plate: str
    user_id: int
    place_type_id: int
    blue_zone_id: int
    

    @field_validator("plate")
    def plateValid(cls, plate):

        if len(plate) > 6:
            raise ValueError("La longitud de la placa debe ser máximo de 6 dígitos")

        return plate

    