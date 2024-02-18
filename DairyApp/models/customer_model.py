"""This file defines the customer model"""

#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String, DateTime, Date, Boolean

from DairyApp.libs.dblib.base import Base
from datetime import datetime


# id, name, address, mobile, email, dob, oid, registered_for_msg, profile_photo, date_created, date_updated

class CustomerModel(Base):

    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id = Column(Integer)
    name = Column(String)
    address = Column(String)
    mobile = Column(String(length=12))
    email = Column(String)
    dob = Column(Date)
    registered_for_msg = Column(Boolean, default=False)
    #profile_picture = Column(Blob, default="")
    date_created = Column(DateTime, default=datetime.utcnow)
    date_updated = Column(DateTime, default=datetime.utcnow)

    def __init__(self, name, address, mobile, dob, email, owner_id, registered_for_msg=False):
        print("Inside customer __init__")
        self.owner_id = owner_id
        self.name = name
        self.address = address
        self.mobile = mobile
        self.email = email
        self.dob = dob
        self.registered_for_msg = registered_for_msg
