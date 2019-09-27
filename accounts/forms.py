from django import forms
from .models import CustomerUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomerUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomerUser
        fields =('username', 'email','password1', 'password2',)

class CustomerUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomerUser
        fields =('username','email')