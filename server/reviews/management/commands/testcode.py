import random
from turtle import pen
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from reviews.models import Review 
from movies.models import Movie, Genre
from django_seed import Seed
from collections import Counter

class Command(BaseCommand): 
    help = 'this command hello' 
    def add_arguments(self, parser): 
        parser.add_argument( '--number', default=2, type=int, help='how many time show message')
        
    def handle(self, *args, **options): 
        user = get_user_model().objects.get(username='test101')
        movies = user.review_set.all()

        print(movies)