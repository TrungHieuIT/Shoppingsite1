from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
class RegisterForm(forms.Form):
    username=forms.CharField(label='Tai Khoan' ,max_length=30)
    email=forms.EmailField(label='Email')
    password1=forms.CharField(label='Mat khau' ,widget=forms.PasswordInput())
    password2=forms.CharField(label='Nhap lai Mat khau' ,widget=forms.PasswordInput())

    def clean_passWord2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password1']
            if password1==password2 and password1:
                return password2
        raise forms.ValidationError("Mat khau khong hop le")

    def clean_userName(self):
         username = self.cleaned_data['username']
         if not re.search(r'^/W+$',username):
             raise forms.ValidationError("Tai Khoan co ky tu dac biet")
         try:
            User.objects.get(userName=username)
         except ObjectDoesNotExist:
            return username
         raise forms.ValidationError("Tai Khoan da ton tai")
    def save(self):
         User.objects.create_user(username=self.cleaned_data['username'],email=self.cleaned_data['email'],password=self.cleaned_data['password1'])

