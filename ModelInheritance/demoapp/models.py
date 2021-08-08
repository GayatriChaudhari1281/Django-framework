from django.db import models

# Create your models here.
class PersonalData(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=50)
    class Meta:
        abstract=True
        #if these 2 lines removed then it is multitable inheritance

class Student(PersonalData):
    rollno=models.IntegerField()
    marks=models.IntegerField()

class Teacher(PersonalData):
    subject=models.CharField(max_length=50)
    salary=models.FloatField()
