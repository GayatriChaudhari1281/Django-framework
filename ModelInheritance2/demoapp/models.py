from django.db import models
#MultiTable inheritance
# Create your models here.
class PersonalData(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=50)

class Student(PersonalData):
    rollno=models.IntegerField()
    marks=models.IntegerField()

class Teacher(PersonalData):
    subject=models.CharField(max_length=50)
    salary=models.FloatField()
