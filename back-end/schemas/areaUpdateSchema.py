from pydantic import BaseModel


class AreaUpdateSchema(BaseModel):
    id: int
    name: str