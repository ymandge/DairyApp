"""This file defines the Customer APIs"""

from http import HTTPStatus

from flask_restx import Namespace, Resource, fields
from DairyApp.services.customer_service import CustomerHandler

api = Namespace("Customer", description='Customer related operations')

customer_model = api.model('Customer information', 
{
    'name': fields.String(required=True, description='Customer name'),
    'address': fields.String(required=True, description='Customer address'),
    'mobile': fields.String(required=True, description='Customer valid Mobile number'),
    'dob': fields.Date(required=True, description='Customer date of birth'),
    'email': fields.String(required=True, description='Customer valid email'),
    'owner_id': fields.String(required=True, description='Owner id'),
    'registered_for_msg': fields.Boolean(required=False, description="Whether register to SMS service or not"),
    # "profile_photo": fields.String(required=False, description="Profile Picture"),
})


@api.route('/')
class CustomerResource(Resource):

    @api.expect(customer_model, validate=True)
    def post(self):
        """
        Create a new customer.
        """

        try:
            # Return a success response
            customer_handler_instance = CustomerHandler()
            result = customer_handler_instance.create_customer(api.payload)
            return {
                'message': result['message']
            }, result['error_code']   # Created

        except Exception as ex:
            print("my log: {}".format(str(ex)))
            # log.error("Caught the exception while adding owner: ", str(ex))
            return (
                {
                    "message": "Failed to add customer"
                },
                HTTPStatus.INTERNAL_SERVER_ERROR    # 500
            )


    def get(self):
        """
        Get all customers
        """

    def delete(self):
        "Delete customer"

    def put(self):
        "Update customer"


@api.route('/<int:owner_id>')
class GetSpecificOwnerCustomers(Resource):
    def get(self, owner_id):
        "Get specific owner customers"

        try:
            # Return a success response
            print("GetSpecificOwner User id = " + str(owner_id))
            customer_handler_instance = CustomerHandler()
            result = customer_handler_instance.get_all_customers_by_owner_id(owner_id)
            return {
                    'message': result['message']
                }, result['error_code']   # Created
        except Exception as ex:
            print("MyLog: {}".format(str(ex)))
            # log.error("Caught the exception: ", str(ex))
            return (
                {
                    "message": "Failed to get customer(s)\nPlease check logs for additional details."
                },
                HTTPStatus.INTERNAL_SERVER_ERROR    # 500
            )