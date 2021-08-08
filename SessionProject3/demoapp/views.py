from django.shortcuts import render
from demoapp.forms import AddItemForm
# Create your views here.
def additem_view(request):
    formObj=AddItemForm()
    if request.method=='POST':
        name=request.POST['name']#from forms.py name in single quote
        quantity=request.POST['quantity']
        #now save this data into sessions
        request.session[name]=quantity
    return render(request,'demoapp/additem.html',{'fobj':formObj})
def display_item_view(request):
    return render(request,'demoapp/displayitem.html')
