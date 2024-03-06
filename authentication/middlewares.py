from django.shortcuts import render,redirect
from django.urls import reverse

class VerificationMiddleware:
  
  def __init__(self,get_response):
    self.get_response = get_response
    
  def __call__(self,request):
    response = self.get_response(request)
    return response
   
  def process_view(self,request,view_func,view_args,view_kwargs):
    authenticated = request.session.get('is_authenticated',None)
    if hasattr(view_func,'authentication_required') and not authenticated:
      restricted_path = request.path 
      print(restricted_path)
      request.session['requested_url'] = restricted_path
      return redirect(reverse('password-confirmation'))