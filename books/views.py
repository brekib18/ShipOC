from django.shortcuts import render
from django.shortcuts import render

from books.forms.book_form import BookCreateForm
from books.forms.book_form import BookUpdateForm
from books.models import Books, BooksImage
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



def index(request):
    if 'sort_button' in request.GET:

        sort_button = request.GET['sort_button']

        if sort_button == 'alphabetical':
            print('alpha')
            result = Books.objects.all()
            books = []
            result = result.order_by('name')
            for elem in result:

                books.append({
                    'id': elem.id,
                    'name': elem.name,
                    'description': elem.description,
                    'firstImage': elem.booksimage_set.first().image,
                    'price': elem.price
                    })
        elif sort_button == 'price_low':
            result = Books.objects.all()
            books = []
            result = result.order_by('price')
            for elem in result:

                books.append({
                    'id': elem.id,
                    'name': elem.name,
                    'description': elem.description,
                    'firstImage': elem.booksimage_set.first().image,
                    'price': elem.price
                    })
        elif sort_button == 'price_high':
            result = Books.objects.all()
            books = []
            result = result.order_by('-price')
            for elem in result:

                books.append({
                    'id': elem.id,
                    'name': elem.name,
                    'description': elem.description,
                    'firstImage': elem.booksimage_set.first().image,
                    'price': elem.price
                    })
        return JsonResponse({'data': books})
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        books = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.booksimage_set.first().image,
            'price': x.price
        } for x in Books.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': books})
    context = {'books': Books.objects.all().order_by('name')}
    return render(request, 'books/index.html', context)


def get_book_by_id(request, id):
    return render(request, 'books/books_details.html', {
        'book': get_object_or_404(Books, pk=id)
    })



@login_required
def create_book(request):
    if not request.user.is_superuser:
        return redirect('books-index')
    if request.method == 'POST':
        form = BookCreateForm(data=request.POST)
        if form.is_valid():
            book = form.save()
            book_image = BooksImage(image=request.POST['image'], book=book)
            book_image.save()
            return redirect('books-index')
    else:
        form = BookCreateForm()
        # TODO: Instance new BookCreateForm()
    return render(request, 'books/create_book.html', {
        'form': form
    })



@login_required
def delete_book(request, id):
    book = get_object_or_404(Books, pk=id)
    if not request.user.is_superuser:
        return redirect('books-index')
    book.delete()
    return redirect('books-index')



@login_required
def update_book(request, id):
    instance = get_object_or_404(Books, pk=id)
    if not request.user.is_superuser:
        return redirect('books-index')
    if request.method == 'POST':
        form = BookUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('books-details', id=id)
    else:
        form = BookUpdateForm(instance=instance)
        print(2)
    return render(request, 'books/update_book.html',{
        'form': form,
        'id': id

    })


