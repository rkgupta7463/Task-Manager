from ninja.security import HttpBearer
from django.contrib.auth import get_user_model
from jwtunits.custom_jwt import decode_jwt_token

User = get_user_model()

class JWTAuth(HttpBearer):
    def authenticate(self, request, token):
        payload = decode_jwt_token(token)
        if not payload:
            return None
        try:
            user = User.objects.get(id=payload["users"])
            return user
        except User.DoesNotExist:
            return None
