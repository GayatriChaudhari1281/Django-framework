from django.shortcuts import render
from . import forms

# (.) current working directory
# Create your views here.
def empForm_view(request):
    formObj=forms.EmployeeForm()
    return render(request,'demoapp/register.html',{'fobj':formObj})
