from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phoneno=models.CharField(max_length=12,blank=True,null=True)
    profileimage=models.ImageField(upload_to='media/profileimg',blank=True)
    dateofbirth=models.DateField(null=True,blank=True)
    email=models.EmailField(unique=True)


