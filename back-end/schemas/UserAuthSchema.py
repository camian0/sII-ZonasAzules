from pydantic import BaseModel, Field
from typing import Optional


class UserAuthSchema(BaseModel):

    email: str = Field(
        pattern="^([\w\.\-]+)@([\w\-]+)((\.(\w){2,3})+)$", default="email@server.com"
    )
    password: str
    role_id: Optional[int] = None
