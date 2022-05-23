from django.shortcuts import render
from django.contrib.auth import get_user_model
from yaml import serialize
from .serializers.account import ProfileSerializer, UserReviewSerializer, UserWatchSerializer, UserWishSerializer
from movies.models import Movie

# DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# swagger
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(methods=['GET',])
@api_view(['GET'])
def profile(request, username):
    user = get_user_model().objects.get(username=username)    
    serializer = ProfileSerializer(user)
    return Response(serializer.data)

@swagger_auto_schema(methods=['GET',])
@api_view(['GET'])
def user_wish(request, username):

    user = get_user_model().objects.get(username=username)
    
    serializer = UserWishSerializer(user)
    return Response(serializer.data)

@swagger_auto_schema(methods=['GET',])
@api_view(['GET'])
def user_watch(request, username):

    user = get_user_model().objects.get(username=username)
    
    serializer = UserWatchSerializer(user)
    return Response(serializer.data)

@swagger_auto_schema(methods=['GET',])
@api_view(['GET'])
def user_review(request, username):
    user = get_user_model().objects.get(username=username)    
    serializer = UserReviewSerializer(user)
    return Response(serializer.data)