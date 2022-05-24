from rest_framework import serializers

from movies.models import Movie
from ..models import Review

class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = (
            'user', 
            'movie', 
            'title', 
            'content', 
            'directing',
            'music',
            'story',
            'acting',
            'art',
        )

        read_only_fields = ['user', 'movie', ]
        
class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = (
            'user', 
            'movie', 
            'title', 
            'content', 
            'directing',
            'music',
            'story',
            'acting',
            'art',
        )

        read_only_fields = ['user', 'movie', ]


class ReviewDetailSerializer(serializers.ModelSerializer):
    class TmpMovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('pk','poster_path', 'title', 'release_date', 'vote_average')
    
    movie = TmpMovieSerializer(read_only=True)

    class Meta:
        model = Review
        fields = (
            'user', 
            'movie', 
            'title', 
            'content', 
            'directing',
            'music',
            'story',
            'acting',
            'art',
        )

        read_only_fields = ['user', 'movie', ]
    
