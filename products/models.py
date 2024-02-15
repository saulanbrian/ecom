from django.db import models
from shop.models import Shop

# Create your models here.
class Review(models.Model):
  
  choices = [
    (1,'⭐'),
    (2,'⭐⭐'),
  ]
  
  rating = models.IntegerField(
    choices=choices)
    
  feedback = models.TextField(
    max_length=100)
   


class Product(models.Model):
  shop_origin = models.ForeignKey(Shop,
  on_delete=models.CASCADE,
  related_name='products')
  
  name = models.CharField(
    max_length=30)
  
  price = models.IntegerField(
    null=True)
  
  
  def __str__(self):
    return self.name
    
    
class Review(models.Model):
  
  choices = [
    (1,'⭐'),
    (2,'⭐⭐'),
  ]
  
  rating = models.IntegerField(
    choices=choices)
    
  feedback = models.TextField(
    max_length=100)
    
  product = models.ForeignKey(
    Product,
    on_delete=models.CASCADE,
    related_name='reviews'
    )