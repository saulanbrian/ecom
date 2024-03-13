from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Profile

class ProfileMiddleware:
  
  def __init__(self,get_response):
    self.get_response = get_response
    
  def __call__(self,request):
    response = self.get_response(request)
    return response
  
  def process_view(self,request,view_func,view_args,view_kwargs):
    has_profile = Profile.objects.filter(user_id=request.user.id).exists()
    if hasattr(view_func,'profile_required') and not has_profile:
      request.session['requested_url'] = request.path
      return redirect(reverse('profile-creation'))
    