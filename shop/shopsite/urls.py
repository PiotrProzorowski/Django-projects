from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path("ties/", views.ties, name="ties"),
    path("rings/", views.rings, name="rings"),
    path("necklaces/", views.necklaces, name="necklaces"),
    path("shoes/", views.shoes, name="shoes"),
    path("candles/", views.candles, name="candles"),
    path("update_item/", views.UpdateItem, name="update_item")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)