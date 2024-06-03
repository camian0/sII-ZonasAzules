from .meta import Base
from sqlalchemy import Column, Integer, ForeignKeyConstraint, VARCHAR
from sqlalchemy.orm import relationship


class CreditCard(Base):
    __tablename__ = "credit_cards"

    id = Column(Integer, primary_key=True)
    number = Column(VARCHAR(255), nullable=False, unique=True)
    titular_name = Column(VARCHAR(255), nullable=False)
    cvc = Column(VARCHAR(255), nullable=False)
    user_id = Column(Integer, nullable=False)

    user = relationship("User", back_populates="credit_cards")

    __table_args__ = (
        ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_credit_cards_user_id"),
    )
