from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy, reverse

from .models import Profile

from .forms import ProfileCreationForm

@login_required(login_url=reverse_lazy('login'))
def profile(request):
  profile = request.user.profile
  return render(request,'profiles/index.html',{'profile':profile})

profile.profile_required = True

  
@login_required(login_url=reverse_lazy('login'))
def profile_creation(request):
  form = ProfileCreationForm()
  if Profile.objects.filter(user__id=request.user.id).exists():
    return redirect('profile')
  elif request.method == 'POST':
    form = ProfileCreationForm(request.POST)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = request.user
      profile.save()
      redirect_path = request.session.get('requested_url',None)
      if redirect_path:
        request.session.pop('requested_url')
        return redirect(redirect_path)
      return redirect(reverse('profile'))
  return render(request,'profiles/profilecreation.html',{'form':form})