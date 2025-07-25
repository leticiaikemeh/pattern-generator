# payments/models.py
from django.db import models
from orders.models import Order

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    method = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    reference = models.CharField(max_length=100, unique=True)
    paid_at = models.DateTimeField(null=True, blank=True)
