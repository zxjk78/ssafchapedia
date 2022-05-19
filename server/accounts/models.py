from django.db import models
from django.contrib.auth.models import AbstractUser
from ..movies.models import Movie
# Create your models here.
class User(AbstractUser):
    like = models.ManyToManyField(Movie, related_name='like_users', blank= True)
    watch = models.ManyToManyField(Movie, related_name='watch_users', blank= True)
    wish = models.ManyToManyField(Movie, related_name='wish_users', blank= True)
    
