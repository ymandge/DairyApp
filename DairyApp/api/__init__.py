from flask import Blueprint
from flask_restx import Api

# Flask project imports
from DairyApp.api.v1.owner_api import api as api_owner
from DairyApp.api.v1.customer_api import api as api_customer

# http://10.205.253.25:8000/dairyapp/rest/v1/owner/
# http://10.205.253.25:8000/dairyapp/rest/v1/customer/
# http://10.205.253.25:8000/dairyapp/rest/v1/delivery/

api_v1 = Blueprint("api_v1", __name__, url_prefix="/dairyapp")

api = Api(api_v1, version="1.0", title="DairyApp APIs", description="DairyApp API console")

api.add_namespace(api_owner)
api.add_namespace(api_customer)
