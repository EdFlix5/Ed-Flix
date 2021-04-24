from django.db import models

# Create your models here.

class FileUpload(models.Model):
    
    id = models.IntegerField(auto_created=True,primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
