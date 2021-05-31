from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Sport, Athlete, Sponser, Channel
from .forms import SportForm, AthleteForm, ChannelForm 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



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
  athlete_form = AthleteForm()
  channel_form = ChannelForm()
  context = { 'sport': found_sport, 'AthleteForm': athlete_form, 'ChannelForm': channel_form}
  
  return render(request, 'sports/sports_detail.html', context)



# CHANNEL TO WATCH SPORTS
def channel_sport(request, sport_id):
  form = ChannelForm(request.POST)


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
def assoc_athlete(request, sport_id, athlete_id):
  found_sport = Sport.objects.get(id=sport_id)
  found_sport.athletes.add(athlete_id)

  return redirect('detail', sport_id)  

def add_athlete(request, sport_id):
  form = AthleteForm(request.POST)
  if form.is_valid():
    new_athlete = form.save(commit=False)
    new_athlete.sport_id = sport_id 
    new_athlete.save()
  
  return redirect('detail', sport_id = sport_id)


# ADD A CHANNEL 
def assoc_channel(request, sport_id, channel_id):
  found_sport = Sport.objects.get(id=sport_id)
  found_sport.channels.add(channel_id)

  return redirect('detail', sport_id)  

def add_channel(request, sport_id):
  form = ChannelForm(request.POST)
  if form.is_valid():
    new_channel = form.save(commit=False)
    new_channel.sport_id = sport_id 
    new_channel.save()
  
  return redirect('detail', sport_id = sport_id)


# DELETE CHANNEL
def delete_channel(request, sport_id, channel_id):
  sport=Sport.objects.get(id=sport_id)
  found_channel = Channel.objects.get(id=channel_id)
  sport.channel_set.remove(found_channel)
  return redirect('detail', sport_id = sport_id)  


# UPDATE CHANNEL
def update_channel(request, channel_id):
  channel = Channel.objects.get(id=channel_id)

  if request.method == 'GET':
    form = ChannelForm(instance=channel)
    context = {
      'form': form
    }

    return render(request, 'sports/channel_edit.html', context)
  else:
    form = ChannelForm(request.POST, instance=channel)
    if form.is_valid():
      channel = form.save()
      return redirect('detail', channel.id)  


# DELETE ATHLETE
def delete_athlete(request, sport_id, athlete_id):
  sport=Sport.objects.get(id=sport_id)
  found_athlete = Athlete.objects.get(id=athlete_id)
  sport.athlete_set.remove(found_athlete)
  return redirect('detail', sport_id = sport_id)

# ATHLETE DETAIL
def athlete_detail(request, athlete_id):
  athlete = Athlete.objects.get(id=athlete_id)

  
  sponsers_athlete_doesnt_have = Sponser.objects.exclude(athlete=athlete_id)
  context = { 'athlete': athlete, 'sponsers': sponsers_athlete_doesnt_have}

  return render(request, 'sports/athlete_detail.html', context) 


# ADD A SPONSER TO AN ATHLETE
def assoc_sponser(request, athlete_id, sponser_id):
  found_athlete = Athlete.objects.get(id=athlete_id)
  found_athlete.sponsers.add(sponser_id)
  return redirect('athlete_detail', athlete_id = athlete_id)


def remove_sponser(request, athlete_id, sponser_id):
  Athlete.objects.get(id=athlete_id).sponsers.remove(sponser_id)
  return redirect('athlete_detail', athlete_id=athlete_id)



# SIGNUP FUNCTION
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'  

  form = UserCreationForm()      

  context = {
    'form': form,
    'error_message': error_message
  }

  return render(request, 'registration/signup.html', context)


# DELETE ATHLETE 
# def delete_athlete(request, athlete_id):
#   athlete = Athlete.objects.get(id=athlete_id)
#   athlete.delete()
#   return redirect('index')

# def athlete_set(request, athlete_id):
#   athlete = Athlete.objects.get(id=athlete_id)
#   # sport.athlete_set.clear()
#   return redirect('index')



# DETAIL SPORTS
# def detail(request, sport_id):
#   found_sport = Sport.objects.get(id=sport_id)
#   athlete_form = AthleteForm()
#   context = { 'sport': found_sport, 'AthleteForm': athlete_form }
#   return render(request, 'sports/sports_detail.html', context)
