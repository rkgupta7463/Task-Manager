from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100, blank=True)
    phone_no  = models.CharField(max_length=15, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['full_name','phone_no']

    def __str__(self):
        return self.email
    

    def serializer(self):
        dic={}
        dic['id']=self.id
        dic['full_name']=self.full_name
        dic['email']=self.email
        dic['phone_number']=self.phone_no
        dic['is_active']=self.is_active
        dic['is_staff']=self.is_staff
        dic['created_at']=self.created_at
        dic['updated_at']=self.updated_at

        return dic
    
    def short_serializer(self):
        dic={}
        dic['id']=self.id
        dic['full_name']=self.full_name
        dic['email']=self.email
        dic['phone_number']=self.phone_no

        return dic


### task model    
class Task(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField()
    completed=models.BooleanField(default=False)
    
    created_by=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name="creator")
    updated_by=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name="updated_by")
    
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __Str__(self):
        return f"{self.title} - created at: {self.created_at} - completed: {self.completed}"
    
    def serializer(self):
        dic={}
        dic['id']=self.id
        dic['title']=self.title
        dic['description']=self.description
        dic['completed']=self.completed
        dic['created_by']=self.created_by.short_serializer()
        dic['created_at']=self.created_at
        dic['updated_at']=self.updated_at

        return dic