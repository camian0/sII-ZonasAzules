from .meta import Base
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship


class PlaceType(Base):
    __tablename__ = "place_types"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), unique=True, nullable=False)

    reservations = relationship("Reservation", back_populates="place_type")
