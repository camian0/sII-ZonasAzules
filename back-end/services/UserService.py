from typing import List
from sqlalchemy.orm import Session

from models.user import User
from models.authUser import AuthUser
from schemas.User import UserSchema
from helpers.CryptDecrypt import getPasswordHash
from services.LoginService import createAuthUser
from helpers.helpers import listRelationship


def getUsers(db: Session) -> List[User] | None:
    query = db.query(User).all()
    if len(query) > 0:
        users = [i.dict() for i in query]
        return users
    return None


def create(user: UserSchema, db: Session) -> bool:
    newUser = User()
    newUser.__dict__.update(user.__dict__)
    newAuthUser = AuthUser()
    passwordHash = getPasswordHash(newUser.password)
    newAuthUser.email = newUser.email
    newAuthUser.password = passwordHash
    newAuthUser.role_id = 2
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    newAuthUser.user_id = newUser.id
    result = createAuthUser(newAuthUser, db)
    if not result:
        db.rollback()
        return False

    return True
