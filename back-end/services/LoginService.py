from sqlalchemy.orm import Session
from helpers.CryptDecrypt import verifyPassword

from models.AuthUser import AuthUser
from schemas.UserAuthSchema import UserAuthSchema
from services.JWTService import encodeJwt


def login(userAuth: UserAuthSchema, db: Session) -> str | None:
    query = db.query(AuthUser).filter(userAuth.email == AuthUser.email).first()

    if query:
        if verifyPassword(userAuth.password, query.password):
            setattr(userAuth, "role_id", query.role_id)
            token = encodeJwt(userAuth.__dict__)
            return token

    return None
