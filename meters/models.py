
from django.db import models
from customers.models import Customer


class Meter(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('faulty', 'Faulty'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='meters')
    meter_number = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    installation_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.meter_number} - {self.customer.full_name}"