from django.shortcuts import render
from clothes.models import Clothes
from django.shortcuts import get_object_or_404

def index(request):
    context = {'clothes': Clothes.objects.all().order_by('name')}
    return render(request, 'clothes/index.html', context)

def get_clothes_by_id(request,id):
    return render(request,'clothes/clothes_details.html',{
        'clothes': get_object_or_404(Clothes, pk=id)
    })
