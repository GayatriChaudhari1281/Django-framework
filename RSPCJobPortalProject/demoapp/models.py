from django.db import models

# Create your models here.
class PuneJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    mobno=models.IntegerField()

class BangloreJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    mobno=models.IntegerField()

class ChennaiJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    mobno=models.IntegerField()

class HydrabadJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    eligibility=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    mobno=models.IntegerField()
