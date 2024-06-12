from .meta import Base
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship


class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), unique=True, nullable=False)

    roles = relationship(
        "Role", secondary="role_menus", back_populates="menus", lazy="noload"
    )

    def dict(self):
        return {"id": self.id, "name": self.name}
