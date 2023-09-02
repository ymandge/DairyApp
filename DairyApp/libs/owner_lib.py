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
        """Function for adding owner into db"""

        try:
            session = Session()
            session.add(owner)
            session.commit()
            session.close()
        except Exception as ex:
            session.rollback()
            print(str(ex))
            raise ex
        finally:
            # if session open
            session.close() 

        # TODO - Return approprivate value

    def get_all_owner(self):
        """Get all owners"""

        # create a new session
        session = Session()
        #all_rows = session.query(OwnerModel).all()

                # Retrieve all rows from the database table
        all_rows = session.query(OwnerModel).all()

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
            
        session.close()
        return owners_list
    
    def get_owner(uname):   # id, name, emailid
        """Get specific owner"""

    def delete_owner(uname):
        """Delete owner"""

    def update_owner():
        """Update"""

