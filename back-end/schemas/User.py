from pydantic import BaseModel, EmailStr
from pydantic import field_validator


class UserSchema(BaseModel):
    names: str
    last_names: str
    phone: str
    document: str
    password: str
    email: EmailStr

    @field_validator("password")
    def passwordName(cls, password):

        if len(password) < 8:
            raise ValueError("La longitud mínima  es de 8 caracteres.")

        return password
