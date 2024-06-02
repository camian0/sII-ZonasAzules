from config.db import Base
from sqlalchemy import Column, Integer, VARCHAR, Float,String, ForeignKeyConstraint
from sqlalchemy.orm import relationship

class BlueZone(Base):
    __tablename__ = "blue_zones"
    
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), unique=True, nullable=False)
    address = Column(VARCHAR(100), nullable=False)
    observation = Column(String(200))
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    total_vacancy_moto = Column(Integer, nullable=False)
    total_busy_occupied = Column(Integer, nullable=False)
    total_vacancy_car = Column(Integer, nullable=False)
    total_busy_car = Column(Integer, nullable=False)
    area_id = Column(Integer, nullable=False)  # Definición de la clave foránea

    area = relationship("Area", back_populates="bule_zones")
    places = relationship("Place", back_populates="bule_zone")

    __table_args__ = (
        ForeignKeyConstraint(['area_id'], ['areas.id'], name='fk_blue_zones_area_id'),
    )