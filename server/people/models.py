from django.db import models
from numpy import character
from ..movies.models import Movie
# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=40)
    popularity = models.FloatField()
    profile_path = models.CharField(max_length=200)


class Actor(models.Model):
    name = models.CharField(max_length=40)
    popularity = models.FloatField()
    profile_path = models.CharField(max_length=200)


class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.OneToOneField(Actor, on_delete=models.SET_NULL)
    character = models.CharField(max_length=100)