from .base import Base
from datetime import datetime
from sqlalchemy import (BigInteger, Column, DateTime, String)


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    name = Column(String(100), unique=True)
    email = Column(String(150))
    province = Column(String(100))
    city =  Column(String(50))
    major = Column(String(150))