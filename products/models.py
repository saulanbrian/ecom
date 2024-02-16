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
  
  image = models.ImageField(
    upload_to='images',
    null=True)
  
  rating_ave = models.DecimalField(
    null=True,
    max_digits=2,
    decimal_places=1,
    editable=False)
  
  
  def __str__(self):
    return self.name
  
  def save(self,*args,**kwargs):
    super().save(*args,**kwargs)
    reviews = self.reviews.all()
    if reviews:
      ratings = 0
      for review in reviews:
        ratings += review.rating
      self.rating_ave = ratings/len(reviews)
      super().save(*args,**kwargs)
    
    
class Review(models.Model):
  
  choices = [
    (1, '⭐'),
    (2, '⭐⭐'),
    (3, '⭐⭐⭐'),
    (4, '⭐⭐⭐⭐'),
    (5, '⭐⭐⭐⭐⭐'),
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
    