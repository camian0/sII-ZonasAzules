from sqlalchemy import Column, Integer, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from config.db import Base

class PlaceReservation(Base):
    __tablename__ = 'place_reservations'
    
    id = Column(Integer, primary_key=True)
    
    place_id = Column(Integer, primary_key=True, nullable=False)
    reservation_id = Column(Integer, primary_key=True, nullable=False)
    
    place = relationship("Place", back_populates="reservations")
    reservation = relationship("Reservation", back_populates="places")

    __table_args__ = (
        ForeignKeyConstraint(['place_id'], ['places.id'], name='fk_place_reservations_place_id'),
        ForeignKeyConstraint(['reservation_id'], ['reservations.id'], name='fk_place_reservations_reservation_id')
    )