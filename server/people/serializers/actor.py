from rest_framework import serializers
from people.models import Actor

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


