from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
    return render(request, "shopsite/cart.html")

def checkout(request):
    return render(request, "shopsite/checkout.html")

def account(request):
    return render(request, "shopsite/account.html")

def watches(request):
    return render(request, "shopsite/watches.html")

def perfume(request):
    return render(request, "shopsite/perfume.html")

def candles(request):
    return render(request, "shopsite/candles.html")

def necklaces(request):
    return render(request, "shopsite/necklaces.html")

def shoes(request):
    return render(request, "shopsite/shoes.html")

def rings(request):
    return render(request, "shopsite/rings.html")

def ties(request):
    return render(request, "shopsite/ties.html")

