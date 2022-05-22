from nbformat import read
from rest_framework import serializers
from ..models import Genre, Movie
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

# class MovieSearchSerializer(serializers.ModelSerializer): // 배열로 있는 genre_ids를 똑같이 배열로 뱉고 싶으면 고민좀 더해보기
    
#     genres = serializers.SerializerMethodField()


#     class Meta:
#         model = Movie
#         fields = (
#             'title', 
#             'genres',
#             'vote_average',
#             'release_date',
#             'poster_path',
#         )
    
#     def get_genres(self, obj):
#         print('serializer 입니다.')
#         print(obj)
#         genres =  obj.objects.filter('genre__genre' in obj.genre_ids)
        
#         return genres

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
    