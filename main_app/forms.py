from django import forms
from .models import Athlete, Sport, Channel

class SportForm(forms.ModelForm):
  class Meta:
    model = Sport
    fields = ('name', 'description', 'location', 'gear_needed')
   

class AthleteForm(forms.ModelForm):
  class Meta:
    model = Athlete
    fields = ('name', 'age', 'hometown')

class ChannelForm(forms.ModelForm):
  class Meta:
    model = Channel
    fields = ('date', 'channel')    
    
