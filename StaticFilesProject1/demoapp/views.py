from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    x=int(date.strftime('%H')) #strftime function is used to get hours and return in string contenttypes
    msg='hello friend ,Good '
    if x<12:
        msg=msg+'Morning!!'
    elif x<16:
        msg=msg+'AfterNoon!!'
    elif x<21:
        msg=msg+'Evening!!'
    else:
        msg=msg+'night!!'

    return render(request,'demoapp/home.html',{'Message':msg ,'Date':date})
