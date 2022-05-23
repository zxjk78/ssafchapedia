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
        
        users = get_user_model().objects.all()

        print(users)
        # 특정 유저
        user1 = get_user_model().objects.get(username='test101')
        # 장르를 담을 배열
        genre_list = []
        # 유저가 남긴 리뷰 전체
        user_reviewd = user1.review_set.all()
        print(user_reviewd)
        # 그 리뷰 하나하나의 영화
        user_reviewd_movies = user1.review_set.all().values_list('movie', flat=True)
        print(user_reviewd_movies)

        tmp = list(user_reviewd_movies)
        print(tmp)
        

        user_revie_movie_genre = user1.review_set.movie.genre_ids.all()

        print(user_revie_movie_genre)
