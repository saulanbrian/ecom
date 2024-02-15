from django.db import models

from shop.models import Shop
from django.contrib.auth.models import User

# Create your models here
class Product(models.Model):
  shop_origin = models.ForeignKey(Shop,
  on_delete=models.CASCADE,
  related_name='products')
  
  name = models.CharField(
    max_length=30)
  
  price = models.IntegerField()
  
  
  def __str__(self):
    return self.name
    
    
class Review(models.Model):
  
  choices = [
    (1,'⭐'),
    (2,'⭐⭐'),
  ]
  
  user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='reviews',
  )
  
  rating = models.IntegerField(
    choices=choices)
    
  feedback = models.TextField(
    max_length=100)
    
  product = models.ForeignKey(
    Product,
    on_delete=models.CASCADE,
    related_name='reviews',
    default=1
    )
    