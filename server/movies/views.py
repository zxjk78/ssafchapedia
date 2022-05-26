from collections import Counter
from django.shortcuts import render,get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Movie, Genre
from people.models import Actor, Cast
from .serializers.movie import MovieListSerializer, MovieSearchSerializer, MovieRecommendSerializer
from people.serializers.actor import ActorDetailSerializer 
# swagger
from drf_yasg.utils import swagger_auto_schema

class ListMovieView(ListAPIView):
    queryset = Movie.objects.all().order_by('-popularity')
    serializer_class = MovieListSerializer


# Create your views here.
# @api_view(['GET'])
# def movie_list(request):
#     #인기순으로 영화 배열
#     if request.method=='GET':
#         movies = Movie.objects.order_by('-popularity')[:50]
#         serializer = MovieListSerializer(movies,many=True)
#         # print(movies)
#         return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail(request,movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def movie_random(request):
    movies = Actor.objects.order_by('?')[:5]
    serializer = ActorDetailSerializer(movies,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_search(request):
    keyword = request.GET.get('keyword')
    
    movies = Movie.objects.filter(title__contains=keyword)

    serializer = MovieSearchSerializer(movies, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

# 이부분 인터셉터로 토큰 들여보내고 나서 테스트해볼것
@authentication_classes([IsAuthenticated])
@swagger_auto_schema(methods=['GET'])
@api_view(['GET'])
def movie_recommend(request):
    user = request.user    
    print(user)
    user_reviewed_movies = list(user.review_set.all().values_list('movie', flat=True)) 

    genre_cnt_list = []
    for movie_no in user_reviewed_movies:
        movie = Movie.objects.get(pk=movie_no)
        genres = movie.genre_ids.all()
        for genre in genres:
            genre_cnt_list.append(genre.pk)
        
    action_code = Counter(genre_cnt_list).most_common(1)[0][0]
    movie_recommend = Movie.objects.filter(genre_ids = action_code).exclude(id__in=user_reviewed_movies).order_by('-vote_average')[:10]


    serializer = MovieRecommendSerializer(movie_recommend, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# @authentication_classes([IsAuthenticated])
# @api_view(['GET'])
# def genres(request):
#     person = get_object_or_404(get_user_model(), username=request.user)
#     # 해당 유저가 어떤 장르를 가장 좋아하는지 체크하기 위한 Json(dict type)
#     person_genre = person.genre_dict

#     if request.method == 'GET':
#         genres = Genre.objects.all()
#         serializer = GenreSerializer(genres, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     else:
#         for data in request.data:
#             # MtoM field 관리
#             person.like_genres.add(data)
#             # Json field 관리
#             person_genre[str(data)] += 1
#         person.save()
#         return Response(status=status.HTTP_201_CREATED)

# 장르 데이터를 기반으로 영화 추천
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def recommend(request):
#     person = get_object_or_404(get_user_model(), username=request.user)
#     person_genre = person.genre_dict

#     max_val = 0
#     best_genre = ''
#     for key, val in person_genre.items():
#         if val >= max_val:
#             max_val = val
#             best_genre = key

#     if max_val != 0:
#         movies = Movie.objects.order_by('?')[:1000]
#         recommend_movies = []
#         cnt = 0
#         for movie in movies:
#             if cnt >= 200:
#                 break
#             if int(best_genre) in [x.id for x in movie.genre_ids.all()]:
#                 recommend_movies.append(movie)
#                 cnt += 1
#                 continue

#         best_genre = get_object_or_404(Genre, pk=int(best_genre))

#         serializer = MovieSerializer(recommend_movies[:50], many=True)
#         return JsonResponse({'data': serializer.data, 'best_genre': best_genre.name }, status=status.HTTP_200_OK)
#     else:
#         return JsonResponse({'best_genre': '아직 데이터가 없는 상태' }, status=status.HTTP_200_OK)
