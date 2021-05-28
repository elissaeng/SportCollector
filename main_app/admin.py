from django.contrib import admin
from .models import Athlete, Sport, Sponser

# Register your models here.
admin.site.register(Sport)
admin.site.register(Athlete)
admin.site.register(Sponser)