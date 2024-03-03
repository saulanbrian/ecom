from django.db import models

from django.contrib.auth.models import User
from products.models import Product

from django.utils import timezone

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
  
  date_placed = models.DateTimeField(auto_now_add=True)
  
  date_received = models.DateTimeField(null=True)
  
  def confirm_receive(self):
    self.data_received = timezone.now()
    self.received = True
  
  def compute_total(self):
    price = self.product.price
    total = price * self.amount
    self.price = total  