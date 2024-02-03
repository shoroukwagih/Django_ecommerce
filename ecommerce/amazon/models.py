# models.py
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=150)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
