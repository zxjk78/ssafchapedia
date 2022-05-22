from rest_framework import serializers
from ..models import *

class PeopleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Director
        fields = (
            'movie', 
            'actor', 
            'character',
        )