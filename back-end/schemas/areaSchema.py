from pydantic import BaseModel
from pydantic import field_validator


class AreaSchema(BaseModel):
    name: str

    @field_validator('name')
    def name_not_none(cls, value):
        if value is None:
            raise ValueError('El nombre es requerido')
        return value