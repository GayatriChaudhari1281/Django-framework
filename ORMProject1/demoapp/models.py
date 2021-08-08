from django.db import models

class CustomManager1(models.Manager):
    def get_empsalrange(self,esal1,esal2):
        return super().get_queryset().filter(esal_range=(esal1,esal2))
    def get_queryset(self):
        return super().get_queryset().order_by('-esal')
# Create your models here.
class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('ename')

class CustomManager3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__lt=200000)

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=50)
    esal=models.FloatField()
    eaddress=models.CharField(max_length=50)
    objects=CustomManager1()#objects is not inbuilt we can change it but wee need to change then when callling any function

class ProxyEmployee(Employee):
    objects=CustomManager2()
    class Meta:
        proxy=True

class ProxyEmployee2(Employee):
    objects=CustomManager3()
    class Meta:
        proxy=True
