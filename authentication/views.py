from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from .forms import RegistrationForm,PasswordVerificationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.views import View

def LoginView(request):
  form = AuthenticationForm()
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(
      request,
      username=username,
      password=password)
    if user is not None:
      login(request,user)
      return HttpResponse('loggedin')
    
  return render(
    request,
    'authentication/login.html',
    {'form':form})
    
def RegisterView(request):
  form = RegistrationForm()
  if request.method == 'POST':
    form = RegistrationForm(
      request.POST)
    if form.is_valid():
      form.save()
      return render(
        request,
        'authentication/success.html')
  return render(
    request,
    'authentication/signup.html',
    {'form':form})
    
@login_required(login_url=reverse_lazy('login'))
def verify_identity(request):
  form = PasswordVerificationForm()
  if request.method=='POST':
    user = authenticate(
      username=request.user.username,
      password=request.POST.get('password'))
    if user:
      return render(request,'authentication/success.html')
    form = PasswordVerificationForm(request.POST)
  return render(request,'authentication/verification.html',{'form':form})

