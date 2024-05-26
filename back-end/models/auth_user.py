from config.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

metadata = Base.metadata

class AuthUser(Base):
    __tablename__ = "auth_users"
    
    id = Column(Integer, primary_key=True, index=True)
    # password = Column(String(255), unique=True)    
    role_id = Column(Integer, ForeignKey('roles.id'))
    
    role = relationship("Role", back_populates="auth_users", foreign_keys=[role_id])
    