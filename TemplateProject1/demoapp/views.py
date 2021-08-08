from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def template_view(request):
    return render(request,'demoapp/home.html')
