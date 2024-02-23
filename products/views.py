from django.shortcuts import render

from .models import Product
from cart.models import Cart

from django.http import JsonResponse

from django.core.exceptions import PermissionDenied

from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

def products(request):
  products = Product.objects.all()
  return render(
    request,
    'products/index.html',
    {'products':products})

def add_to_cart(request):
  try: 
    if request.user.is_authenticated:
      id_ = request.POST.get('id_')
      user = request.user
      product = Product.objects.get(pk=id_)
      user.cart.products.add(product)
      user.cart.save()
      return JsonResponse({
        'success':True,
        'message':'added to cart successfuly',
      })
    else:
      raise PermissionDenied
  except PermissionDenied as e:
    print('lgin required')
    return JsonResponse({
      'error':str(e),
      'message':'error: make sure you are logged'
    },status=403)
    
