from django.shortcuts import render
from accessories.models import Accessories

# Create your views here.

def index(request):
    context = {'accessories': Accessories.objects.all().order_by("name")}
    return render(request, 'accessories/index.html',context)
