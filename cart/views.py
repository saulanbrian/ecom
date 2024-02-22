from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Cart

from django.urls import reverse_lazy

@login_required(
  login_url=reverse_lazy('login'))
def cart(request):
  user_id = request.user.id
  products = Cart.objects.get(
    user__id=user_id).products.all()
  return render(
    request,
    'cart/index.html',
    {'products':products})
 
  
