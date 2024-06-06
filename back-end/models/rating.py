from .meta import Base
from sqlalchemy import Column, Integer, String, ForeignKeyConstraint, Text
from sqlalchemy.orm import relationship


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True)
    qualification = Column(Integer, nullable=False)
    observation = Column(String(2000), nullable=False)
    blue_zone_id = Column(Integer, nullable=False)

    blue_zone = relationship("BlueZone", back_populates="ratings", lazy="noload")

    __table_args__ = (
        ForeignKeyConstraint(
            ["blue_zone_id"], ["blue_zones.id"], name="fk_blue_zones_blue_zone_id"
        ),
    )

    def dict(self):
        return {
            "id": self.id,
            "qualification": self.qualification,
            "aboservation": self.observation,
            "blue_zone_id": self.blue_zone_id,
        }
