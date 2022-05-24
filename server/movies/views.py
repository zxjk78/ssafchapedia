from collections import Counter
from django.shortcuts import render,get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticated
<<<<<<< HEAD
=======

>>>>>>> a1f66aa4e08ea43562b82fdc65c36bf38d166c2f
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Movie, Genre
from people.models import Actor, Cast
from .serializers.movie import MovieListSerializer, MovieSearchSerializer, MovieRecommendSerializer
# swagger
from drf_yasg.utils import swagger_auto_schema

class ListMovieView(ListAPIView):
    queryset = Movie.objects.all().order_by('-popularity')
    serializer_class = MovieListSerializer
<<<<<<< HEAD

=======
>>>>>>> a1f66aa4e08ea43562b82fdc65c36bf38d166c2f
# Create your views here.
# @api_view(['GET'])
# def movie_list(request):
#     #인기순으로 영화 배열
#     if request.method=='GET':
#         movies = Movie.objects.order_by('-popularity')[:50]
#         serializer = MovieListSerializer(movies,many=True)
#         # print(movies)
#         return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail(request,movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def movie_random(request):
    movies = Movie.objects.order_by('?')[:50]
    serializer = MovieListSerializer(movies,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_search(request):
    keyword = request.GET.get('keyword')
    
    movies = Movie.objects.filter(title__contains=keyword)

    serializer = MovieSearchSerializer(movies, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

# 이부분 인터셉터로 토큰 들여보내고 나서 테스트해볼것
@authentication_classes([IsAuthenticated])
@swagger_auto_schema(methods=['GET'])
@api_view(['GET'])
def movie_recommend(request):
    user = request.user    
    print(user)
    user_reviewed_movies = list(user.review_set.all().values_list('movie', flat=True)) 

    genre_cnt_list = []
    for movie_no in user_reviewed_movies:
        movie = Movie.objects.get(pk=movie_no)
        genres = movie.genre_ids.all()
        for genre in genres:
            genre_cnt_list.append(genre.pk)
        
    action_code = Counter(genre_cnt_list).most_common(1)[0][0]
    movie_recommend = Movie.objects.filter(genre_ids = action_code).exclude(id__in=user_reviewed_movies).order_by('-vote_average')[:10]


    serializer = MovieRecommendSerializer(movie_recommend, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)