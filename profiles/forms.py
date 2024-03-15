from django import forms

from .models import Profile

class ProfileCreationForm(forms.ModelForm):
  class Meta:
    model = Profile 
    exclude = ('user',)
  
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    for field in self.fields:
      self.fields[field].widget.attrs.update({
        'placeholder':self.fields[field].label
      })