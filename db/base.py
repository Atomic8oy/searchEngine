from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import MYSQL_URL

engine = create_engine(
    url=MYSQL_URL,
    pool_size=10,
    max_overflow=30,
    pool_recycle=3600,
    pool_timeout=10
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
