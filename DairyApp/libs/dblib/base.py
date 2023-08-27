#!/usr/bin/env python
#from functools import wraps

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker #, scoped_session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://postgres:a@localhost:5432/dairyappdb', echo=True, pool_pre_ping=True)

Session = sessionmaker(bind=engine)



# Session = scoped_session(session_factory)

# def get_session():
#     """
#     :return: Session
#     """
#     return Session()

# def transaction(function):
#     @wraps(function)
#     def get_session_for_transaction(*args, **kwargs):
#         session = get_session()
#         try:
#             result = function(*args, **kwargs)
#             session.commit()
#             return result
#         except Exception as ex:
#             session.rollback()
#             raise ex
#         finally:
#             session.close()

#     return get_session_for_transaction


Base = declarative_base()


# def create_all():
#     """
#     Create database tables.
#     """
#     Base.metadata.create_all(engine)