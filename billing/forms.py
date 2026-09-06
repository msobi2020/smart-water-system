from django import forms
from .models import Bill, Payment


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['meter', 'billing_month', 'previous_reading', 'current_reading', 'rate_per_unit']
        widgets = {
            'meter': forms.Select(attrs={'class': 'form-select'}),
            'billing_month': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'previous_reading': forms.NumberInput(attrs={'class': 'form-control'}),
            'current_reading': forms.NumberInput(attrs={'class': 'form-control'}),
            'rate_per_unit': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['bill', 'amount_paid', 'payment_method', 'reference_number']
        widgets = {
            'bill': forms.Select(attrs={'class': 'form-select'}),
            'amount_paid': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
            'reference_number': forms.TextInput(attrs={'class': 'form-control'}),
        }