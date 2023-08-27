"This file is for handling owner APIs and owner_lib interaction"

from DairyApp.models.owner_model import Owner

from DairyApp.libs.dblib.base import Session, Base, engine

class OwnerHandler():
    "This class is a intermmediator between owner API and low level owner_lib"

    def create_owner(self, payload_data):
        "This method will validate and create new owner"

        try:
            # Validation

            # create a new session
            session = Session()

            test_owner = Owner(
                name=payload_data["name"],
                address=payload_data["address"],
                mobile=payload_data["mobile"],
                dob=payload_data["dob"],
                email=payload_data["email"],
                password=payload_data["password"],
            )

            session.add(test_owner)

            session.commit()
            session.close()

            # Add critical/error/info/debug logging

            # check id owner is already exists if so then return 400 (Bad request); Owner already exists

            # Validate the input parameters

            # Create Owner instance and send it to low level lib

        except Exception as ex:
            session.rollback()
            print("Caught the exception: ", str(ex))
            # return

        finally:
            # if open
            session.close()


    def get_all_owners(self):
        ""
         # create a new session
        session = Session()
        query = session.query(Owner)

        # Fetch all rows from the query and convert them to a list of dictionaries
        result_dicts = [row.__dict__ for row in query.all()]

        # Remove the '_sa_instance_state' key from each dictionary
        result_dicts = [{key: value for key, value in row_dict.items() if key != '_sa_instance_state'} for row_dict in result_dicts]

        # skip the hidden columns from end-user i.e. date_created

        print("All data: ".format(result_dicts))

        for row_dict in result_dicts:
            print("row :".format(row_dict))

        session.close()

        all_owmers = []
        return all_owmers