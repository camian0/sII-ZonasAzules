from config.DB import Base
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship


class Role(Base):
    __tablename__ = "roles"

    id = Column(VARCHAR(20), primary_key=True, index=True)
    name = Column(VARCHAR(50), unique=True)

    def dict(self):
        return {
            "name": self.name,
        }
