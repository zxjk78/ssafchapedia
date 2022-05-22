from django.db import models
from numpy import character

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
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    actor = models.OneToOneField(Actor, on_delete=models.SET_NULL,null=True)
    character = models.CharField(max_length=100)