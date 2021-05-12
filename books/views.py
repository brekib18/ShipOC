from django.shortcuts import render
from django.shortcuts import render

from books.forms.book_form import BookCreateForm
from books.models import Books
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        books = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.booksimage_set.first().image
        } for x in Books.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': books})
    context = {'books': Books.objects.all().order_by('name')}
    return render(request, 'books/index.html', context)


def get_book_by_id(request,id):
    return render(request,'books/books_details.html',{
        'book': get_object_or_404(Books, pk=id)
    })


def create_book(request):
    if request.method == 'POST':
        print(1)
    else:
        form = BookCreateForm()
        # TODO: Instance new BookCreateForm()
    return render(request, 'books/create_book.html', {
        'form': form
    })

