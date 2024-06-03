from .meta import Base
from sqlalchemy import Column, Integer, ForeignKeyConstraint
from sqlalchemy.orm import relationship


class RoleMenu(Base):
    __tablename__ = "role_menus"

    id = Column(Integer, primary_key=True, autoincrement=True)

    role_id = Column(Integer, primary_key=True, nullable=False)
    menu_id = Column(Integer, primary_key=True, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(["role_id"], ["roles.id"], name="fk_role_menus_role_id"),
        ForeignKeyConstraint(["menu_id"], ["menus.id"], name="fk_role_menus_menu_id"),
    )
