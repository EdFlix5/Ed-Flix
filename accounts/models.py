from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    middle_name = models.CharField(max_length=30, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    profession = models.CharField(max_length=30, blank=True)
    course = models.CharField(max_length=50, blank=True)



class DocViews(models.Model):

    id = models.IntegerField(auto_created=True,primary_key=True)
    username = models.CharField(max_length=40)
    visit_id = models.IntegerField()