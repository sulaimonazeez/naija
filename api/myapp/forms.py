from .models import musicUploaders, New, Movies
from django import forms
class postData(forms.ModelForm):
  class Meta:
    model = musicUploaders
    fields = '__all__'