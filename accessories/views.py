from django.shortcuts import render
from accessories.models import Accessories
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    context = {'accessories': Accessories.objects.all().order_by("name")}
    return render(request, 'accessories/index.html',context)

def get_accessories_by_id(request,id):
    return render(request,'accessories/accessories_details.html',{
        'accessories': get_object_or_404(Accessories, pk=id)
    })