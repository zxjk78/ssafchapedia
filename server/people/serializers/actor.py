from rest_framework import serializers
from people.models import Actor
from movies.models import Movie

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
    
    # movies = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = (
            'actor_id', 
            'name', 
            'korean_name',
            'profile_path',
            'movies',
        )

    # def get_movies(self, Actor):
    #     result = []
    #     # movies = Movie.objects.filter(actors=Actor)
    #     movies= None
    #     tmp = None
    #     for movie in movies:
    #         tmp = dict()
    #         tmp['id'] = movie.id
    #         tmp['poster_path'] = movie.poster_path
    #         tmp['title'] = movie.title

    #         result.push(tmp)
    #     return result


