from pydantic import BaseModel
from pydantic import Field


# Clase de esquema para la estructura de los datos de usuario
class SearchBlueZoneSchema(BaseModel):
    id: int 
    areaId: int 
    typeVehicle: int 
    iniatialDate: str
    finalDate: str
