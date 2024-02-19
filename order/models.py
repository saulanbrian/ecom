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
  
  def confirm_receive(self):
    self.received = True
