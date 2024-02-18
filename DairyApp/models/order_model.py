#!/usr/bin/env python3
# from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func

# from DairyApp.libs.dblib.base import Base


# class Order(Base):
#     __tablename__ = 'orders'

#     id = Column(Integer, primary_key=True)
#     order_date = Column(DateTime(timezone=True), server_default=func.now())
#     quantity = Column(Float)
    
#     product_id = Column(Integer, ForeignKey('products.id'))
#     product = relationship('Product')

#     customer_id = Column(Integer, ForeignKey('customers.id'))
#     customer = relationship('Customer', back_populates='orders')

#     delivery_boy_id = Column(Integer, ForeignKey('delivery_boys.id'))
#     delivery_boy = relationship('DeliveryBoy', back_populates='orders')
