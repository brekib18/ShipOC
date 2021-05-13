from django.shortcuts import render
from clothes.models import Clothes
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse

from clothes.forms.clothes_form import ClothesCreateForm, ClothesUpdateForm
from clothes.models import Clothes, ClothesImage

def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        clothes = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.clothesimage_set.first().image
        } for x in Clothes.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': clothes})
    context = {'clothes': Clothes.objects.all().order_by('name')}
    return render(request, 'clothes/index.html', context)


def get_clothes_by_id(request,id):
    return render(request,'clothes/clothes_details.html',{
        'clothes': get_object_or_404(Clothes, pk=id)
    })




def create_clothes(request):
    if request.method == 'POST':
        form = ClothesCreateForm(data=request.POST)
        if form.is_valid():
            clothes = form.save()
            clothes_image = ClothesImage(image=request.POST['image'], clothes=clothes)
            clothes_image.save()
            return redirect('cereal-index')
    else:
        form = ClothesCreateForm()
        # TODO: Instance new BookCreateForm()
    return render(request, 'clothes/create_clothes.html', {
        'form': form
    })



def delete_clothes(request, id):
    clothes = get_object_or_404(Clothes, pk=id)
    clothes.delete()
    return redirect('clothes-index')


def update_clothes(request, id):
    instance = get_object_or_404(Clothes, pk=id)
    if request.method == 'POST':
        form = ClothesUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('clothes-details', id=id)
    else:
        form = ClothesUpdateForm(instance=instance)
        print(2)
    return render(request, 'clothes/update_clothes.html',{
        'form': form,
        'id': id

    })
