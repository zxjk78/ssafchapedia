from django.db import models

# Create your models here.

class Actor(models.Model):
    actor_id = models.IntegerField()
    name = models.CharField(max_length=40)
    korean_name = models.CharField(max_length=40, null=True)
    popularity = models.FloatField(null=True)
    profile_path = models.CharField(max_length=200, null=True)
    movies = models.ManyToManyField('movies.Movie', through='Cast', related_name='actors')

class Cast(models.Model):
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

class Tmp(models.Model):
    actor_id = models.IntegerField(unique=True)

