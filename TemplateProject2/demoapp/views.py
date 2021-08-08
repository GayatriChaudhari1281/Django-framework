from django.shortcuts import render
import datetime
# Create your views here.
#how to inject dynamic content from view function to template function
def template_view(request):
    dt=datetime.datetime.now()
    name="Rahul"
    address="Pune"
    mobno=992345676
    my_dict={'date':dt,'nm':name,'ad':address,'mob':mobno}
    #return render(request,'demoapp/home.html',context=my_dict)
    return render(request,'demoapp/home.html',my_dict)
    #return render(request,'demoapp/home.html',{'date':dt})
