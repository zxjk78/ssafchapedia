from rest_framework import serializers
from ..models import Review

class ReviewListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = (
            'user', 
            'movie', 
            'content', 
            'directing',
            'music',
            'story',
            'acting',
            'art',
        )


