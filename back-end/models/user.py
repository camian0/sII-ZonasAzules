from .meta import Base
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    names = Column(VARCHAR(255), nullable=False)
    last_names = Column(VARCHAR(255), nullable=False)
    phone = Column(VARCHAR(255), nullable=True)
    document = Column(VARCHAR(255), unique=True, nullable=False)

    auth_users = relationship("AuthUser", back_populates="user")
    credit_cards = relationship("CreditCard", back_populates="user")
    reservations = relationship("Reservation", back_populates="user")

    def dict(self):
        return {
            "names": self.names,
            "last_names": self.last_names,
            "phones": self.phone,
            "document": self.document,
            "auth_users": self.auth_users,
            "credic_cards": self.credit_cards,
            "reservations": self.reservations,
        }
