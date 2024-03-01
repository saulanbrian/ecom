from django.shortcuts import render
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required

from .models import Order
from django.contrib.auth.models import User

@login_required(login_url=reverse_lazy('login'))
def orders(request):
  orders = request.user.orders.all()
  return render(request,'order/index.html',{'orders':orders})