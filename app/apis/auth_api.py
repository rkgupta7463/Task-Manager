from ninja import Router,Schema,Form
from ninja.security import HttpBearer, APIKeyHeader
from app.models import UserProfile
from django.contrib.auth import authenticate
from jwtunits.custom_jwt import create_jwt_token
from django.db import IntegrityError    

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
    full_name: str = None
    phone_no: str = None
    pass1:str
    pass2:str 

@auth_api.post("signup/")
def signup(request, payload: Form[RegisterSchema]):
    email = payload.email.strip().lower()

    if UserProfile.objects.filter(email__iexact=email).exists():
        return {"status": False, "message": "This email id already exists!", "data": ""}

    try:
        user = UserProfile.objects.create_user(
            email=email,
            full_name=payload.full_name,
            phone_no=payload.phone_no
        )

        if payload.pass1 == payload.pass2:
            user.set_password(payload.pass1)
            user.save()

        token = create_jwt_token(user.id)
        return {"status": True, "message": "User registered successfully!", "data": token}

    except IntegrityError as e:
        print("exption:- ",e)
        return {"status": False, "message": f"{e}", "data": ""}