from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers.review import ReviewListSerializer, ReviewSerializer
from .models import Review
from movies.models import Movie
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# swagger
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

@swagger_auto_schema(methods=['GET'], request_body=ReviewListSerializer)
@api_view(['GET'])
def review_list(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    reviews = Review.objects.filter(movie=movie)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@swagger_auto_schema(methods=['POST'], request_body=ReviewSerializer)
@api_view(['POST'])
def review_create(request, movie_pk):
    user = request.user
    movie = Movie.objects.get(pk=movie_pk)
    serializer =  ReviewSerializer(data=request.data)
    # 저장 단계 전에 외래키 필드값의 부재에 오류 안나게 하려면 serializer에서 read_only 옵션이나 read_only_fields 작성
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)    
    return Response(serializer.data, status=status.HTTP_201_CREATED)
