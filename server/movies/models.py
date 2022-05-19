from django.db import models
from django.conf import settings 
from ..people.models import Director

# Create your models here.

class Genre(models.Model):
    genre = models.CharField(max_length=20)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    runtime = models.IntegerField()
    vote_arerage = models.FloatField()
    vote_count = models.IntegerField()
    release_date = models.DateField()
    poster_path = models.CharField(max_length=200)

    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, related_name='genre_movie') 