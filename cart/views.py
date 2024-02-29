from django.shortcuts import render,redirect

from django.http import HttpResponse,JsonResponse

from django.contrib.auth.decorators import login_required

from .models import Cart
from products.models import Product
from order.models import Order

from django.urls import reverse_lazy,reverse

import json

loginurl = reverse_lazy('login')
orders = []

@login_required(login_url=loginurl)
def cart(request):
  user_id = request.user.id
  products = Cart.objects.get(
    user__id=user_id).products.all()
  return render(
    request,
    'cart/index.html',
    {'products':products})
 
@login_required(login_url=loginurl)
def pre_order(request):
  if request.method=='POST':
    body = request.body.decode('utf-8')
    data = json.loads(body)
    orders.clear()
    request.session.pop('products',None)
    request.session['products'] = data['products']
    return JsonResponse({
      'message':'success',
      'redirect_url':reverse_lazy('preview-orders')
    })

@login_required(login_url=loginurl)
def preview(request):
  if request.method=='POST':
    request.session['redirect_url'] = reverse('order-confirmed')
    return redirect(reverse('password-confirmation'))
  products = request.session.get('products',None)
  order_confirmed = request.session.get('order_confirmed',None)
  if order_confirmed:
    request.session.pop('order_confirmed')
    for order in orders:
      order.save()
    orders.clear()
    return HttpResponse('order placed')
  elif products:
    request.session.pop('products')
    for product_ in products:
      order = Order(
        buyer=request.user,
        product=Product.objects.get(pk=product_['product_id']),
        amount=product_['amount']
        )
      order.compute_total()
      orders.append(order)
    return render(request,'cart/preview.html',{'orders':orders})
   
def order_confirmed(request):
  if request.method=='POST':
    request.session['order_confirmed'] = True
    return redirect(reverse('preview-orders'))