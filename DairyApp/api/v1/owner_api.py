"""This file defines the Owner APIs"""

from http import HTTPStatus

from flask_restx import Namespace, Resource, fields
from DairyApp.services.owner_services import OwnerHandler

api = Namespace("Owners", description='Owner related operations')

owner_model = api.model('Dairy Owner information', 
{
    'name': fields.String(required=True, description='Owner name'),
    'address': fields.String(required=True, description='Owner address'),
    'mobile': fields.String(required=True, description='Owner valid Mobile number'),
    'dob': fields.Date(required=True, description='Owner date of birth'),
    'email': fields.String(required=True, description='Owner valid email'),
    'password': fields.String(required=True, description='Owner password'),
})


@api.route('/')
class OwnerResource(Resource):
    @api.expect(owner_model, validate=True)
    def post(self):
        """
        Create a new owner.
        """
        try:
            # Return a success response
            owner_handler_instance = OwnerHandler()
            owner_handler_instance.create_owner(api.payload)
            return {'message': 'Owner created successfully 22'}, HTTPStatus.CREATED   # Created
        except Exception as ex:
            # log.error("Caught the exception: ", str(ex))
            return (
                {
                    "message": "Failed to add owner, error - " + str(ex)
                },
                HTTPStatus.INTERNAL_SERVER_ERROR    # 500
            )

    def get(self):
        """
        Get all Owners
        """

        try:
            # Return a success response
            owner_handler_instance = OwnerHandler()
            return owner_handler_instance.get_all_owners()
        except Exception as ex:
            # log.error("Caught the exception: ", str(ex))
            return (
                {
                    "message": "Failed to get owners, error - " + str(ex)
                },
                HTTPStatus.INTERNAL_SERVER_ERROR    # 500
            )

    def delete(self):
        "Delete owner"

    def put(self):
        "Update owner"



        return {"message": "Owner updated successfully"}, HTTPStatus.OK