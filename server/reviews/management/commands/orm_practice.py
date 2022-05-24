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
        # 그 리뷰 하나하나의 영화
        user_movies_id = []
        for review in user_reviewd:
            movie = review.movie
            user_movies_id.append(movie.id)
            print(movie)
            # 영화의 장르
            genres = movie.genre_ids.all()

            for genre in genres:
                genre_list.append(genre.genre)
        
        print(genre_list)

        cnt = Counter(genre_list)

        print(cnt)
        # Counter({'Action': 4, 'Fantasy': 3, 'Drama': 3, 'Adventure': 2, 'Science Fiction': 2, 'Animation': 2, 'Comedy': 2, 'Family': 2, 'War': 1, 'Thriller': 1, 'Horror': 1})
        print(Counter(genre_list).most_common(1))
        # [('Action', 4)]

        # action을 제일 좋아한다는 것을 알았으니, 액션영화를 추천해주면 되는데, 그중에서 유저가 안본 것을 골라서, 평점 높은 순으로 추천해줘야함.
        action_code = Genre.objects.get(genre='Action')
        movie_action = Movie.objects.filter(genre_ids = action_code).exclude(id__in=user_movies_id).order_by('vote_average')[:10]

        print(movie_action)

        