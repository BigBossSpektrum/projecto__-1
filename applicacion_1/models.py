# models.py
from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def discounted_price(self):
        return self.price * 0.7  # Aplicando el 30% de descuento

    def __str__(self):
        return self.name
