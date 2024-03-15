from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  address = models.CharField(max_length=100)
  email = models.EmailField()
  contact_number = models.IntegerField()