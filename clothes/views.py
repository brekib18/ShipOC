from django.shortcuts import render
from clothes.models import Clothes
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

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
