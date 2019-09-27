from django import forms
from .models import Order
from accounts.models import CustomerUser

class OrderCreateForm(forms.ModelForm):
    class Meta():
        model = CustomerUser
        fields = ['first_name', 'last_name','email', 'address', 'phone', 'city']
        model = Order
        fields = ['user']