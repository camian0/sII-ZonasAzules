from pydantic import BaseModel


class reportSchema(BaseModel):
    starDate: str
    endDate: str
    idZone: str