from config.db import Base
from sqlalchemy import Column, Integer, DateTime, ForeignKeyConstraint
from sqlalchemy.orm import relationship

class Reservation(Base):
    __tablename__ = "reservations"
    
    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime, nullable=False)
    finish_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, nullable=False)

    user = relationship("User", back_populates="reservations")
    places = relationship("Place", secondary="place_reservations", back_populates="reservations")

    __table_args__ = (
        ForeignKeyConstraint(['user_id'], ['users.id'], name='fk_reservations_user_id'),
    )