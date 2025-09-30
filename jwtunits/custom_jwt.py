import jwt
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_mang.settings')
django.setup()

from django.conf import settings
from datetime import datetime, timedelta
from app.models import UserProfile

def create_jwt_token(user_id):
    
    payload = {
        "users": user_id,
        "exp": datetime.utcnow() + timedelta(seconds=settings.JWT_EXP_DELTA_SECONDS),
        "iat": datetime.utcnow(),
    }

    token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)
    return token

def decode_jwt_token(token):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
