from django.shortcuts import render
from demoapp.models import Book
# Create your views here.
def Book_info_view(request):
    book=Book.objects.all()
    return render(request,'demoapp/book.html',{'book':book})
