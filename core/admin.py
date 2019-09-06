from django.contrib import admin
from .models import Category,Product,Brand
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cate_name', 'slug']
    prepopulated_fields = {'slug': ('cate_name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pro_name', 'slug','brand_id', 'price','pro_image', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at', 'updated_at']
    list_editable = ['price','status','pro_image']
    prepopulated_fields = {'slug': ('pro_name',)}


admin.site.register(Product, ProductAdmin)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand_name', 'slug']
    prepopulated_fields = {'slug': ('brand_name',)}
    
admin.site.register(Brand,BrandAdmin)



