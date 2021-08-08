from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=50)
    esal=models.FloatField()
    eaddress=models.CharField(max_length=50)

    #NOTE:For CharField ,compulsory we have too specify size
    #TableName=>demoapp_employee
    #fields Name=>eno,ename,esal,eaddress
    #behaviour/datatypes=>eno=IntegerField
