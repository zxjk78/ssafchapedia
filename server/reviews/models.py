from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from movies.models import Movie
# Create your models here.
user = settings.AUTH_USER_MODEL

class Review(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    
    directing = models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(1)])
    music = models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(1)])
    story = models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(1)])
    acting = models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(1)])
    art = models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(1)])