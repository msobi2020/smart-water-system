from django.db import models
from meters.models import Meter


class Bill(models.Model):
    STATUS_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
    ]

    meter = models.ForeignKey(Meter, on_delete=models.CASCADE, related_name='bills')
    billing_month = models.DateField(help_text="Tumia tarehe ya kwanza ya mwezi, mfano 2026-09-01")
    previous_reading = models.DecimalField(max_digits=10, decimal_places=2)
    current_reading = models.DecimalField(max_digits=10, decimal_places=2)
    rate_per_unit = models.DecimalField(max_digits=6, decimal_places=2, default=1000.00)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unpaid')
    date_generated = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        units_used = self.current_reading - self.previous_reading
        self.amount_due = units_used * self.rate_per_unit
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill #{self.id} - {self.meter.meter_number}"


class Payment(models.Model):
    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('mobile_money', 'Mobile Money'),
        ('bank', 'Bank Transfer'),
    ]

    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='payments')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=15, choices=PAYMENT_METHODS, default='cash')
    payment_date = models.DateTimeField(auto_now_add=True)
    reference_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Payment {self.amount_paid} for Bill #{self.bill.id}"
