import imp
from django.shortcuts import render
from django.contrib.auth import get_user_model
from uritemplate import partial
from .serializers.review import ReviewListSerializer, ReviewSerializer
from .models import Review
from movies.models import Movie
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
# swagger
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

@swagger_auto_schema(methods=['GET'])
@api_view(['GET'])
def review_list(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    reviews = Review.objects.filter(movie=movie)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@authentication_classes([IsAuthenticated])
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


@authentication_classes([IsAuthenticated])
@swagger_auto_schema(methods=['PUT'], request_body=ReviewSerializer)
@api_view(['PUT'])
def review_update_detail(request, movie_pk):
    user = request.user
    movie = Movie.objects.get(pk=movie_pk)
    # 이전에는 내용에 대한 저장을 안했기 때문에, 리뷰 객체를 불러와서 update해야한다.
    review = Review.objects.get(user=user, movie=movie) # reviewPK를 페이지에서 던져준다음 받던가, 아니면 user, movie로 조회하던가
    serializer =  ReviewSerializer(review, data=request.data, partial=True)
    # 저장 단계 전에 외래키 필드값의 부재에 오류 안나게 하려면 serializer에서 read_only 옵션이나 read_only_fields 작성
    if serializer.is_valid(raise_exception=True):
        serializer.save()    
    return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)

