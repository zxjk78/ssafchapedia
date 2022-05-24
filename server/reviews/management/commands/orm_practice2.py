import random
from turtle import pen
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.models import F
from reviews.models import Review 
from movies.models import Movie, Genre
from django_seed import Seed
from collections import Counter

class Command(BaseCommand): 
    help = 'this command hello' 
    def add_arguments(self, parser): 
        parser.add_argument( '--number', default=2, type=int, help='how many time show message')
        
    def handle(self, *args, **options): 
        
        # 특정 유저
        user1 = get_user_model().objects.get(username='test101') # 1
        # 장르를 담을 배열
        genre_list = []
        # 유저가 남긴 리뷰 전체의 하나하나의 영화번호
        user_reviewed_movies = user1.review_set.all().values_list('movie', flat=True) # 2
        # user_reviewed_movies = user1.review_set.annotate(score = F('directing') + F('art') + F('music')+ F('acting') + F('acting')).filter('score__gt=10').values_list('movie', flat=True) # 2
        tmp = list(user_reviewed_movies)
        
        genre_cnt_list = []
        for movie_no in tmp:
            movie = Movie.objects.get(pk=movie_no)
            genres = movie.genre_ids.all()
            for genre in genres:
                genre_cnt_list.append(genre.pk)
        
        action_code = Counter(genre_cnt_list).most_common(1)[0][0]
        movie_recommend = Movie.objects.filter(genre_ids = action_code).exclude(id__in=user_reviewed_movies).order_by('-vote_average')[:10]

        print(movie_recommend)