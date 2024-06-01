from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base

class PlaceReservation(Base):
    __tablename__ = 'place_reservations'
    
    id = Column(Integer, primary_key=True, index=True)
    
    place_id = Column(Integer, ForeignKey('places.id'), primary_key=True)
    reservation_id = Column(Integer, ForeignKey('reservations.id'), primary_key=True)
    
    place = relationship("Place", back_populates="reservations")
    reservation = relationship("Reservation", back_populates="places")