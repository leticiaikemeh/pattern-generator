# patterns/models.py
from django.db import models
from orders.models import Order

class Pattern(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    file_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

