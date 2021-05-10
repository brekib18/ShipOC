from django.shortcuts import render
from cereal.models import Cereal
from django.shortcuts import render
from cereal.models import Cereal
from django.shortcuts import get_object_or_404


# Create your views here.





def index(request):
    context = {'cereals': Cereal.objects.all().order_by('name')}
    return render(request, 'cereal/index.html', context)

def get_cereal_by_id(request,id):
    return render(request,'cereal/cereal_details.html',{
        'cereal': get_object_or_404(Cereal, pk=id)
    })