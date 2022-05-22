from django.shortcuts import render
from django.contrib.auth import get_user_model
from yaml import serialize
from .serializers.account import ProfileSerializer
from movies.models import Movie

# DRF
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# swagger
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(methods=['GET',], auto_schema=True)
@api_view(['GET'])
def profile(request, username):

    user = get_user_model().objects.get(username=username)
    
    serializer = ProfileSerializer(user)
    return Response(serializer.data)