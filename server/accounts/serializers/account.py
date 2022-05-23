from attr import field
from rest_framework import serializers
from django.contrib.auth import get_user_model

from movies.models import Movie

class ProfileSerializer(serializers.ModelSerializer):

    # Meta에 사용할 fields 위에서 새롭게 fields명과 같은 변수로 필드를 지정하면, class meta의 fields에서
    # 해당 field 로 덮어씌워진다.

    # serializerMethodField는 필드에 들어갈 데이터를 커스터마이징하는데 사용하는 클래스이다.
    # 매개변수로 method_name=을 지정해주지 않으면 get_fieldName 형식으로 method를 정의하고 거기 안에 내가 사용하고 싶은 필드를 적는 형식
    # 그래서 하단에  get_review_set(self, obj) 을 적어준 형식이고 obj는 Meta 클래스에서 정의한 model이 들어감
    
    # review_set = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = (
            'id', 
            'username', 
        )

    # # obj는 Meta에서 정의한 모델 = 여기선 user, reviews = get_user_model().review_set.all()과 마찬가지
    # def get_review_set(self, obj):
    #     data = []
    #     reviews = obj.review_set.all()
    #     review_dict = None
    #     for review in reviews:
    #         review_dict = {}
    #         review_dict['movie'] = review.movie.title
    #         review_dict['poster'] = review.movie.poster_path
    #         review_dict['title'] = review.title
    #         review_dict['content'] = review.content
    #         data.append(review_dict)
    #     return data


class UserReviewSerializer(serializers.ModelSerializer):
    review_set = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'review_set')

    def get_review_set(self, obj):
        data = []
        movies = obj.review_set.all()
        review_dict = None
        for movie in movies:
            review_dict = {}
            review_dict['movie'] = movie.title
            review_dict['poster'] = movie.poster_path
            data.append(review_dict)
        return data

class UserWatchSerializer(serializers.ModelSerializer):
    watch = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'watch')

    def get_watch(self, obj):
        data = []
        movies = obj.watch.all()
        watch_dict = None
        for movie in movies:
            like_dict = {}
            like_dict['movie'] = movie.title
            like_dict['poster'] = movie.poster_path
            data.append(watch_dict)
        return data

class UserWishSerializer(serializers.ModelSerializer):

    wish = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'wish')

    def get_wish(self, obj):
        data = []
        movies = obj.wish.all()
        wish_dict = None
        for movie in movies:
            like_dict = {}
            like_dict['movie'] = movie.title
            like_dict['poster'] = movie.poster_path
            data.append(wish_dict)
        return data

