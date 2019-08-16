from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250,default='')
    slug = models.CharField(max_length=100,default='')
    description = models.TextField(default='')
    active = models.BooleanField(default=True)


class Product(models.Model):
    title = models.CharField(max_length=250, default='')
    product_img = models.CharField(max_length=225, default='')
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField(default='')
    active = models.BooleanField(default=True)


class Variation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=250, default='')
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    inventory = models.BooleanField(default=0)
