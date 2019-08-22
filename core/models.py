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


class Product (models.Model):
    pro_id = models.AutoField(primary_key = 'true')
    pro_name = models.CharField(max_length = 100 , null = False)
    cate_id = models.ForeignKey(Category , on_delete = models.CASCADE)
    pro_image = models.ImageField(max_length = 255, null = False)
    pro_price = models.FloatField()
    description = models.TextField()
    status = models.SmallIntegerField(choices = statusChoice)
    date_create = models.DateField()

    class Meta:
        db_table = "Product"

    def __str__(self):
            return self.pro_name
    

#class Order (models.Model):
   # order_id = models.AutoField(primary_key = 'true')
   # user_id = models.ForeignKey(User , on_delete = models.CASCADE)
   # total = models.FloatField()



#class User (models.Model):
  #  user_id = models.AutoField(primary_key = 'true')
  #  user_name = models.CharField(max_length = 50)
  #  phone = models.CharField(default='',max_length=15)
  #  address = models.CharField(default='',max_length=250)

   # def __str__(self):
   #         return self.user_name