"This file will handle database interaction for customer operations"

#from DairyApp.models.customer_model import CustomerModel
from DairyApp.libs.dblib.base import Session

class CustomerLib:
    """This class is for customer operations"""

    def __init__(self):
        """ctor"""

    def add_customer(self, customer):
        """Function for adding customer into db"""

        try:
            session = Session()
            session.add(customer)
            session.commit()
            session.close()
        except Exception as ex:
            session.rollback()
        finally:
            # if session open
            session.close() 

        # TODO - Return approprivate value