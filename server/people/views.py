from django.shortcuts import render,get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Director,Actor,Cast
from movies.serializers.movie import MovieListSerializer

# Create your views here.
# @api_view(['GET'])
# def people(request):
#     if request.method=='GET':
#         movies = Cast.objects.order_by('-popularity')[:50]
#         serializer = MovieListSerializer.CastSerializer(movies,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

# @api_view(['GET'])
# def movie_detail(request,movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     serializer = MovieListSerializer(movie)
#     return Response(serializer.data)