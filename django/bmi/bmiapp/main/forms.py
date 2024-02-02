from django import forms
from django.forms import ModelForm
from .models import BMImodel

class BMIform(ModelForm):
    weight = forms.FloatField(min_value=1)
    height = forms.FloatField(min_value=1)
    class Meta:
        model = BMImodel
        fields = "__all__"