from fastapi.security import HTTPBearer
from fastapi import Depends, HTTPException, Request
from .JWTService import decodeJwt
from sqlalchemy.orm import Session
from config.dB import getDb

from models.authUser import AuthUser
from helpers.mantainRole import MantainRole



class VerifyRole(HTTPBearer):
    async def __call__(self, request: Request, db: Session = Depends(getDb)):
        credentials = await super().__call__(request)
        reqBody = credentials.credentials
        if reqBody.__contains__('"'):
            reqBody = reqBody.replace('"', "")
        data = decodeJwt(reqBody)
        role = MantainRole(db)
        if data:
            user = db.query(AuthUser).filter(AuthUser.email == data["email"]).first()            
            roleName=user.role.name
            res = role.verifyPermit(data["role_id"], roleName)
            if res:
                return credentials
            else:
                raise HTTPException(
                    status_code=403, detail="No tienes permiso para realizar esta acción"
                )
        else:
            raise HTTPException(status_code=403, detail="No tienes permiso para realizar esta acción")
