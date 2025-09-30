from ninja import Router,Schema,Form
from ninja.security import HttpBearer, APIKeyHeader
from app.models import UserProfile
from django.contrib.auth import authenticate
from jwtunits.custom_jwt import create_jwt_token
from django.db import IntegrityError    

auth_api = Router(tags=["Authentication"])

class LoginSchema(Schema):
    username: str
    password: str

@auth_api.post('login/')
def login(request,payload:LoginSchema):
    print("username:- ",payload.username)
    print("password:- ",payload.password)

    user = authenticate(username=payload.username, password=payload.password)
    print("user:- ",user)
    if not user:
        return {"status": False, "message": "Invalid credentials"}
    
    token = create_jwt_token(user.id)

    return {"status": True, "token": token,"user_detail":user.serializer()}


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
def signup(request, payload: RegisterSchema):
    email = payload.email.strip().lower()

    if UserProfile.objects.filter(email__iexact=email).exists():
        return {"status": False, "message": "This email id already exists!", "data": ""}

    try:
        user = UserProfile.objects.create_user(
            email=email,
            full_name=payload.full_name,
            phone_no=payload.phone_no
        )
        print("user:- ",user)
        if payload.pass1 == payload.pass2:
            user.set_password(payload.pass1)
            user.save()

        token = create_jwt_token(user.id)
        return {"status": True, "message": "User registered successfully!", "access_token": token,"data":user.serializer()}

    except IntegrityError as e:
        print("exption:- ",e)
        return {"status": False, "message": f"{e}", "data": ""}