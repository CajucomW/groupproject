from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#TODO: Doe we need to fix this from 'def' to 
#class create_user(models.Model):?
def create_user(data):
    user =  User.objects.create_user(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        first_name=data['first_name'],
        last_name=data['last_name']
        )
    user.is_admin=False
    user.is_staff=False
    user.save()