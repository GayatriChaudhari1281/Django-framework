from django.shortcuts import render
from demoapp.models import *
# Create your views here.
def index_view(request):
    return render(request,'demoapp/index.html')

def punejobs_view(request):
    pjobs=PuneJobs.objects.all()
    return render(request,'demoapp/punejob.html',{'pjobs':pjobs})

def chennaijobs_view(request):
    cjobs=ChennaiJobs.objects.all()
    return render(request,'demoapp/chennaijob.html',{'cjobs':cjobs})

def banglorejobs_view(request):
    bjobs=BangloreJobs.objects.all()
    return render(request,'demoapp/banglorejob.html',{'bjobs':bjobs})

def hydrabadjobs_view(request):
    hjobs=HydrabadJobs.objects.all()
    return render(request,'demoapp/hydrabadjob.html',{'hjobs':hjobs})
