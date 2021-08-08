from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#Define url pattern at application level instead of project level

def display1_view(request):
    return HttpResponse("<h1>Response from display1_view</h1>")

def display2_view(request):
    return HttpResponse("<h1>Response from display2_view</h1>")

def display3_view(request):
    return HttpResponse("<h1>Response from display3_view</h1>")

def display4_view(request):
    return HttpResponse("<h1>Response from display4_view</h1>")

def display5_view(request):
    return HttpResponse("<h1>Response from display5_view</h1>")
