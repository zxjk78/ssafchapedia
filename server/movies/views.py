from django.shortcuts import render,get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie,Genre
from .serializers.movie import MovieListSerializer

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    #인기순으로 영화 배열
    if request.method=='GET':
        movies = Movie.objects.order_by('-popularity')[:50]
        serializer = MovieListSerializer(movies,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

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