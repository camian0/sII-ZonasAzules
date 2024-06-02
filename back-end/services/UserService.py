from typing import List
from sqlalchemy.orm import Session
from models.user import User


def getUsers(db: Session) -> List[User] | None:
    query = db.query(User).all()
    if len(query) > 0:
        return query
    return None
