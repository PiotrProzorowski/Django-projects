from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
import json
# Create your views here.

def home(request):
    return render(request, "shopsite/home.html")

def categories(request):
    return render(request, "shopsite/categories.html")

def new(request):
    new = Product.objects.filter(category="new")
    return render(request, "shopsite/new.html", {"products": new})

def sale(request):
    sale = Product.objects.filter(category="sale")
    return render(request, "shopsite/sale.html", {"products": sale})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}

    return render(request, "shopsite/cart.html", {"items": items, "order": order})

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {"get_cart_total": 0, "get_cart_items": 0}

    return render(request, "shopsite/checkout.html", {"items": items, "order": order})

def account(request):
    return render(request, "shopsite/account.html")

def watches(request):
    watches = Product.objects.filter(category="watches")
    return render(request, "shopsite/watches.html", {"products": watches})

def perfume(request):
    perfume = Product.objects.filter(category="perfume")
    return render(request, "shopsite/perfume.html", {"products": perfume})

def candles(request):
    candles = Product.objects.filter(category="candles")
    return render(request, "shopsite/candles.html", {"products": candles})

def necklaces(request):
    necklaces = Product.objects.filter(category="necklaces")
    return render(request, "shopsite/necklaces.html", {"products": necklaces})

def shoes(request):
    shoes = Product.objects.filter(category="shoes")
    return render(request, "shopsite/shoes.html", {"products": shoes})

def rings(request):
    rings = Product.objects.filter(category="rings")
    return render(request, "shopsite/rings.html", {"products": rings})

def ties(request):
    ties = Product.objects.filter(category="ties")
    return render(request, "shopsite/ties.html", {"products": ties})

def UpdateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action', action)
    print('productId', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action =='add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

