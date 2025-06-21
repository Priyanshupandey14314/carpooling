from django import forms
from .models import Ride
class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['source', 'destination', 'date', 'gender',
            'available_seats', 'price_per_seat', 'description',
            'driver_name', 'driver_phone']
        widgets = {
            'source': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter source location'}),
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter destination'}),
            'driver_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'driver_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your phone number'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notes about the ride (optional)', 'rows': 3}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'available_seats': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'price_per_seat': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
        }
