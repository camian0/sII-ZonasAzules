from config.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Place(Base):
    __tablename__ = "places"
    
    id = Column(Integer, primary_key=True, index=True)

    reservations = relationship("Reservation", secondary="place_reservations", back_populates="places")