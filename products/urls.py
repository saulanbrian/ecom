from django.urls import path
from . import views

urlpatterns = [
  path('',views.products,name='products'),
  path('add',views.add_to_cart,name='add-to-cart')
  ]