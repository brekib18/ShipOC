from django.shortcuts import render
from django.http import JsonResponse

from .models import *
# Create your views here.

def updateItem(request):
    return JsonResponse('Item was added', safe=False)