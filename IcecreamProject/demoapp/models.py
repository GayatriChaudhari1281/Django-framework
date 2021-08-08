from django.db import models

# Create your models here.
class Icecream(models.Model):
    flavour=models.CharField(max_length=15)
    ingrediants=models.CharField(max_length=20)
    company=models.CharField(max_length=10)
    price=models.IntegerField()
    expdate=models.DateField()
