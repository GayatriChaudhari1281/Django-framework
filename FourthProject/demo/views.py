from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#single project with multiple application

def demo_show(request):
    return HttpResponse("<h1>Welcome to Demo Application")

    
