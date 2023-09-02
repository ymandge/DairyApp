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
        finally:
            # if session open
            session.close() 

        # TODO - Return approprivate value

    def get_all_owner(self):
        """Get all owners"""

        # create a new session
        session = Session()
        query = session.query(OwnerModel)
        session.close()
    
    def get_owner(uname):   # id, name, emailid
        """Get specific owner"""

    def delete_owner(uname):
        """Delete owner"""

    def update_owner():
        """Update"""

