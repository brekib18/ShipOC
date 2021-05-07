from django.shortcuts import render
from cereal.models import Cereal
# Create your views here.




def index(request):
    context = {'cereals': Cereal.objects.all().order_by('name')}
    return render(request, 'cereal/index.html', context)