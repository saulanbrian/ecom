from django.urls import path
from . import views

urlpatterns = [
  path('',views.products,name='products'),
  path('add',views.add_to_cart,name='add-to-cart'),
  path('<pk>/detail',views.product_detail,name='product-detail'),
  path('add-review',views.add_review,name='add-review')
  ]