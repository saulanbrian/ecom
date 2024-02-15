from django.db import models
from shop.models import Shop

import uuid

# Create your models here.
class Product(models.Model):
  shop_origin = models.ForeignKey(Shop,
  on_delete=models.CASCADE,
  related_name='products')
  
  name = models.CharField(
    max_length=30)
  
  def __str__(self):
    return self.name