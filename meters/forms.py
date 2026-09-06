from django import forms
from .models import Meter


class MeterForm(forms.ModelForm):
    class Meta:
        model = Meter
        fields = ['customer', 'meter_number', 'location', 'installation_date', 'status']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-select'}),
            'meter_number': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'installation_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }