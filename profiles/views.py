from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy, reverse

from .models import Profile

from .forms import ProfileCreationForm

@login_required(login_url=reverse_lazy('login'))
def profile(request):
  profile = Profile.objects.filter(user__id=request.user.id)
  if profile:
    return render(request,'profiles/index.html')
  return redirect(reverse('profile-creation'))
  
@login_required(login_url=reverse_lazy('login'))
def profile_creation(request):
  if Profile.objects.filter(user__id=request.user.id).exists():
    return redirect('profile')
  form = ProfileCreationForm()
  if request.method == 'POST':
    form = ProfileCreationForm(request.POST)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = request.user
      profile.save()
      return redirect(reverse('profile'))
  return render(request,'profiles/profilecreation.html',{'form':form})