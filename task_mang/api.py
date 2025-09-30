from ninja import NinjaAPI
from app.apis.api import api  

app = NinjaAPI()

app.add_router('v1/', api)
