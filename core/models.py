
from django.db import models

# Create your models here.

statusChoice = ((1,'Hien thi'),(0 , 'An'))


class Category(models.Model):
    cate_id = models.AutoField(primary_key = 'true')
    cate_name = models.CharField(max_length= 100,null = False)
    status = models.SmallIntegerField(choices = statusChoice)
    date_create = models.DateField()

    class Meta:
        db_table = "Category"
    
    def __str__(self):
            return self.cate_name

class Brand (models.Model):
    bra_id = models.AutoField(primary_key = 'true')
    bra_name = models.CharField(max_length = 50 ,null = False)
    status = models.SmallIntegerField(choices = statusChoice)
    date_create = models.DateField()
    
    class Meta:
        db_table = "Brand"

    def __str__(self):
            return self.bra_name


class Product (models.Model):
    pro_id = models.AutoField(primary_key = 'true')
    pro_name = models.CharField(max_length = 100 , null = False)
    cate_id = models.ForeignKey(Category , on_delete = models.CASCADE)
    pro_image = models.ImageField(max_length = 255, null = False)
    pro_price = models.FloatField()
    pro_year = models.CharField(max_length = 4)
    description = models.TextField()
    status = models.SmallIntegerField(choices = statusChoice)
    date_create = models.DateField()
    bra_id = models.ForeignKey(Brand , on_delete = models.CASCADE)

    
    class Meta:
        db_table = "Product"

    def __str__(self):
            return self.pro_name
    

class User (models.Model):
    user_id = models.AutoField(primary_key = 'true')
    user_name = models.CharField(max_length = 50)
    phone = models.CharField(default='',max_length=15)
    address = models.CharField(default='',max_length=250)

    class Meta:
            db_table = "User"
            
    def __str__(self):
        return self.user_name


class Order (models.Model):
   order_id = models.AutoField(primary_key = 'true')
   user_id = models.ForeignKey(User , on_delete = models.CASCADE)
   total = models.FloatField()

   class Meta:
        db_table = "Order"


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    create_at  = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Cart"


class Variation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=250, default='')
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    status = models.SmallIntegerField(choices = statusChoice)
    inventory = models.BooleanField(default=0)

    class Meta:
        db_table = "Variation"

