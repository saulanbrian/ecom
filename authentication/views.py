from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse

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
    user = authenticate(request,username=username,password=password)
    if user is not None:
      login(request,user)
      return HttpResponse('loggedin')   
  return render(request,'authentication/login.html',{'form':form})

    
def RegisterView(request):
  form = RegistrationForm()
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      return render(request,'authentication/success.html')
  return render(request,'authentication/signup.html',{'form':form})

    
@login_required(login_url=reverse_lazy('login'))
def verify_identity(request):
  redirect_url = request.session.get('requested_url',None)
  if redirect_url:
    form = PasswordVerificationForm()
    if request.method == 'POST':
      form = PasswordVerificationForm(request.POST)
      user = authenticate(username=request.user.username,password=request.POST.get('password'))
      if user:
        request.session['is_authenticated'] = True
        request.session.pop('requested_url')
        return redirect(redirect_url)
    return render(request,'authentication/verification.html',{'form':form,'redirect_url':redirect_url})
  return redirect(reverse('home'))
