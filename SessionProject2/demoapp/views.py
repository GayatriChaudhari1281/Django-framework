from django.shortcuts import render
from . import forms
# Create your views here.
def name_view(request):
    nameObj=forms.NameForm()
    return render(request,'demoapp/name.html',{'nobj':nameObj})

def age_view(request):
    #read data coming from name.html
    name=request.GET['name'] #'name shoulf be same as form name field'
    #save this data in session & display age.html page
    request.session['name']=name
    ageObj=forms.AgeForm()
    return render(request,'demoapp/age.html',{'aobj':ageObj})

def city_view(request):
    #read data coming from name.html
    age=request.GET['age'] #'name shoulf be same as form name field'
    #save this data in session & display age.html page
    request.session['age']=age
    cityObj=forms.CityForm()
    return render(request,'demoapp/city.html',{'cobj':cityObj})

def home_view(request):
    city=request.GET['city']
    request.session['city']=city
    return render(request,'demoapp/home.html')
