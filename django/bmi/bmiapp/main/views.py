from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import BMIform

# Create your views here.

def home(response):
    return render(response, "main/home.html")

def calculate(response):
    if response.method == "POST":
        form = BMIform(response.POST)
        if form.is_valid():
            weight = form.cleaned_data["weight"]
            height = form.cleaned_data["height"]
            bmi = round(weight / height ** 2, 2)
            return render(response, "main/calculate.html", {"form": form, "bmi": bmi})
    else: 
        form = BMIform()
    return render(response, "main/calculate.html", {"form": form})

def results(response):
    return render(response, "main/results.html")