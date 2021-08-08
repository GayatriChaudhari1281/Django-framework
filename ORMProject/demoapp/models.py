from django.db import models

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('ename')
# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=50)
    esal=models.FloatField()
    eaddress=models.CharField(max_length=50)
    objects=CustomManager()#objects is not inbuilt we can change it but wee need to change then when callling any function
