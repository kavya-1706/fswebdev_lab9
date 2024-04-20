from django.db import models

class Recipe(models.Model):
    dish=models.CharField(max_length=30)
    time=models.CharField(max_length=10)
    ingredients=models.TextField()
    comment=models.CharField(max_length=100)
# Create your models here.
