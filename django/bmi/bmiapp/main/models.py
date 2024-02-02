from django.db import models

# Create your models here.

class BMImodel(models.Model):
    weight = models.FloatField()
    height = models.FloatField()
    
    def bmi(self):
        return weight / height ** 2