from pydantic import BaseModel, field_validator
from datetime import datetime


class ReservationSchema(BaseModel):
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
    
    '''
    Verifica que la fecha esté en formato yyyy-MM-dd hh:mm:ss
    '''
    @field_validator("start_date")
    def validate_date(cls, start_date):
        try:
            exp_date = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError("La fecha debe tener el formato yyyy-MM-dd hh:mm:ss")
        
        return start_date
    
    '''
    Verifica que la fecha esté en formato yyyy-MM-dd hh:mm:ss
    '''
    @field_validator("finish_date")
    def validate_date(cls, finish_date):
        try:
            exp_date = datetime.strptime(finish_date, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError("La fecha debe tener el formato yyyy-MM-dd hh:mm:ss")
        
        return finish_date

    