from django.db import models

# Create your models here.
class Book(models.Model):
    PNR_NO=models.IntegerField()
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
