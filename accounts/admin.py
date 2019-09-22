from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomerUserCreationForm, CustomerUserChangeForm
from .models import CustomerUser
# Register your models here.

class CustomerUserAdmin(UserAdmin):
    add_form = CustomerUserCreationForm
    form = CustomerUserChangeForm
    model = CustomerUser
    list_display = ['email', 'username',]

admin.site.register(CustomerUser, CustomerUserAdmin)