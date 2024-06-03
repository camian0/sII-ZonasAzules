from .meta import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKeyConstraint, VARCHAR
from sqlalchemy.orm import relationship

class Reservation(Base):
    __tablename__ = "reservations"
    
    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime, nullable=False)
    finish_date = Column(DateTime, nullable=False)
    plate = Column(VARCHAR(50), nullable=False)
    user_id = Column(Integer, nullable=False)
    place_type_id = Column(Integer, nullable=False)
    blue_zone_id = Column(Integer, nullable=False)

    user = relationship("User", back_populates="reservations")
    place_type = relationship("PlaceType", back_populates="reservations")
    blue_zone = relationship("BlueZone", back_populates="reservations")

    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_reservations_user_id'),
        ForeignKeyConstraint(['place_type_id'], ['place_types.id'], name='fk_reservations_place_type_id'),
        ForeignKeyConstraint(['blue_zone_id'], ['blue_zones.id'], name='fk_reservations_blue_zone_id'),
    )