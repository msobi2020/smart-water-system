from django.db import models
from customers.models import Customer


class Complaint(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    CATEGORY_CHOICES = [
        ('leak', 'Water Leak'),
        ('no_water', 'No Water Supply'),
        ('billing_issue', 'Billing Issue'),
        ('meter_fault', 'Meter Fault'),
        ('other', 'Other'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='complaints')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='open')
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_resolved = models.DateTimeField(blank=True, null=True)
    response_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Complaint #{self.id} - {self.customer.full_name} ({self.status})"
