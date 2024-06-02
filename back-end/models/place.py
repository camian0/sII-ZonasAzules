from config.db import Base
from sqlalchemy import Column, Integer, ForeignKeyConstraint
from sqlalchemy.orm import relationship

class Place(Base):
    __tablename__ = "places"
    
    id = Column(Integer, primary_key=True)
    blue_zone_id = Column(Integer, nullable=False)
    place_state_id = Column(Integer, nullable=False)
    place_type_id = Column(Integer, nullable=False)

    reservations = relationship("Reservation", secondary="place_reservations", back_populates="places")
    blue_zones = relationship("BlueZone", back_populates="places")
    place_state = relationship("PlaceState", back_populates="places")
    place_type = relationship("PlaceType", back_populates="places")

    __table_args__ = (
        ForeignKeyConstraint(['blue_zone_id'], ['blue_zones.id'], name='fk_places_blue_zone_id'),
        ForeignKeyConstraint(['place_state_id'], ['place_states.id'], name='fk_places_place_state_id'),
        ForeignKeyConstraint(['place_type_id'], ['place_types.id'], name='fk_places_place_type_id')
    )