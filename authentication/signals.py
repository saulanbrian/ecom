from django.db.models.signals import post_save

from django.contrib.auth.models import User
from cart.models import Cart

from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_cart(sender,created,instance,**kwargs):
  if created:
    cart = Cart(user=instance)
    cart.save()
    print(f'cart made for{instance}')