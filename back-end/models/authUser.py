from .meta import Base
from sqlalchemy import Column, Integer, VARCHAR, ForeignKeyConstraint
from sqlalchemy.orm import relationship


class AuthUser(Base):
    __tablename__ = "auth_users"

    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(255), unique=True, nullable=False)
    password = Column(VARCHAR(255), nullable=False)
    role_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)

    role = relationship("Role", back_populates="auth_users")
    user = relationship("User", back_populates="auth_users")

    __table_args__ = (
        ForeignKeyConstraint(["role_id"], ["roles.id"], name="fk_auth_user_role_id"),
        ForeignKeyConstraint(["user_id"], ["users.id"], name="fk_auth_user_user_id"),
    )

    def dict(self):
        return {"email": self.email}
