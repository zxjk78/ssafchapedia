from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers.review import ReviewListSerializer
from .models import Review
from movies.models import Movie
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# swagger
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@swagger_auto_schema(methods=['POST'], request_body=ReviewListSerializer)
@api_view(['POST'])
def review_create(request, movie_pk):

    user = request.user

    movie = Movie.objects.get(pk=movie_pk)
    serializer =  ReviewListSerializer(data=request.data)
    # 저장 단계 전에 외래키 필드값의 부재에 오류 안나게 하려면 serializer에서 read_only 옵션이나 read_only_fields 작성
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)
    
    return Response(serializer.data, status=status.HTTP_201_CREATED)
