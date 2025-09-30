from ninja import NinjaAPI
from app.apis.api import api 
from app.apis.auth_api import auth_api 

app = NinjaAPI()

app.add_router('v1/', api)
app.add_router('v1',auth_api)
