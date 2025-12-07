from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base
class Users(Base):
    __tablename__ = 'public.users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    roleId = Column(Integer, nullable=False)
    isDeleted = Column(Boolean, nullable=True)