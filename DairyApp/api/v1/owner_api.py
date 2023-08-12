"""This file defines the Owner APIs"""

from flask_restx import Namespace, Resource, fields

api = Namespace("Owners", description='Owner related operations')

owner_model = api.model('Owner', {
    'ownername': fields.String(required=True, description='Owner name'),
    'email': fields.String(required=True, description='Email'),
    'address': fields.String(required=True, description='Address')
})

@api.route('/')
class OwnerResource(Resource):
    @api.expect(owner_model, validate=True)
    def post(self):
        """
        Create a new owner.
        """

        print("create owner payload: {}".format(api.payload))

        data = api.payload
        username = data.get('ownername')
        email = data.get('email')
        address = data.get('address')

        # Perform validation and error handling as needed

        # Create a new user
        #user = User(username=username, email=email, address=address)
        #UserService.create_user(user)

        # Return a success response
        return {'message': 'Owner created successfully'}, 201

    def get(self):
        """
        Get Owners
        """

        print("get owners called")

        return {"message": "Success"}, 200

    def delete(self):
        "Delete owner"