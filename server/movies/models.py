from django.db import models
from django.conf import settings 
from people.models import Director

# Create your models here.

class Genre(models.Model):
    genre = models.CharField(max_length=20)

class Movie(models.Model):
    pk = models.IntegerField()

    genre_ids = models.ManyToManyField(Genre)
    poster_path = models.CharField(max_length=200, blank=True, null=True)
    adult = models.BooleanField()
    title = models.CharField(max_length=100)
    overview = models.TextField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    original_title = models.CharField(max_length=100)
    original_language = models.CharField(max_length=100)
    popularity = models.FloatField(null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)
    vote_average = models.FloatField(null=True, blank=True) 