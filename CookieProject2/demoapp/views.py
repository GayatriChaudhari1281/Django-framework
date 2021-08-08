from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request,'demoapp/name.html')
#application change session id change
#brower close session id change
def age_view(request):
    #read data coming from name.html page
    name=request.GET['name']
    #display age.html form to user
    response=render(request,'demoapp/age.html')
    #save that name for future reference inside Cookie
    response.set_cookie('name',name)
    return response

def city_view(request):
    #read data coming from name.html page
    age=request.GET['age']
    #display age.html form to user
    response=render(request,'demoapp/city.html')
    #save that name for future reference inside Cookie
    response.set_cookie('age',age)
    return response

def home_view(request):
    city=request.GET['city']
    name=request.COOKIES.get('name')
    age=request.COOKIES.get('age')
    response=render(request,'demoapp/home.html',{'name':name,'age':age,'city':city})
    return response
