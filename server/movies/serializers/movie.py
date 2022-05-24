from nbformat import read
from rest_framework import serializers
from ..models import Genre, Movie
from people.models import  Cast, Actor

# class CastSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cast
#         fields=('id','actor','movie',)
class MovieListSerializer(serializers.ModelSerializer):
    
    

    class CastSerializer(serializers.ModelSerializer):
        class ActorSerializer(serializers.ModelSerializer):
            class Meta:
                model = Actor
                fields = ('name', 'popularity', 'profile_path')
                
        actor = ActorSerializer(read_only=True)
        
        class Meta:
            model = Cast
            # fields = ('actor', 'movie','character')

            fields = ('actor',)
    cast_set = CastSerializer(read_only = True)

    class Meta:
        model = Movie
        fields = (
            'pk',
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
            'cast_set',
        )



class MovieSearchSerializer(serializers.ModelSerializer):
    
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('genre', )
    

    genre_ids = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            'title', 
            'genre_ids',
            'vote_average',
            'release_date',
            'poster_path',
        )

class MovieRecommendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'title',
            'vote_average',
            'release_date',
            'poster_path',
        )
