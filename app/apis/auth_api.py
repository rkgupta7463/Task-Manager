from ninja import Router,Schema
from ninja.security import HttpBearer, APIKeyHeader
from app.models import UserProfile
from django.contrib.auth import authenticate
from jwtunits.custom_jwt import create_jwt_token

class TokenAuth(HttpBearer):
    def authenticate(self, request, token):
        user = UserProfile.objects.filter(email=token).first()
        if user:
            return user
        return None 
    
auth_api = Router(tags=["Authentication"])

@auth_api.post('login/')
def login(request, username: str, password: str):
    user = authenticate(username=username, password=password)
    if not user:
        return {"success": False, "message": "Invalid credentials"}
    
    token = create_jwt_token(user.id)
    return {"success": True, "token": token}


@auth_api.post('logout/')
def logout(request):
    request.auth = None  
    request.user = None 
    return {"status": True, "message": "Logout successful!", "data": ""}

class RegisterSchema(Schema):
    email: str
    password: str
    full_name: str = None
    phone_no: str = None
    pass1:str
    pass2:str 

@auth_api.post("register/")
def register(request, payload: RegisterSchema):
    user = UserProfile.objects.create_user(
        email=payload.email,
        full_name=payload.full_name,
        phone_no=payload.phone_no
    )

    if payload.pass1.check_password(payload.pass2):
        user.set_password(payload.pass1)
        user.save()

    token = create_jwt_token(user.id)
    return {
        "status": True,
        "message": "User registered successfully!",
        "data": token
    }