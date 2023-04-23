from django import forms
from .models import Cart

#creating a class for cartform 
class CartForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields='__all__'