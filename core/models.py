from django.db import models
from django.urls import reverse
# Create your models here.

statusChoice = ((1,'Hien thi'),(0 , 'An'))

class Category(models.Model):
    cate_name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.SmallIntegerField(choices = statusChoice)

    class Meta:
        db_table = "Category"

    def __str__(self):
            return self.cate_name

    def get_absolute_url(self):
        return reverse('core:index', args=[self.slug])
    


class Brand (models.Model):
    brand_name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    status = models.SmallIntegerField(choices = statusChoice)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "Brand"

    def __str__(self):
            return self.brand_name


class Product (models.Model):
    cate_id = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    pro_name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank = True)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pro_image = models.ImageField(max_length = 255, null = False)
    pro_year = models.CharField(max_length = 4)
    brand_id = models.ForeignKey(Brand , on_delete = models.CASCADE) 
    status = models.SmallIntegerField(choices = statusChoice)
    vote = models.IntegerField(default=0)
    
    class Meta:
        ordering = ('pro_name', )
        index_together = (('id', 'slug'),)
        db_table = "Product"

    def __str__(self):
            return self.pro_name

    def get_absolute_url(self):
        return reverse('core:product_detail', args=[self.id,self.slug])
    
    




