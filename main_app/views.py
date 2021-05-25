from django.shortcuts import render
from django.http import HttpResponse
from .models import Sport



# Create your views here.
def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')  


def reviews(request):
    return render(request, 'reviews.html')


def index(request):
  sports = Sport.objects.all()
  context = { 'sports': sports}
  return render(request, 'sports/sports_index.html', context)  


def detail(request, sport_id):
  found_sport = Sport.objects.get(id=sport_id)
  context = { 'sport': found_sport }
  return render(request, 'sports/sports_detail.html', context)



