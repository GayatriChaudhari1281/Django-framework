from django.db import models

# Create your models here.
class Student(models.Model):
    rollNo=models.IntegerField()
    name=models.CharField(max_length=50)
    marks=models.FloatField()
    address=models.CharField(max_length=50)
