from django.db import models

# Create your models here.
#3.Multilevel Model Inheritance
class GrandParent(models.Model):
    field1=models.CharField(max_length=50)
    field2=models.CharField(max_length=50)

class Parent(GrandParent):
    field3=models.CharField(max_length=50)
    field4=models.CharField(max_length=50)

class Child(Parent):
    field5=models.CharField(max_length=50)
