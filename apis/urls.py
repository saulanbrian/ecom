from django.urls import path

from products import apiviews as product_api_views

urlpatterns = [
  path('products',product_api_views.ProductListView.as_view()),
  path('products/<int:pk>',product_api_views.ProductModifyView.as_view())
  ]