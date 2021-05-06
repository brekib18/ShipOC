from django.shortcuts import render
# Create your views here.

cereals = [
    {'name': 'cocoa puffs', 'price': 4.99},
    {'name': 'musli', 'price': 8.99}
]

def index(request):
    return render(request, 'cereal/index.html', context = {'cereals': cereals})