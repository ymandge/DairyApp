"This file is for handling owner APIs and owner_lib interaction"

from DairyApp.models.owner_model import OwnerModel
from DairyApp.libs.owner_lib import OwnerLib

class OwnerHandler:
    "This class is a intermmediator between owner API and low level owner_lib"

    def create_owner(self, payload_data):
        "This method will validate and create new owner"

        try:
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

            # Validate the input parameters

            # Create Owner instance and send it to low level lib
            owner = OwnerLib()
            owner.add_owner(test_owner)

        except Exception as ex:
            print("Caught the exception: ", str(ex))
            # return

    def get_all_owners(self):
        """temp"""
