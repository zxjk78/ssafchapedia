from nbformat import read
from rest_framework import serializers
from ..models import Movie
from people.models import Director, Cast, Actor

class MovieListSerializer(serializers.ModelSerializer):
    
    class DirectorSerializer(serializers.ModelSerializer):
        class Meta:
            model = Director
            fields = ('name', 'profile_path')

    class CastSerializer(serializers.ModelSerializer):
        class ActorSerializer(serializers.ModelSerializer):
            class Meta:
                model = Actor
                fields = ('name', 'popularity', 'profile_path')
        
        actor = ActorSerializer(read_only=True)
        class Meta:
            model = Cast
            fields = ('actor', 'profile_path')

    director = DirectorSerializer(read_only=True)
    cast_set = CastSerializer(read_only = True)

    class Meta:
        model = Movie
        fields = (
            'title', 
            'overview', 
            'runtime', 
            'vote_arerage',
            'vote_count',
            'release_date',
            'poster_path',
            'vote_arerage',
            'director',
            'cast_set',
        )