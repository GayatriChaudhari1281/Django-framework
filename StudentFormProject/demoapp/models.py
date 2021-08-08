from django.db import models

# Create your models here.
class Student(models.Model):
    rollNo=models.IntegerField()
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    email=models.EmailField()
    feedback=models.CharField(max_length=300)
#username=gayatri
#password=Gaya@128
