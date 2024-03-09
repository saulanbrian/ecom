from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ('id','shop_origin','price','image','rating_ave',)