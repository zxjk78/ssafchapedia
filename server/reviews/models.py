from xml.parsers.expat import model
from django.db import models
from django.conf import settings
from movies.models import Movie
# Create your models here.
user = settings.AUTH_USER_MODEL

class Review(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    directing = models.IntegerField()
    music = models.IntegerField()
    story = models.IntegerField()
    acting = models.IntegerField()
    art = models.IntegerField()