"This file is for handling owner APIs and owner_lib interaction"
from http import HTTPStatus

from DairyApp.models.owner_model import OwnerModel
from DairyApp.libs.owner_lib import OwnerLib
import json

class OwnerHandler:
    "This class is a intermmediator between owner API and low level owner_lib"

    def create_owner(self, payload_data):
        "This method will validate and create new owner"

        # Validation
        test_owner = OwnerModel(
            name=payload_data["name"],
            address=payload_data["address"],
            mobile=payload_data["mobile"],
            dob=payload_data["dob"],
            email=payload_data["email"],
            password=payload_data["password"],
        )

        
        # Add critical/error/info/debug logging

        # check id owner is already exists if so then return 400 (Bad request); Owner already exists
        if 0:
            return {'error_code': HTTPStatus.BAD_REQUEST, 'message': 'Owner already exist.'}
        # Validate the input parameters

        # Create Owner instance and send it to low level lib
        owner = OwnerLib()
        try :
            owner.add_owner(test_owner)
            return {'error_code': HTTPStatus.CREATED,'message': 'Owner added successfully.'}
        except Exception as ex:
            print("MyLog :{}".format(str(ex)))
            #log(str(ex)) 
            return {'error_code': HTTPStatus.INTERNAL_SERVER_ERROR,'message': 'Failed to add owner.'}

    def get_all_owners(self):
        """temp"""
        owner = OwnerLib()
        print("Getting all owners")
        owner_list = owner.get_all_owner()
        print(owner_list)
        return json.dumps(owner_list)
    
    def get_owner_using_id(self,uid):

        owner = OwnerLib()
        print("OwnerService User id = " + str(uid))
        owner = owner.get_owner_using_id(int(uid))
        print("After")
        return json.dumps(owner)
    
    # def get_owner_using_name(self,uname):

    #     owner = OwnerLib()
    #     print("OwnerService User name = " + str(uname))
    #     owner = owner.get_owner_using_name(uname)
    #     print("After")
    #     return json.dumps(owner)

