from django.db import models
from django.contrib.auth.models import User 
# from django.db.models.fields import CharField

CHANNEL = (
  ('E', 'ESPN'),
  ('F', 'Fox Sports'),
  ('R', 'RedBull TV')
)

# SPONSER
class Sponser(models.Model):
  name = models.CharField(max_length=150)

  def __str__(self):
    return f'{self.name}'


# Create your models here.

# SPORT
class Sport(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=250)
  location = models.TextField(max_length=250)
  gear_needed = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name}'


# SPORT CHANNEL
 class Channel(models.Model):
  date = models.DateField()
  channel = models.CharField(
    max_length=1,
    choices=CHANNEL,
    default=CHANNEL[0][0]
  )
  sport = models.ForeignKey(Sport, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return f'{self.get_channel_display()} on {self.date}'



# ATHLETE
class Athlete(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  hometown = models.TextField(max_length=100)
  sponsers = models.ManyToManyField(Sponser, blank=True)

  sport = models.ForeignKey(Sport, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return f'{self.name} | {self.age}'