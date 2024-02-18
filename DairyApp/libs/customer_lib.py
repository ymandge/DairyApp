"This file will handle database interaction for customer operations"

from sqlalchemy.orm import class_mapper

from DairyApp.libs.dblib.base import Session
from DairyApp.models.customer_model import CustomerModel


class CustomerLib:
    """This class is for customer operations"""

    def __init__(self):
        """ctor"""

    def add_customer(self, customer):
        """
        Function to add customer into DB
        Input  : Owner Model
        Output : ??
        """

        try:
            session = Session()
            session.add(customer)
            session.commit()
        except Exception as ex:
            session.rollback()
            raise ex
        finally:
            # if session open
            session.close() 

        # TODO - Return approprivate value


    def get_all_customers_by_owner_id(self, owner_id):
        """
        Function to get all customers for given owner id from DB
        Input  : Owner ID
        Output : All customers for given owner id
        """

        try:
            # create a new session
            session = Session()

            # Get table columns
            columns = [column.key for column in class_mapper(CustomerModel).columns]

            # Filter and fetch all rows with specified owner_id
            all_rows = session.query(CustomerModel).filter(CustomerModel.owner_id == owner_id).all()

            # Convert rows to dictionaries
            customer_list = [
                {column: getattr(row, column) if column not in ['dob', 'date_created', 'date_updated']
                else str(getattr(row, column)) for column in columns}
                for row in all_rows
            ]

            return customer_list

        except Exception as ex:
            #  session.rollback()   // Not need IMO, because we are not performing any write operation on db in this function
            raise ex
        finally:
            session.close()
