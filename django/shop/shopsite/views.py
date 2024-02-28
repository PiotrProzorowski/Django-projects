from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
# Create your views here.

def home(request):
    return render(request, "shopsite/home.html")

def categories(request):
    return render(request, "shopsite/categories.html")

def new(request):
    return render(request, "shopsite/new.html")

def sale(request):
    return render(request, "shopsite/sale.html")

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

