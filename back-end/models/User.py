from config.dB import Base
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    names = Column(VARCHAR(50))
    last_names = Column(VARCHAR(50))
    telephone = Column(VARCHAR(20))
    auth_user_id = Column(Integer, ForeignKey("auth_users.id"), nullable=False)
    auth_user = relationship("AuthUser", back_populates="User")

    def dict(self):
        return {
            "names": self.names,
            "lastNames": self.last_names,
            "telephone": self.telephone,
            "authUser": self.auth_user,
        }
