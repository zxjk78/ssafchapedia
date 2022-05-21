from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers.review import ReviewListSerializer
from .models import Review
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET'])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def review_create(request, movie_pk):
    user = request.user
    serializer =  ReviewListSerializer(request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie_pk, user=user.pk)
    
    return Response(serializer.data, status=status.HTTP_201_CREATED)
