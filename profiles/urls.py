from django.urls import path

from . import views

urlpatterns = [
  path('',views.profile,name='profile'),
  path('create',views.profile_creation,name='profile-creation')
  ]