
from django.db import models

# Create your models here.
class StudentModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    rows = models.CharField(max_length=100000)
    email = models.EmailField()
    validated = models.BooleanField(default=False)
    