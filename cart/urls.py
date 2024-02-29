from django.urls import path

from . import views

urlpatterns = [
  path('',views.cart,name='cart'),
  path('pre-order',views.pre_order,
  name='pre-order'),
  path('preview',views.preview,name='preview-orders'),
  path('confirm',views.order_confirmed,name='order-confirmed')
  ]