from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Product,Review
from cart.models import Cart

from django.http import JsonResponse

from django.core.exceptions import PermissionDenied

from django.contrib.auth.decorators import login_required

from .forms import ReviewForm

import json

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
    
def product_detail(request,pk):
  form = ReviewForm()
  product = Product.objects.get(pk=pk)
  return render(request,'products/detail.html',{'product':product,'form':form})

def add_review(request):
  if request.method=='POST':
    body = request.body.decode('utf-8')
    data = json.loads(body)
    rating = data['rating']
    feedback = data['feedback']
    product_id = data['id']
    print(type(product_id))
    product = Product.objects.get(pk=product_id)
    new_review = Review(product=product,rating=rating,feedback=feedback,user=request.user)
    new_review.save()
    return JsonResponse({'message':'review saved'})
