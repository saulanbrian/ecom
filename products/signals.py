from django.db.models.signals import post_save,pre_save,post_delete
from django.dispatch import receiver

from products.models import Review, Product

@receiver(post_save,sender=Review)
def trigger_product_save(
  sender,created,instance,**kwrags):
    if created:
      user_review = instance.product.reviews.filter(
        user__id=instance.user.id)
      if len(user_review)>1:
        print('you can only leave a review once in an item')
        instance.delete()
    
    instance.product.save()
    
@receiver(
  post_delete,sender=Review)
def update_product_rating(
  sender,instance,**kwargs):
    instance.product.save()
