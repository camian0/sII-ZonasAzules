from datetime import datetime
from pydantic import BaseModel
from pydantic import BaseModel, Field
from pydantic import field_validator

class reportSchema(BaseModel):
    startDate: str
    endDate: str
    idZone: str

    '''
    Verifica que la fecha esté en formato yyyy-MM-dd hh:mm:ss
    '''
    @field_validator("startDate")
    def validate_date(cls, startDate):
        try:
            exp_date = datetime.strptime(startDate, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError("La fecha debe tener el formato yyyy-MM-dd hh:mm:ss")
        
        return startDate
    
    '''
    Verifica que la fecha esté en formato yyyy-MM-dd hh:mm:ss
    '''
    @field_validator("endDate")
    def validate_date(cls, endDate):
        try:
            exp_date = datetime.strptime(endDate, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError("La fecha debe tener el formato yyyy-MM-dd hh:mm:ss")
        
        return endDate