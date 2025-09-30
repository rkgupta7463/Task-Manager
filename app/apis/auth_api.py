from ninja import Router,Schema
from ninja.security import HttpBearer, APIKeyHeader
from app.models import UserProfile
from django.contrib.auth import authenticate

class TokenAuth(HttpBearer):
    def authenticate(self, request, token):
        user = UserProfile.objects.filter(email=token).first()
        if user:
            return user
        return None 
    
auth_api = Router(tags=["Authentication"])

@auth_api.post('login/')
def login(request, email: str, password: str):
    user = authenticate(request, username=email, password=password)
    if user is not None:
        return {"status": True, "message": "Login successful!", "data": {"email": user.email}}
    else:
        return {"status": False, "message": "Invalid credentials", "data": ""}

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

@auth_api.post('register/')
def register(request, payload: RegisterSchema):
    """
    Register a new user.
    """
    data = payload.validate(request.data)
    user = UserProfile.objects.create_user(
        email=data.email,
        password=data.password,
        full_name=data.full_name,
        phone_no=data.phone_no
    )
    return {"status": True, "message": "User registered successfully!", "data": {"email": user.email}}

