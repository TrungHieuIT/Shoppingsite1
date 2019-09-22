from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomerUser(AbstractUser):
    phone = models.CharField(default='',max_length=15)
    address = models.CharField(default='',max_length=200)
    city =  models.CharField(default='',max_length=100)

    def __str__(self):
        return self.email

