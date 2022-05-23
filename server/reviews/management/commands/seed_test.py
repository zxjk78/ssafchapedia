import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from reviews.models import Review 
from movies.models import Movie
from django_seed import Seed

class Command(BaseCommand): 
    help = 'this command hello' 
    def add_arguments(self, parser): 
        parser.add_argument( '--number', default=2, type=int, help='how many time show message')
        
    def handle(self, *args, **options): 
        number = options.get('number')
        seeder =Seed.seeder()
        users = get_user_model().objects.all()
        movies = Movie.objects.all()

        seeder.add_entity(Review, number, {
            'user': lambda x: random.choice(users),
            'movie': lambda x: random.choice(movies),
            'directing': lambda x: random.randint(1,3),
            'music': lambda x: random.randint(1,3),
            'story': lambda x: random.randint(1,3),
            'acting': lambda x: random.randint(1,3),
            'art': lambda x: random.randint(1,3),
        })

        seeder.execute()
