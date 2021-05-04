from django.db import models

# Create your models here.

class FileUpload(models.Model):
    
    id = models.IntegerField(auto_created=True,primary_key=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=15)
    DOCUMENT_CHOICES = (
        ('N', 'Notes'),
        ('P', 'PYQ'),
        ('G', 'Gate PYQ'),
    )
    documentType = models.CharField(max_length=1, choices=DOCUMENT_CHOICES)

    file_name = models.CharField(max_length=100)
    file_size = models.CharField(max_length=20)
    file_text = models.TextField(max_length=10000000)
    file_location = models.CharField(max_length=100)
