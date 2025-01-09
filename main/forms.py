from django import forms
from .models import Ride
class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['source', 'destination', 'date', 'available_seats', 'price_per_seat', 'description']
        widgets = {
            'source': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter starting location',
            }),
            'destination': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter destination',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'available_seats': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Person',
            }),
            'price_per_seat': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price per seat (₹)',
                'step': '0.01',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'type':'text-area',
                'placeholder': 'Additional details (optional)',
                'rows': 3,
            }),
        }
