from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from demoapp.forms import SignupForm
from django.http import HttpResponseRedirect

# Create your views here.
def homepage_view(request):
    return render(request,'demoapp/home.html')

@login_required #annotation in java in python decorators
def javaexams_view(request):
    return render(request,'demoapp/javaexams.html')

@login_required
def pythonexams_view(request):
    return render(request,'demoapp/pythonexams.html')

@login_required
def aptitudeexams_view(request):
    return render(request,'demoapp/aptitudeexams.html')

def logout_view(request):
    return render(request,'demoapp/logout.html')

def signup_view(request):
    form=SignupForm()#object created
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'demoapp/signup.html',{'form':form})
