from pydantic import BaseModel


class reportSchema(BaseModel):
    startDate: str
    endDate: str
    idZone: str