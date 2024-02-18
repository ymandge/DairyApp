import json
from http import HTTPStatus

from DairyApp.models.customer_model import CustomerModel
from DairyApp.libs.customer_lib import CustomerLib

class CustomerHandler:
    "This class is a intermmediator between customer API and low level customer_lib"

    def create_customer(self, payload_data):
        "This method will validate and create new customer"

        # Validation
        new_customer = CustomerModel(
            name=payload_data["name"],
            address=payload_data["address"],
            mobile=payload_data["mobile"],
            dob=payload_data["dob"],
            email=payload_data["email"],
            owner_id=payload_data["owner_id"],
            registered_for_msg=payload_data["registered_for_msg"],
        )

        # Add critical/error/info/debug logging

        # check id customer is already exists if so then return 400 (Bad request); customer already exists
        if 0:
            return {'error_code': HTTPStatus.BAD_REQUEST, 'message': 'Customer already exist.'}
        # Validate the input parameters

        # Create Owner instance and send it to low level lib
        owner = CustomerLib()
        try :
            owner.add_customer(new_customer)
            return {'error_code': HTTPStatus.CREATED,'message': 'Customer added successfully.'}
        except Exception as ex:
            print("MyLog :{}".format(str(ex)))
            #log(str(ex))
            return {'error_code': HTTPStatus.INTERNAL_SERVER_ERROR,'message': 'Failed to add customer.'}


    def get_all_customers_by_owner_id(self, owner_id):
        """
        TODO : Update function string
        """

        # TODO : Add validation for owner_id such as lower and upper limit

        customer_lib = CustomerLib()

        try :
            result = customer_lib.get_all_customers_by_owner_id(int(owner_id))
            message = str('ID : {} not found, Please enter valid ID').format(owner_id) if len(result) == 0 else json.dumps(result)
            return {'error_code': HTTPStatus.OK,'message': message}
        except Exception as ex:
            print("MyLog :{}".format(str(ex)))
            #log(str(ex))
            return {'error_code': HTTPStatus.INTERNAL_SERVER_ERROR,'message': 'Failed to get customer(s).'}
