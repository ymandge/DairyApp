#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String, DateTime, Date

from DairyApp.libs.dblib.base import Base
from datetime import datetime

class OwnerModel(Base):

    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    address = Column(String)
    mobile = Column(Integer)
    email = Column(String)
    dob = Column(Date)
    date_created = Column(DateTime, default=datetime.utcnow)
    password = Column(String)
    #id, name, address, mobile, dob, licence, secret(password + salt), email, uname, profile_photo, date_created, date_updated
    
    # dob = Column(Date)
    # secret = secret(password + salt)
    # licence
    # uname
    # profile_photo = Column(Blob)
    # date_updated

    def __init__(self, name, address, mobile, dob, email, password):
        self.name = name
        self.address = address
        self.mobile = mobile
        self.dob = dob
        self.email = email
        self.password = password 

    # def __repr__(self):
    #     return "<User(id='%s', name='%s')>" % (
    #         self.id, self.name)
