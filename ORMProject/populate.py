import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ORMProject.settings')
import django
django.setup()

from demoapp.models import *
from faker import Faker
from random import *
obj=Faker()


def populate(no):
    for i in range(no):
        fno=obj.random_int(min=101,max=400)
        fname=obj.name()
        faddress=obj.address()
        fsal=obj.random_int(min=100000,max=400000)
        emp_record=Employee.objects.get_or_create(eno=fno,ename=fname,eaddress=faddress,esal=fsal)

populate(100)
