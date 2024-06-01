from config.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Reservation(Base):
    __tablename__ = "reservations"
    
    id = Column(Integer, primary_key=True, index=True)

    places = relationship("Place", secondary="place_reservations", back_populates="reservations")