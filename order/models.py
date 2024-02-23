from django.db import models

from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
  buyer = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='orders')
  
  product = models.ForeignKey(
    Product,
    on_delete=models.CASCADE,
    related_name='orders')
  
  received = models.BooleanField(
    default=False)
  
  amount = models.IntegerField(default=1)
  
  price = models.IntegerField(
    null=True,editable=False)
  
  def confirm_receive(self):
    self.received = True
  
  def save(self,*args,**kwargs):
    price = self.product.price
    total = price * self.amount
    self.price = total
    super().save(*args,**kwargs)