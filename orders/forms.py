from django import forms
from .models import Order
from accounts.models import CustomerUser

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user']
        # model = CustomerUser
        # fields = ['username','email', 'address', 'phone', 'city']