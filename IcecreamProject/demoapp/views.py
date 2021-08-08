from django.shortcuts import render
from demoapp.models import Icecream
from demoapp.forms import IcecreamForm
# Create your views here.
def index_view(request):
    return render(request,'demoapp/index.html')

def add_icecream_view(request):
    formObj=IcecreamForm()#Get
    if request.method=='POST':
        formObj=IcecreamForm(request.POST)#POST
        if formObj.is_valid():
            formObj.save(commit=True)
        return index_view(request)
    return render(request,'demoapp/addicecream.html',{'fobj':formObj})

def list_icecream_view(request):
    icecream_list=Icecream.objects.all()
    return render(request,'demoapp/icecream_list.html',{"icecream_list":icecream_list})
