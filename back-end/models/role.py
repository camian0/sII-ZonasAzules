from config.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Role(Base):
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True)
    

    # Definir la relación con la tabla 'auth_users'
    auth_users = relationship("AuthUser", back_populates="role")