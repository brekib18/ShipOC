from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from accessories.forms.accessories_form import AccessoriesCreateForm, AccessoriesUpdateForm
from accessories.models import Accessories, AccessoriesImage
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        accessories = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'firstImage': x.accessoriesimage_set.first().image
        } for x in Accessories.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': accessories})
    context = {'accessories': Accessories.objects.all().order_by('name')}
    return render(request, 'accessories/index.html', context)


def get_accessories_by_id(request,id):
    return render(request,'accessories/accessories_details.html',{
        'accessories': get_object_or_404(Accessories, pk=id)
    })


@login_required
def create_accessories(request):
    if not request.user.is_superuser:
        return redirect('accessories-index')
    if request.method == 'POST':
        form = AccessoriesCreateForm(data=request.POST)
        if form.is_valid():
            accessories = form.save()
            accessories_image = AccessoriesImage(image=request.POST['image'], accessories=accessories)
            accessories_image.save()
            return redirect('accessories-index')
    else:
        form = AccessoriesCreateForm()
        # TODO: Instance new BookCreateForm()
    return render(request, 'accessories/create_accessories.html', {
        'form': form
    })


@login_required
def delete_accessories(request, id):
    accessories = get_object_or_404(Accessories, pk=id)
    if not request.user.is_superuser:
        return redirect('accessories-index')
    accessories.delete()
    return redirect('accessories-index')


@login_required
def update_accessories(request, id):
    instance = get_object_or_404(Accessories, pk=id)
    if not request.user.is_superuser:
        return redirect('accessories-index')
    if request.method == 'POST':
        form = AccessoriesUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('accessories-details', id=id)
    else:
        form = AccessoriesUpdateForm(instance=instance)
        print(2)
    return render(request, 'accessories/update_accessories.html',{
        'form': form,
        'id': id

    })