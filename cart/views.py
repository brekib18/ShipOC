from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'cart/index.html')



def create_book(request):
    if request.method == 'POST':
        form = CartCreateForm(data=request.POST)
        if form.is_valid():
            book = form.save
            book_image = CartImage(image=request.POST['image'], book=book)
            book_image.save()
            return redirect('cart-index')
    else:
        form = CartCreateForm()
        # TODO: Instance new BookCreateForm()
    return render(request, 'books/create_book.html', {
        'form': form
    })
