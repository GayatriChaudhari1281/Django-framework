from django.shortcuts import render
# Create your views here.


def homepage_view(request):
    return render(request,'demoapp/home.html')
def movie_view(request):
    news1="Kishore Kumar is a Great Singer"
    news2="R.D.BURMAN is a Great Music Composer"
    news3="Amitabh Bcchan is a BigB of Bollywood industry"
    news4="Rajesh Khanna is a first Super star of Bollywood"
    news5="Radhe is a third class movie"
    my_dict={'N1':news1,'N2':news2,'N3':news3,'N4':news4,'N5':news5}
    return render(request,'demoapp/movie.html',my_dict)

def sport_view(request):
    news1="Sachin is a master Blaster"
    news2="Gavaskar ia Little Master"
    news3="Kapil dev is a great All Rounder"
    news4="MSD is  graet Cool Captain"
    news5="Anil Kumbale is a highest wicket taker for India"
    my_dict={'N1':news1,'N2':news2,'N3':news3,'N4':news4,'N5':news5}
    return render(request,'demoapp/sports.html',my_dict)

def politics_view(request):
    news1="Narendra Modi is a Prime Minister of India"
    news2="Manohar Parikar was a great Leader"
    news3="Nirmala Sitha raman is a first full time Women Finance Minister of India"
    my_dict={'N1':news1,'N2':news2,'N3':news3}
    return render(request,'demoapp/politics.html',my_dict)
