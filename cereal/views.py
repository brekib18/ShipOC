from django.shortcuts import render
from cereal.models import Cereal
from django.shortcuts import render
from cereal.models import Cereal
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


# Create your views here.


def index(request):
    if 'search_filter' in request.GET:
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


def get_cereal_by_id(request, id):
    return render(request, 'cereal/cereal_details.html',{
        'cereal': get_object_or_404(Cereal, pk=id)
    })

