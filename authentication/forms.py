from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User

class RegistrationForm(
  UserCreationForm):
    class Meta:
      model = User
      fields = [
        'username',
        'password1',
        'password2'
        ]
  
    def __init__(self,*args,**kwargs):
      super().__init__(*args,**kwargs)
      for field in self.fields:
        self.fields[field].widget.attrs.update({
          'placeholder':field
        })

class PasswordVerificationForm(forms.Form):
  password = forms.CharField(label='password')
    
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.fields['password'].widget.attrs['placeholder'] = 'enter your password'
    
class CustomAuthenticationForm(AuthenticationForm):
  class Meta:
    model = User 
    fields = ['username','password']

  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    for field in self.fields:
      self.fields[field].widget.attrs.update({
        'placeholder':field
      })