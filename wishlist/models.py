from django.db import models
from products.models import Product
from django.contrib.auth.models import User

class WishList(models.Model):
  product = models.ManyToManyField(Product,related_name='products')
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  
