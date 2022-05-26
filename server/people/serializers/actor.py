from rest_framework import serializers
from people.models import Actor
from movies.models import Movie
from movies.serializers.movie import MovieListSerializer

# class PeopleListSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Director
#         fields = (
#             'movie', 
#             'actor', 
#             'character',
#         )


class ActorSearchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = (
            'pk', 
            'actor_id', 
            'name', 
            'korean_name',
            'profile_path',
            'movies',
        )

class ActorDetailSerializer(serializers.ModelSerializer):
    
    movies = serializers.SerializerMethodField()
    masterpiece = serializers.SerializerMethodField()
    class Meta:
        model = Actor
        fields = (
            'pk',
            'id',
            'name', 
            'korean_name',
            'profile_path',
            'popularity',
            'movies',
            'masterpiece',
        )

    def get_movies(self, Actor):
        result = []
        movies = Movie.objects.filter(actors=Actor)
        tmp = None
        for movie in movies:
            tmp = dict()
            tmp['pk'] = movie.pk
            tmp['id'] = movie.id
            tmp['poster_path'] = movie.poster_path
            tmp['title'] = movie.title
            tmp['release_date'] = movie.release_date
            tmp['overview'] = movie.overview
            tmp['original_title'] = movie.original_title
            
            result.append(tmp)
        return result

    def get_masterpiece(self, Actor):
        result = []
        movies = Movie.objects.filter(actors=Actor)
        tmp = None
        for movie in movies:
            if movie.vote_average < 7:
                continue
            tmp = dict()
            tmp['pk'] = movie.pk
            tmp['id'] = movie.id
            tmp['poster_path'] = movie.poster_path
            tmp['title'] = movie.title
            tmp['vote_average'] = movie.vote_average
            tmp['release_date'] = movie.release_date


            result.append(tmp)
        return result[:3]


