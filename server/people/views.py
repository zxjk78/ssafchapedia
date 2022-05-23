from django.shortcuts import render,get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Director,Actor,Cast
from movies.serializers.movie import MovieListSerializer
from .serializers.actor import ActorSearchSerializer, ActorDetailSerializer
# swagger
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

@swagger_auto_schema(methods=['GET'], operation_summary='배우검색', operation_description='배우검색')
@api_view(['GET'])
def actor_search(request):
    keyword = request.GET.get('keyword')
    
    actors = Actor.objects.filter(korean_name__contains=keyword)

    serializer = ActorSearchSerializer(actors, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@swagger_auto_schema(methods=['GET'], operation_summary='단일 배우 상세')
@api_view(['GET'])
def actor_detail(request, actor_pk):
    
    actor = get_object_or_404(Actor,pk=actor_pk)

    serializer = ActorDetailSerializer(actor)
    return Response(serializer.data, status=status.HTTP_200_OK)

