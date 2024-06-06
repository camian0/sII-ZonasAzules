from pydantic import BaseModel
from datetime import datetime

class ReservationSchema(BaseModel):
    start_date: datetime
    finish_date: datetime
    plate: str
    user_id: int
    place_type_id: int
    blue_zone_id: int
    