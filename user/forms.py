from django import forms
from .models import Customers


class RegisterUser(forms.ModelForm):
    class Meta:
        model = Customers
        fields = (
            'name',
            'age',
            'phone',
            'email',
            'country',
        )
        