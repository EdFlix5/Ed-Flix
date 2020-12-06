from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    middle_name = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=15, blank=True)
    profession = models.CharField(max_length=30, blank=True)
    course = models.CharField(max_length=50, blank=True)
