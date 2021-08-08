from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse

# Create your views here.
#class should be chld of views class
class WelcomeView(View):
    def get(self,request):
        return HttpResponse("<h1>Welcome to Class Base View</h1>")
class WelcomeTemplateView(TemplateView):
    template_name='demoapp/welcome.html'
    def get_context_data(self,**kwargs):#django is responsible to call this function
        context=super().get_context_data(**kwargs)#calling hte parent method using super
        context['name']='Gayatri'#context is dictionary
        context['Subject']='Python Django'
        context['Marks']='465'
        return context#sending to template 
# now we want to send context parameter
