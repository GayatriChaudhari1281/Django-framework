from django.shortcuts import render

# Create your views here.
'''def count_view(request):
    icnt=int(request.COOKIES.get('count',0))#count
    newcnt=icnt+1
    response=render(request,'demoapp/count.html',{'nc':newcnt})#nc is different so the count will be 0 always for session
    response.set_cookie('nc',newcnt)
    return response'''

def count_view(request):
    icnt=int(request.COOKIES.get('count',0))#count
    newcnt=icnt+1
    response=render(request,'demoapp/count.html',{'count':newcnt})#nc is different so the count will be 0 always for session
    response.set_cookie('count',newcnt)
    return response
#cookie is browser specific
#for persisent cookies after refresh upto given time cooikes will be stored and the after that time cookies wil set to initial value
