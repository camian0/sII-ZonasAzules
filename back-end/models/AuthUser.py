from config.DB import Base
from sqlalchemy import Column, Integer, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship


class AuthUser(Base):
    __tablename__ = "auth_users"

    id = Column(VARCHAR(20), primary_key=True, index=True)
    email = Column(VARCHAR(50), unique=True)
    password = Column(VARCHAR(100))
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    role = relationship("role")

    def dict(self):
        return {
            "email": self.email,
        }
