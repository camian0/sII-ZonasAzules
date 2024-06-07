from pydantic import BaseModel
from datetime import datetime

class BlueZonesFilterSchema(BaseModel):
    areaId: int
    placeTypeId: int
    start_date: datetime
    finish_date: datetime