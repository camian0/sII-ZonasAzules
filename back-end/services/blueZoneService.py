from typing import List
from sqlalchemy.orm import Session

from models.blueZone import BlueZone
from helpers.helpers import queryPaginate


def get(db: Session, page: int, sizePage: int) -> List[BlueZone] | None:
    query = db.query(BlueZone)
    res = queryPaginate(query, page, sizePage)
    if len(res) > 0:
        zones = [i.dict() for i in query]
        return zones
    return None
