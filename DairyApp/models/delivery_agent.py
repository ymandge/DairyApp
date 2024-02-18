#!/usr/bin/env python3
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship

# from DairyApp.libs.dblib.base import Base

# class DeliveryBoy(Base):
#     __tablename__ = 'delivery_agents'

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     # Add any other DeliveryBoy-specific fields here

#     dairy_owner_id = Column(Integer, ForeignKey('owners.id'))
#     dairy_owner = relationship('DairyOwner', back_populates='delivery_agents')
#     orders = relationship('Order', back_populates='delivery_agents')
