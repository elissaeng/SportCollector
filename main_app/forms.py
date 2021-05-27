from django import forms
from .models import Athlete, Sport

class SportForm(forms.ModelForm):
  class Meta:
    model = Sport
    fields = ('name', 'description', 'location', 'is_fun')
    labels = {'is_fun': 'label for is fun'}

class AthleteForm(forms.ModelForm):
  class Meta:
    model = Athlete
    fields = ('name', 'age')
    
