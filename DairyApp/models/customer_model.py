"""This file defines the customer model"""

#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String, DateTime, Date, Boolean

from DairyApp.libs.dblib.base import Base
from datetime import datetime


# id, name, address, mobile, email, dob, oid, registered_for_msg, profile_photo, date_created, date_updated

class CustomerModel(Base):

    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    address = Column(String)
    mobile = Column(Integer)
    email = Column(String)
    dob = Column(Date)
    oid = Column(Integer)
    registered_for_msg = Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.utcnow)

    def __init__(self, name, address, mobile, dob, email, oid):
        print("Inside customer __init__")
        self.name = name
        self.address = address
        self.mobile = mobile
        self.dob = dob
        self.email = email
        self.oid = oid
