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
        """
        Function to add owner into DB
        Input  : Get all owners
        Output : LIST[DICT{owners}]
        """

        try:
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

            return owners_list
        except Exception as ex:
            session.rollback()
            raise ex
        finally:
            session.close()
    
    def get_owner_using_id(self,uid):   # id, name, emailid
        """Get specific owner"""    
        try:
            # create a new session
            session = Session()

            # Get column names from the model
            columns = OwnerModel.__table__.columns.keys()

            # Retrieve perticular row using id from the database table
            #user = session.query(OwnerModel).get({"id": uid}) 
            user = session.query(OwnerModel).filter(OwnerModel.id == uid)
            print(type(user)) 
            
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
            raise ex
        finally:
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

    def update_owner(self, new_owner):
        """
        Function to update owner into DB
        Input  : Owner Model
        Output : Int ; Number of owner updated
        """
        # TODO - Revisit for appropriate return value
        print("In lib : new_owner {}".format(str(new_owner)))
        try: 
            session = Session()

            #Check user is present in DB
            user_present = session.query(OwnerModel).filter(OwnerModel.email == new_owner["email"]).first()

            if user_present :
                #Update perticular field
                #user = session.query(OwnerModel).filter(OwnerModel.email == new_owner["email"]).update({"address" : new_owner["address"]})

                #Update row using model
                rows_updated = session.query(OwnerModel).filter(OwnerModel.email == new_owner["email"]).update(new_owner)
                print("No of rows updated : {}".format(str(rows_updated)))
                session.commit()
                return rows_updated
            
            return 0
            
        except Exception as ex:
            session.rollback()
            raise ex
        finally:
            # if session open
            session.close()

