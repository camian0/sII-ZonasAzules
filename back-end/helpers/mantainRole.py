from typing import List
from sqlalchemy.orm import Session
from models.role import Role
from helpers.helpers import listRelationship


class MantainRole:
    created: bool

    def __init__(self, db: Session):
        self.roles: dict = {}
        self.db = db
        self.created=False
        self.__createMenuList()

    def __createMenuList(self):
        
        query = self.db.query(Role).all()
        if not self.created:
            for rol in query:
                menus = listRelationship(rol.menus)
                self.roles[rol.name]=[menu["id"] for menu in menus]
            

    def verifyPermit(self, role_id: int, roleName: str):
        for i in self.roles[roleName]:
            if i == role_id:
                return True
        return False
