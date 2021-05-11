from django.shortcuts import render
from accessories.models import Accessories
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

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