from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

from .models import Order
from django.contrib.auth.models import User

import json

@login_required(login_url=reverse_lazy('login'))
def orders(request):
  orders = request.user.orders.all()
  return render(request,'order/all.html',{'orders':orders})
  
def receive_order(request):
  if request.method == 'POST':
    body = request.body.decode('utf-8')
    data = json.loads(body)
    order_id = data['order_id']
    order = Order.objects.get(pk=order_id)
    order.confirm_receive()
    order.save()
    return JsonResponse({
      'message':'success'
    })

def received_orders(request):
  id = request.user.id
  orders = Order.objects.filter(buyer_id=id)
  orders = orders.filter(received=True)
  return render(request,'order/received.html',{'orders':orders})
  
def to_receive(request):
  id = request.user.id
  orders = Order.objects.filter(buyer_id=id)
  orders = orders.filter(is_cancelled=False,received=False)
  return render(request,'order/toreceive.html',{'orders':orders})
  
def cancelled_orders(request):
  id = request.user.id
  orders = Order.objects.filter(buyer_id=id)
  orders = orders.filter(is_cancelled=True)
  return render(request,'order/cancelled.html',{'orders':orders})
  
def cancel_order(request):
  if request.method == 'POST':
    body = request.body.decode('utf-8')
    data = json.loads(body)
    order_id = data['order_id']
    order = Order.objects.get(pk=order_id)
    order.cancel()
    order.save()
    return JsonResponse({
      'message':'success'
    })