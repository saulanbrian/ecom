from django.shortcuts import render,redirect

from django.http import HttpResponse,JsonResponse

from django.contrib.auth.decorators import login_required

from .models import Cart
from products.models import Product
from order.models import Order

from django.urls import reverse_lazy,reverse

import json
import pickle
import base64

login_url = reverse_lazy('login')


@login_required(login_url=login_url)
def cart(request):
  user_id = request.user.id
  products = Cart.objects.get(
    user__id=user_id).products.all()
  return render(request,'cart/index.html',{'products':products})

 
@login_required(login_url=login_url)
def pre_order(request):
  if request.method=='POST':
    body = request.body.decode('utf-8')
    data = json.loads(body)
    request.session.pop('orders',None)
    request.session['orders'] = data['products']
    return JsonResponse({
      'message':'success',
      'redirect_url':reverse_lazy('preview-orders')
    })
  return redirect(reverse('cart'))


@login_required(login_url=login_url)
def preview(request):
  if request.method == 'POST':
    return redirect(reverse('save-orders'))
  request.session['pickled_orders'] = []
  orders = request.session.get('orders',None)
  if orders:
    requested_orders = []
    for order in orders:
      product = Product.objects.get(pk=order['product_id'])
      new_order = Order(buyer=request.user, product=product, amount=order['amount'])
      new_order.compute_total()
      requested_orders.append(new_order)
      pickled = pickle.dumps(new_order)
      serialized = base64.b64encode(pickled).decode('utf-8')
      request.session['pickled_orders'].append(serialized)
    for order in requested_orders:
      print(order.price)
    return render(request,'cart/preview.html',{'orders':requested_orders})
  return redirect('cart')

@login_required(login_url=reverse_lazy('login'))
def save_orders(request):
  orders = request.session.get('pickled_orders',None)
  if orders:
    for encoded_order in orders:
      decoded_order = base64.b64decode(encoded_order)
      unpickled_order = pickle.loads(decoded_order)
      unpickled_order.save()
    request.session.pop('orders')
    request.session.pop('pickled_orders')
    return HttpResponse('orders saved')
  return redirect(reverse('home'))

save_orders.authentication_required = True
save_orders.profile_required = True