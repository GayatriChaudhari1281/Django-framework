
from django.db import models

# Create your models here.
class Student(models.Model):
    rollNo=models.IntegerField()
    name=models.CharField(max_length=50)
    marks=models.FloatField()
    address=models.TextField()
    dob=models.DateField()
    email=models.EmailField()#length=254
    mobno=models.IntegerField()
