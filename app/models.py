from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser


## custom user profile manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    

### custom user profile 
class UserProfile(AbstractUser):
    full_name=models.CharField(max_length=150,null=True,blank=True)
    email=models.EmailField(unique=True)
    phone_no = models.CharField(max_length=14, blank=True, null=True)

    objects=CustomUserManager()

    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - create at:- {self.created_at}"
    

### task model    
class Task(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField()
    completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __Str__(self):
        return f"{self.title} - created at: {self.created_at} - completed: {self.completed}"