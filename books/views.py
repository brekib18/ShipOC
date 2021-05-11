from django.shortcuts import render
from django.shortcuts import render
from books.models import Books
from django.shortcuts import get_object_or_404

def index(request):
    context = {'books': Books.objects.all().order_by("name")}
    return render(request, 'books/index.html',context)

<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
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
    return render(request, 'book/create_book.html', {
        'form': form
    })
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
