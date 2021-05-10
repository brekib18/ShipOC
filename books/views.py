from django.shortcuts import render
from books.models import Books
# Create your views here.

def index(request):
    context = {'books': Books.objects.all().order_by("name")}
    return render(request, 'books/index.html',context)

