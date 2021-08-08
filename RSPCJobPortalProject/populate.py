import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','RSPCJobPortalProject.settings')
import django
django.setup()

from demoapp.models import *
from faker import Faker
from random import *
obj=Faker()

def mobno_gen():
    x=randint(7,9)
    num=str(x)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(no):
    for i in range(no):
        fdate=obj.date()
        fcompany=obj.company()
        ftitle=obj.random_element(elements=('ProjectManager','Team Lead','Software Engineer'))
        feligiblity=obj.random_element(elements=('M.Tech','B.Tech','MCA','BCA'))
        femail=obj.email()
        fmobno=mobno_gen()
        faddress=obj.address()

        #punejobs_record=PuneJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligiblity,address=faddress,email=femail,mobno=fmobno)
        #banglorejobs_record=BangloreJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligiblity,address=faddress,email=femail,mobno=fmobno)
        #chennaijobs_record=ChennaiJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligiblity,address=faddress,email=femail,mobno=fmobno)
        #hydrabadjobs_record=HydrabadJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligiblity,address=faddress,email=femail,mobno=fmobno)




populate(30)
