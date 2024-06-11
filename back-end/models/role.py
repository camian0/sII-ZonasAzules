from .meta import Base
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), unique=True, nullable=False)

    auth_users = relationship("AuthUser", back_populates="role")
    menus = relationship("Menu", secondary="role_menus", back_populates="roles")

    def getMenus(self)->list[dict]:
        """
        Método para obtener los menus permitidos asociados al rol

        Returns:
            list[dict]: Devuelve un diccionario con los permisos que tiene el rol
        """              
        menus = []
        for item in self.menus:
            menus.append({f"{item.name}": True})

        return menus
