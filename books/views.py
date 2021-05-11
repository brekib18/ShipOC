from django.shortcuts import render
from django.shortcuts import render
from books.models import Books
from django.shortcuts import get_object_or_404

def index(request):
    context = {'books': Books.objects.all().order_by("name")}
    return render(request, 'books/index.html',context)

def get_book_by_id(request,id):
    return render(request,'books/books_details.html',{
        'book': get_object_or_404(Books, pk=id)
    })