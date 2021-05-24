from django.shortcuts import render
from django.http import HttpResponse

class Sport:
  def __init__(self, name, description = 'no description', is_fun = True):
    self.name = name
    self.description = description
    self.is_fun = is_fun


sports = [
  Sport('Skiing', 'needs snow'),
  Sport('Mountain Biking', 'needs a bike'),
  Sport('Hiking'),
  Sport('Mountaineering'),
  Sport('Running', is_fun = False)
]


# Create your views here.
def home(request):
  return HttpResponse('<h1>sports!</h1>') 

def index(request):
  context = { 'sports': sports }
  return render(request, 'index.html', context)

def about(request):
  context = { 'sports': sports }
  return render(request, 'about.html', context )  