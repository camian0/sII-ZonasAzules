from config.db import Base
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship

class PlaceState(Base):
    __tablename__ = "place_states"
    
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), unique=True, nullable=False)

    places = relationship("Place", back_populates="place_state")    