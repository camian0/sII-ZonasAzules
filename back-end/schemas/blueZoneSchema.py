from pydantic import BaseModel

class BlueZoneSchema(BaseModel):
    name: str
    address: str
    observation: str
    latitude: float
    longitude: float
    total_car_places: int
    total_moto_places: int
    price_car: float
    price_moto: float
    area_id: int