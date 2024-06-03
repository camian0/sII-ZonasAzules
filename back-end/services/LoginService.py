from sqlalchemy.orm import Session

from helpers.CryptDecrypt import verifyPassword
from models.authUser import AuthUser
from models.user import User
from schemas.UserAuthSchema import UserAuthSchema
from services.JWTService import encodeJwt


def login(userAuth: UserAuthSchema, db: Session) -> str | None:
    query = db.query(AuthUser).filter(userAuth.email == AuthUser.email).first()
    if query:
        if verifyPassword(userAuth.password, query.password):
            userAuth.role_id = query.role_id
            token = encodeJwt(userAuth.__dict__)
            return token
    return None


def createAuthUser(user: AuthUser, db: Session) -> True:
    if user:
        db.add(user)
        db.commit()
        db.refresh(user)
        return True
    return False
