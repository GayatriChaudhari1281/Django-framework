import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ModelProject2.settings')
import django
django.setup()

from demoapp.models import *
from faker import Faker
from random import *
obj=Faker()


def populate(no):
    for i in range(no):
        froll=obj.random_int(min=0,max=100)
        fname=obj.name()
        faddress=obj.address()
        fmarks=obj.random_int(min=30,max=500)
        stud_record=Student.objects.get_or_create(rollNo=froll,name=fname,address=faddress,marks=fmarks)

populate(30)
