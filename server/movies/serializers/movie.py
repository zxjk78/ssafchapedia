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
            fields = ('actor', 'movie','character')

    director = DirectorSerializer(read_only=True)
    cast_set = CastSerializer(read_only = True)

    class Meta:
        model = Movie
        fields = (
            'title', 
            'overview', 
            'genre_ids',
            'adult',
            'vote_average',
            'vote_count',
            'release_date',
            'poster_path',
            'original_title',
            'original_language',
            'popularity',
            'director',
            'cast_set',
        )