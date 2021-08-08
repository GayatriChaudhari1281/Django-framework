from django.shortcuts import render
from demoapp.models import Book
from django.views.generic import DeleteView,UpdateView,ListView,DetailView,CreateView
from django.urls import reverse_lazy
from django.urls import reverse_lazy
# Create your views here.
"""def display_view(request):
    bookObj=Book.objects.all()
    return render(request,'demoapp/book.html',{'b':bookObj})"""

#to create class we need to extend its parent class
#listview by default internally calls default templates whose name is relaated to models class
#and then the book_list.html will be
#default context object=>book_list
class BookListView(ListView):
    model=Book
    #we can customize template file as
    #template_name='demoapp/books.html'
    #we can customize default context object file as
    #context_object_name='books'


class BookDetailView(DetailView):
    model=Book

class BookCreateView(CreateView):
    model=Book
    fields=('title','author','pages','price')

class BookUpdateView(UpdateView):
    model=Book
    fields=('title','author','pages','price')

class BookDeleteView(DeleteView):
    model=Book
    success_url=reverse_lazy('books')#is notname of object can take any name
