from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP,BOOLEAN
from datetime import datetime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Organization(Base):
    __tablename__ = "organization"
    id = Column(Integer,primary_key=True, nullable=False,autoincrement=True)
    username = Column(String(255),nullable=False,unique=True)
    
    def __str__(self) -> str:
        return self.username