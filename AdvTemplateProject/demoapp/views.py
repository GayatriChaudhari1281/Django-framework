from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'demoapp/home.html')

def movie_view(request):
    return render(request,'demoapp/movie.html')

def sport_view(request):
    return render(request,'demoapp/sport.html')

def politics_view(request):
    return render(request,'demoapp/politics.html')
