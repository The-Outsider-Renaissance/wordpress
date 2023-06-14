from sqlalchemy import Boolean, Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
    title = Column(String(255))
    avatar = Column(String(255))
    is_active = Column(Boolean, default=True)
