from django import forms
from django.db import models
from django.db.models import fields
from .models import Order, OrderItem

#creating a class for orderform 
class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields='__all__'
class OrderItemForm(forms.ModelForm):
    class Meta: 
        model = OrderItem
        fields = '__all__'