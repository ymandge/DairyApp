from DairyApp.models.customer_model import CustomerModel
from DairyApp.libs.customer_lib import CustomerLib


class CustomerHandler:
    "This class is a intermmediator between owner API and low level owner_lib"

    def create_owner(self, payload_data):
        "This method will validate and create new owner"

        #try:
            # Validation

            # test_customer = CustomerModel(
            #     name=payload_data["name"],
            #     address=payload_data["address"],
            #     mobile=payload_data["mobile"],
            #     dob=payload_data["dob"],
            #     email=payload_data["email"],
            #     password=payload_data["oid"],
            # )

            # cust = CustomerLib()
            # cust.add_customer(test_customer)

        #except Exception as ex:
        #    print("execption")
        