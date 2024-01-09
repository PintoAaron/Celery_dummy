from sqlalchemy import Integer, String, Column, Boolean 
from db import Base



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    is_active = Column(Boolean, default=False)

