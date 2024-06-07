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

    user = relationship("User", back_populates="reservations", lazy="noload")
    place_type = relationship("PlaceType", back_populates="reservations", lazy="noload")
    blue_zone = relationship("BlueZone", back_populates="reservations", lazy="noload")

    __table_args__ = (
        ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_reservations_user_id"),
        ForeignKeyConstraint(
            ["place_type_id"], ["place_types.id"], name="fk_reservations_place_type_id"
        ),
        ForeignKeyConstraint(
            ["blue_zone_id"], ["blue_zones.id"], name="fk_reservations_blue_zone_id"
        ),
    )

    def dict(self):
        return {
            "id": self.id,
            "start_date": self.start_date.isoformat(),
            "finish_date": self.finish_date.isoformat(),
            "plate": self.plate,
            "user_id": self.user_id,
            "place_type_id": self.place_type_id,
            "blue_zone_id": self.blue_zone_id,
        }
