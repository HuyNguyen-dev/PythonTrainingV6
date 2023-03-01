from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, TIMESTAMP,BOOLEAN
from  app import app,db

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer,primary_key=True, nullable=False,autoincrement=True)
    username = Column(String(255),nullable=False,unique=True)
    full_name = Column(String(255),default=None)
    email = Column(String(255),nullable=False,unique=True)
    phone_number = Column(String(255),default=None)
    report_access = Column(BOOLEAN,default=None)
    view_costs = Column(BOOLEAN,default=None)
    last_login_date = Column(TIMESTAMP,default=None)
    enabled = Column(BOOLEAN,nullable=False,default=True,server_default='1')
    is_corporated = Column(BOOLEAN,nullable=False,default=False,server_default='0')
    created_on = Column(DateTime,default=None)
    modified_on = Column(DateTime,default=None)

    def __str__(self) -> str:
        return self.username
    
class Organization(db.Model):
    __tablename__ = "organization"
    id = Column(Integer,primary_key=True, nullable=False,autoincrement=True)
    username = Column(String(255),nullable=False,unique=True)
    
    def __str__(self) -> str:
        return self.username
    
class Test(Base):
    __tablename__ = "test"
    id = Column(Integer,primary_key=True, nullable=False,autoincrement=True)
    username = Column(String(255),nullable=False,unique=True)
    full_name = Column(String(255),default=None)
    email = Column(String(255),nullable=False,unique=True)
    phone_number = Column(String(255),default=None)
    created_on = Column(DateTime,default=datetime.utcnow)

with app.app_context():
    db.create_all()
