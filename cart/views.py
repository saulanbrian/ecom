from django.shortcuts import render

from django.http import HttpResponse,JsonResponse

from django.contrib.auth.decorators import login_required

from .models import Cart
from products.models import Product
from order.models import Order

from django.urls import reverse_lazy,reverse

import json

loginurl = reverse_lazy('login')

@login_required(login_url=loginurl)
def cart(request):
  user_id = request.user.id
  products = Cart.objects.get(
    user__id=user_id).products.all()
  return render(
    request,
    'cart/index.html',
    {'products':products})
 
 
def pre_order(request):
  if request.method=='POST':
    body = request.body.decode('utf-8')
    data = json.loads(body)
    request.session['products'] = data['products']
    return JsonResponse({
      'message':'success',
      'redirect_url':reverse_lazy('preview-orders')
    })

@login_required(login_url=loginurl)
def preview(request):
  products = request.session.get('products')

  orders = []
  for product_ in products:
    order = Order(
      buyer=request.user,
      product=Product.objects.get(pk=product_['product_id']),
      amount=product_['amount']
      )
    if order:
      order.compute_total()
      orders.append(order)
  return render(request,'cart/preview.html',{'orders':orders})
 
