from pydantic import BaseModel, Field


class UserAuthSchema(BaseModel):

    email: str = Field(
        pattern="^([\w\.\-]+)@([\w\-]+)((\.(\w){2,3})+)$", default="email@server.com"
    )
    password: str
