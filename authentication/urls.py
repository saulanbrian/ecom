from django.urls import path
from . import views

urlpatterns = [
  path('login',views.LoginView,
  name='login'),
  path('signup',views.RegisterView,name='register'),
  path('password-confirmation',views.verify_identity,name='password-confirmation')
  ]