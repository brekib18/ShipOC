from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from cart.models import Cart
from django.contrib.auth.decorators import login_required

from cereal.forms.cereal_form import CerealCreateForm, CerealUpdateForm
from cereal.models import Cereal, CerealImage


# Create your views here.


def index(request):
    if 'search_filter' in request.GET:
        print('hallohallo')
        search_filter = request.GET['search_filter']
        cereals = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.cerealimage_set.first().image
        } for x in Cereal.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': cereals})
    context = {'cereals': Cereal.objects.all().order_by('name')}
    return render(request, 'cereal/index.html', context)


def filter_index(request):
    if 'filter' in request.GET:
        filter_by_cat = request.GET['filter']
        cereals = [{
            'id': x.id,
            'cat_id': x.cereal_category_id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.cerealimage_set.first().image
        } for x in Cereal.objects.filter(cereal_category_id=filter_by_cat)]
        return JsonResponse({'data': cereals})
    context = {'cereals': Cereal.objects.all().order_by('cereal_category_id')}
    return render(request, 'cereal/filter_index.html', context)



def get_cereal_by_id(request, id):
    return render(request, 'cereal/cereal_details.html',{
        'cereal': get_object_or_404(Cereal, pk=id)
    })



@login_required
def create_cereal(request):
    if not request.user.is_superuser:
        return redirect('cereal-index')
    if request.method == 'POST':
        form = CerealCreateForm(data=request.POST)
        if form.is_valid():
            cereal = form.save()
            cereal_image = CerealImage(image=request.POST['image'], cereal=cereal)
            cereal_image.save()
            return redirect('cereal-index')
    else:
        form = CerealCreateForm()
        # TODO: Instance new BookCreateForm()
    return render(request, 'cereal/create_cereal.html', {
        'form': form
    })




@login_required
def delete_cereal(request, id):
    cereal = get_object_or_404(Cereal, pk=id)
    if not request.user.is_superuser:
        return redirect('cereal-index')
    cereal.delete()
    return redirect('cereal-index')



@login_required
def update_cereal(request, id):
    instance = get_object_or_404(Cereal, pk=id)
    if not request.user.is_superuser:
        return redirect('cereal-index')
    if request.method == 'POST':
        form = CerealUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('cereal-details', id=id)
    else:
        form = CerealUpdateForm(instance=instance)
        print(2)
    return render(request, 'cereal/update_cereal.html',{
        'form': form,
        'id': id

    })


# def add_to_cart(request):
#     if request.method == "GET":
#         cart_item = [{
#             'id': x.id,
#             'name': x.name,
#             'description': x.description,
#             'firstImage': x.cerealimage_set.first().image
#         } for x in Cart.objects.all()]
#         return JsonResponse({'data': cart_item})
#     context = {'cart_item': Cart.objects.all().order_by('name')}
#     return render(request, 'cereal/index.html', context)

        # context = {'cereals': Cereal.objects.filter(name__icontains=search_filter)}
        # return render(request, 'cereal/index.html', context)
        # return render(request, 'cereal/index.html')


