from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("calculate/", views.calculate, name="calculate"),
    path("results/", views.results, name="results")
]