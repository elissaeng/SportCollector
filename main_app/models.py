from django.db import models
# from django.db.models.fields import CharField

# Create your models here.
class Sport(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(max_length=250)
  is_fun = models.BooleanField(max_length=50)