from rest_framework import serializers
from people.models import Actor
from movies.models import Movie
from server.movies.serializers.movie import MovieListSerializer

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
            'id', 
            'name', 
            'korean_name',
            'profile_path',
            'movies',
            'masterpiece',
        )

    def get_movies(self, Actor):
        result = []
        movies = Movie.objects.filter(actors=Actor)
        tmp = None
        for movie in movies:
            tmp = dict()
            tmp['id'] = movie.id
            tmp['poster_path'] = movie.poster_path
            tmp['title'] = movie.title
            tmp['release_date'] = movie.release_date

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
            tmp['id'] = movie.id
            tmp['poster_path'] = movie.poster_path
            tmp['title'] = movie.title
            tmp['vote_average'] = movie.vote_average
            tmp['release_date'] = movie.release_date


            result.append(tmp)
        return result


