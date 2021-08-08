from django.shortcuts import render

# Create your views here.
def count_view(request):
    count=request.session.get('count',0)
    newcount=count+1
    request.session['count']=newcount
    print(request.session.get_expiry_age())
    print(request.session.session_key)
    return render(request,'demoapp/count.html',{'count':newcount})


#session key is same for same browser but if we change browser then session_key also changes
# and aslo in same browser if we send request from another tab then also session_key remains same
#and if we shut down the broswer then also session key remains same until the default time
