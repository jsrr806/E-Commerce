from django import forms

from .models import Order

class AddressForm(forms.ModelForm):
    class Meta:
        model = Order
        fields=[
            'address',
        ]
