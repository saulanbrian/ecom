from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Shop(models.Model):
    owner = models.OneToOneField(
    User,on_delete=models.CASCADE)
    name = models.CharField(
    max_length=15)
    pfp = models.ImageField(upload_to='shop/images',null=True)
    
    def __str__(self):
      return self.name