from django.contrib import admin
from .models import Category,Product,Variation,Cart,Order,User,Brand
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(User)
admin.site.register(Variation)
