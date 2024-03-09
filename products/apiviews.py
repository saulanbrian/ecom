from rest_framework import generics
from .serializers import ProductSerializer

from .models import Product

class ProductListView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
class ProductModifyView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  