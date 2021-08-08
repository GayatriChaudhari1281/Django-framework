from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def python_view(request):
    return HttpResponse("<h1>Welcome to python world!!")

def django_view(request):
    return HttpResponse("<h1>Welcome to Django world!!")

def rest_API_view(request):
    return HttpResponse("<h1>Welcome to RestAPI world!!")
