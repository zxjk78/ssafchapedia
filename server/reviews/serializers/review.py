from rest_framework import serializers
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
