from django.shortcuts import render
from django.http import HttpResponse

from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login, authenticate, logout

# Create your views here.
def LoginView(request):
  form = AuthenticationForm()
  if request.method == 'POST':
    username = request.POST.get('usernae')
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
    'authentication/login.html')
    
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
