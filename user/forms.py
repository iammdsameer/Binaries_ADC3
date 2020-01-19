from django import forms
from .models import Customers


class RegisterUser(forms.ModelForm):
    class Meta:
        model = Customers
        fields = (
            'f_name',
            'm_name',
            'l_name',
            'dob',
            'phone',
            'email',
            'gender'
            
            
        )
        