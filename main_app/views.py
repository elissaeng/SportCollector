from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Sport, Athlete
from .forms import SportForm



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

# DETAIL SPORTS
def detail(request, sport_id):
  found_sport = Sport.objects.get(id=sport_id)
  context = { 'sport': found_sport }
  return render(request, 'sports/sports_detail.html', context)


# CREATE SPORTS
def create_sport(request):
  if request.method == 'GET':
    form = SportForm()
    context = {
      'form': form,
    }
    return render(request, 'sports/sports_new.html', context)
  else:
    form = SportForm(request.POST)
    if form.is_valid():
      sport = form.save()
      return redirect('detail', sport.id)


# DELETE SPORTS 
def delete_sport(request, sport_id):
  sport = Sport.objects.get(id=sport_id)
  sport.delete()
  return redirect('index')



# UPDATE SPORTS
def update_sport(request, sport_id):
  sport = Sport.objects.get(id=sport_id)

  if request.method == 'GET':
    form = SportForm(instance=sport)
    context = {
      'form': form
    }

    return render(request, 'sports/sports_edit.html', context)
  else:
    form = SportForm(request.POST, instance=sport)
    if form.is_valid():
      sport = form.save()
      return redirect('detail', sport.id)




# ADD AN ATHLETE
def assoc_athlete(request, sport_id, toy_id):
  found_sport = Sport.objects.get(id=sport_id)
  found_sport.athletes.add(athlete_id)

  return redirect('detail', sport_id)      