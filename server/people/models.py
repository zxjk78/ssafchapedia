from django.db import models

# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=40)
    popularity = models.FloatField()
    profile_path = models.CharField(max_length=200)


class Actor(models.Model):
    actor_id = models.IntegerField()
    name = models.CharField(max_length=40)
    korean_name = models.CharField(max_length=40, null=True)
    popularity = models.FloatField(null=True)
    profile_path = models.CharField(max_length=200, null=True)


class Cast(models.Model):
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)

class Tmp(models.Model):
    actor_id = models.IntegerField(unique=True)

