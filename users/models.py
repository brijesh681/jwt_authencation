from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=55)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
