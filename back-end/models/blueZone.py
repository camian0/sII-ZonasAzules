from .meta import Base
from sqlalchemy import Column, Integer, VARCHAR, Float, String, ForeignKeyConstraint
from sqlalchemy.orm import relationship


class BlueZone(Base):
    __tablename__ = "blue_zones"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), unique=True, nullable=False)
    address = Column(VARCHAR(100), nullable=False)
    observation = Column(String(200))
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    total_car_places = Column(Integer, nullable=False)
    total_moto_places = Column(Integer, nullable=False)
    area_id = Column(Integer, nullable=False)

    area = relationship("Area", back_populates="blue_zones", lazy="noload")
    reservations = relationship(
        "Reservation", back_populates="blue_zone", lazy="noload"
    )

    __table_args__ = (
        ForeignKeyConstraint(["area_id"], ["areas.id"], name="fk_blue_zones_area_id"),
    )
