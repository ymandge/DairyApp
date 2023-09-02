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
    'oid': fields.String(required=True, description='Owner id'),
})


@api.route('/')
class CustomerResource(Resource):

    @api.expect(customer_model, validate=True)
    def post(self):
        """
        Create a new customer.
        """


    def get(self):
        """
        customer all Owners
        """

    def delete(self):
        "Delete customer"

    def put(self):
        "Update customer"
