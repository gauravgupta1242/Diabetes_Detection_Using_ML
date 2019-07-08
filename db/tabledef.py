from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///registered.db', echo=True)
Base = declarative_base()
 
########################################################################
class User(Base):
    """"""
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    mail_id  = Column(String)
    phone_number = Column(Integer)
    
    #----------------------------------------------------------------------
    def __init__(self, username, password,mail_id ,phone_number):
        """"""
        self.username = username
        self.password = password
        self.mail_id =  mail_id
        self.phone_number = phone_number
 
# create tables
Base.metadata.create_all(engine)



class abc(Base):
    
    __tablename__ = "medical"

    id = Column(Integer, primary_key=True)
    blood_pressure = Column(Integer)
    insuline = Column(Integer)
    bmi = Column(Integer)
    dpf = Column(Integer)
    age = Column(Integer)
    
    #----------------------------------------------------------------------
    def __init__(self, blood_pressure, insuline, bmi , dpf, age):
        """"""
        self.blood_pressure = blood_pressure
        self.insuline = insuline
        self.bmi = bmi
        self.dpf = dpf 
        self.age = age


# create tables
Base.metadata.create_all(engine)
