from django.shortcuts import render
from .models import Product

from django.http import JsonResponse

def products(request):
  products = Product.objects.all()
  return render(
    request,
    'products/index.html',
    {'products':products})

def add_to_cart(request):
  print('got here')
  return JsonResponse({
    'message':'success'
  })