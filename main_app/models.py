from django.db import models
from django.contrib.auth.models import User 
# from django.db.models.fields import CharField


# Create your models here.
class Sport(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=250)
  location = models.TextField(max_length=250)
  is_fun = models.BooleanField(default=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)


class Athlete(models.Model):
  name = models.CharField(max_length=100)
  age = models.IntegerField()

  sport = models.ForeignKey(Sport, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return f'{self.name}'