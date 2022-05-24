from django.shortcuts import render,get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie, Genre
from people.models import Actor, Cast
from .serializers.movie import MovieListSerializer, MovieSearchSerializer

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    #인기순으로 영화 배열
    if request.method=='GET':
        movies = Movie.objects.order_by('-popularity')[:50]
        serializer = MovieListSerializer(movies,many=True)
        print(movies)
        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail(request,movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)

# #영화 출연 배우 목록 조회
# @api_view(['GET'])
# def movie_cast(request,movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     #url = f'https://api.themoviedb.org/3/movie/{movie_pk}/credits?api_key=b083ba699306944d1930bb483794ede6&language=ko-KR'
#     # print(request.get(url).json())
#     serializer = MovieListSerializer(movie)
#     return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_random(request):
    movies = Movie.objects.order_by('?')[:50]
    serializer = MovieListSerializer(movies,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

# 요청이 가면 영화, 배우 둘 다 한번에 json으로 처리해야 되는지, 다른 endpoint에 요청을 보내서 처리해야되는지?
@api_view(['GET'])
def movie_search(request):
    keyword = request.GET.get('keyword')
    
    movies = Movie.objects.filter(title__contains=keyword)

    serializer = MovieSearchSerializer(movies, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
