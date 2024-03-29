
from django.shortcuts import render, get_object_or_404, redirect
from cereal.models import Cereal

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Cart

@login_required()
def my_cart(request):
    if request.user.is_superuser:
        return render(request, '404.html')
    if request.method == 'GET':
        prod = []
        for x in Cart.objects.filter(user_id = request.user.id):
            prod.append(x)
        print(prod)
        prod_ids = [p.cereal_id for p in prod]
        context = {'items': prod, 'totalprice': _total_price(prod_ids, request.user.id)}
        return render(request,'shopcart/index.html', context)

@login_required()
def add_to_cart(request, id):
    if request.user.is_superuser:
        return render(request, '404.html')
    prod = []
    for x in Cart.objects.filter(user_id=request.user.id):
        prod.append(str(x))
    prod_int = [int(i) for i in prod]
    if id in prod_int and id == Cart.objects.get(user_id = request.user.id, cereal_id=id).cereal_id:
        cartitem = Cart.objects.get(user_id = request.user.id, cereal_id = id)
        cartitem.quantity += 1
    else:
        cartitem = Cart(user_id=request.user.id, cereal_id=id, quantity=1)
    cartitem.save()
    print()
    return redirect('/cereals/' + str(id))


def _total_price(prodid_list, u_id):
    totalPrice = 0
    for i in prodid_list:
        totalPrice += Cereal.objects.get(id=i).price * int(Cart.objects.get(user_id=u_id, cereal_id=i).quantity)
    totalPrice = round(totalPrice, 2)
    return totalPrice

@login_required()
def delete_from_cart(request, id):
    if request.user.is_superuser:
        return render(request, '404.html')
    for x in Cart.objects.filter(user_id=request.user.id):
        if str(x) == str(id):
            product = get_object_or_404(Cart, pk=x.id)
            product.delete()

    return my_cart(request)

