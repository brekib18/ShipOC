from django.shortcuts import render
from clothes.models import Clothes

def index(request):
    context = {'clothes': Clothes.objects.all().order_by('name')}
    return render(request, 'clothes/index.html', context)
