from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    x=int(date.strftime('%H')) #strftime function is used to get hours and return in string contenttypes
    msg='hello friend ,Good '
    if x<12:
        #msg=msg+'Morning!!'
        return render(request,'demoapp/morning.html')
    elif x<16:
        #msg=msg+'AfterNoon!!'
        return render(request,'demoapp/afternoon.html')
    elif x<21:
        #msg=msg+'Evening!!'
        return render(request,'demoapp/evening.html')
    else:
        #msg=msg+'night!!'
        return render(request,'demoapp/night.html')

    #return render(request,'demoapp/home.html',{'Message':msg ,'Date':date})
