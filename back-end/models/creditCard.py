from .meta import Base
from sqlalchemy import Column, Integer, ForeignKeyConstraint, VARCHAR
from sqlalchemy.orm import relationship
from datetime import datetime


class CreditCard(Base):
    __tablename__ = "credit_cards"

    id = Column(Integer, primary_key=True)
    number = Column(VARCHAR(255), nullable=False, unique=True)
    titular_name = Column(VARCHAR(255), nullable=False)
    cvc = Column(VARCHAR(255), nullable=False)
    expiry_date = Column(VARCHAR(5), nullable=False)
    user_id = Column(Integer, nullable=False)



    user = relationship("User", back_populates="credit_cards", lazy="noload")

    __table_args__ = (
        ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_credit_cards_user_id"),
    )

    def dict(self):
        return {
            "titular_name": self.titular_name,
            "number": self.number,
            "cvc": self.cvc,
            "expiry_date": self.expiry_date,
            "user_id": self.user_id,
        }
