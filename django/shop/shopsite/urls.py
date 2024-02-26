from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("categories/", views.categories, name="categories"),
    path("new/", views.new, name="new"),
    path("sale/", views.sale, name="sale"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("account/", views.account, name="account"),
    path("watches/", views.watches, name="watches"),
    path("perfume/", views.perfume, name="perfume"),
    path("ties/", views.perfume, name="ties"),
    path("rings/", views.perfume, name="rings"),
    path("necklaces/", views.perfume, name="necklaces"),
    path("shoes/", views.perfume, name="shoes"),
    path("candles/", views.perfume, name="candles")
]