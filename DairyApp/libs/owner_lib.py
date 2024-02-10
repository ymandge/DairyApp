"""
This is low level lib file for handling various owner operations
by interacting with db using SQLAlchemy.
"""

from DairyApp.models.owner_model import OwnerModel
from DairyApp.libs.dblib.base import Session

class OwnerLib:
    """This class is for owner operations"""

    def __init__(self):
        """ctor"""

    def add_owner(self, owner):
        """
        Function to add owner into DB
        Input  : Owner Model
        Output : boolean ; Success(True), Failure(False) 
        """
        # TODO - Revisit for appropriate return value
        
        try:
            session = Session()
            session.add(owner)
            session.commit()
        except Exception as ex:
            session.rollback()
            raise ex
        finally:
            # if session open
            session.close() 

       

    def get_all_owner(self):
        """Get all owners"""

        # create a new session
        session = Session()

        # Retrieve all rows from the database table
        all_rows = session.query(OwnerModel).all()
        print(type(all_rows)) 
        # Get column names from the model
        columns = OwnerModel.__table__.columns.keys()

        # Print column names
        print("Column Names:", columns)

        # Print all rows with column values
        owners_list = []
        for row in all_rows:
            owner_dict = {}
            for column in columns:
                if column == "dob" or column == "date_created":
                    owner_dict[column] = str(getattr(row, column))
                else:
                    owner_dict[column] = getattr(row, column)

            owners_list.append(owner_dict)

        # rows = session.query(OwnerModel).all()
        # # Convert the rows to a list of dicts
        # dict_rows = list(map(dict, rows))
        # print(dict_rows)
            
        session.close()
        return owners_list
    
    def get_owner_using_id(self,uid):   # id, name, emailid
        """Get specific owner"""    
        try:
            # create a new session
            session = Session()
            print("in owner lib")

            # Get column names from the model
            columns = OwnerModel.__table__.columns.keys()

            # Retrieve perticular row using id from the database table
            print("OwnerLib User id = " + str(uid))
            #user = session.query(OwnerModel).get({"id": uid})
           
            user = session.query(OwnerModel).filter(OwnerModel.id == uid)
            print(type(user)) 
            
            columns = OwnerModel.__table__.columns.keys()

            # # Print all rows with column values
            owners_list = []
           
            for row in user:
                owner_dict = {}
                for column in columns:
                    if column == "dob" or column == "date_created":
                        owner_dict[column] = str(getattr(row, column))
                    else:
                        owner_dict[column] = getattr(row, column)

                owners_list.append(owner_dict)

            return owners_list
        except Exception as ex:
            session.rollback()
            print("in exception")
            print(str(ex))
            raise ex
        finally:
            # if session open
            print("in finally")
            session.close() 


    # def get_owner_using_name(self,uname):   # id, name, emailid
    #     """Get specific owner"""    
    #     try:
    #         # create a new session
    #         session = Session()
    #         print("in owner lib")
    #         # Retrieve perticular row using id from the database table
    #         print("OwnerLib User name = " + str(uname))
    #         user = session.query(OwnerModel).get({"name": uname})

    #         #print("User data = " + user)
    #         return user
    #     except Exception as ex:
    #         session.rollback()
    #         print("in exception")
    #         print(str(ex))
    #         raise ex
    #     finally:
    #         # if session open
    #         session.close() 

    def delete_owner(uname):
        """Delete owner"""

    def update_owner():
        """Update"""

