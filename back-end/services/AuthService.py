from fastapi.security import HTTPBearer
from fastapi import Depends, HTTPException, Request

from .JWTService import decodeJwt
from sqlalchemy.orm import Session
from config.DB import getDb

from models.AuthUser import AuthUser


class AuthService(HTTPBearer):
    async def __call__(self, request: Request, db: Session = Depends(getDb)):
        credentials = await super().__call__(request)
        reqBody = credentials.credentials
        if reqBody.__contains__('"'):
            reqBody = reqBody.replace('"', "")
        data = decodeJwt(reqBody)

        if data:
            user = db.query(AuthUser).filter(AuthUser.email == data["email"]).first()
            if user:
                return credentials
            else:
                raise HTTPException(
                    status_code=403, detail="Invalid authorization code"
                )
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code")
