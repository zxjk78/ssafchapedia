from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from .serializers.review import ReviewListSerializer, ReviewSerializer, ReviewDetailSerializer
from .models import Review
from movies.models import Movie
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from rest_framework import status
# swagger
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
@swagger_auto_schema(methods=['GET'])
class UserReviewDetailView(ListAPIView):
    # 어디에 클래스를 정의하건 상관없고, 중요한건 이렇게 상속해서 원하는대로
    # 작성한 Pagination class를 아래 pagination_class에서 상속하는 것 
    class CustomPageNumberPagination(PageNumberPagination):
        page_size = 5

    serializer_class = ReviewDetailSerializer
    lookup_url_kwarg = 'username'
    pagination_class = CustomPageNumberPagination
    def get_queryset(self):
        username = self.kwargs.get(self.lookup_url_kwarg)
        user = get_object_or_404(get_user_model(), username=username)
        reviews = Review.objects.filter(user=user).order_by('-pk')
        return reviews


@swagger_auto_schema(methods=['GET'], operation_summary='리뷰, 영화 리스트')
@api_view(['GET'])
def review_movie_list(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    reviews = Review.objects.filter(movie=movie)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)

@authentication_classes([IsAuthenticated])
@swagger_auto_schema(methods=['GET',], operation_summary='해당 영화에 대한 리뷰 작성 T/F 반환')
@api_view(['GET'])
def review_exist(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    isExist = Review.objects.filter(user=user, movie=movie).exists()
    data = {
        'result': False
    }
    if isExist:
        data['result'] = True
    return JsonResponse(data)

@authentication_classes([IsAuthenticated])
@swagger_auto_schema(methods=['POST','PUT'], request_body=ReviewSerializer,  operation_summary='리뷰 작성')
@api_view(['POST','PUT'])
def review_create(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)  

    if request.method == 'POST':
        # 저장 단계 전에 외래키 필드값의 부재에 오류 안나게 하려면 serializer에서 read_only 옵션이나 read_only_fields 작성
        serializer =  ReviewSerializer(data=request.data)   
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)    
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'PUT':
        # 이전에는 내용에 대한 저장을 안했기 때문에, 리뷰 객체를 불러와서 update해야한다.
        review = get_object_or_404(Review, user=user, movie=movie)
        serializer = ReviewSerializer(review, data= request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()    
        return Response(serializer.data, status=status.HTTP_200_OK)

@swagger_auto_schema(methods=['GET'], )
@api_view(['GET'])
def review_user_list(request, username):
    user = get_user_model().objects.get(username=username)
    review = Review.objects.filter(user=user).order_by('-pk')[0]
    serializer = ReviewDetailSerializer(review)
    return Response(serializer.data)

@authentication_classes([IsAuthenticated])
@api_view(['DELETE'])
def review_delete(request, review_pk):
    print(review_pk)
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()    
    return Response({'msg': f'{review_pk}가 성공적으로 삭제'})

@authentication_classes([IsAuthenticated])
@api_view(['GET'])
def review_get(request, review_pk):
    
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)

@authentication_classes([IsAuthenticated])
@api_view(['PUT'])
def review_update(request, review_pk):
    
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(review, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
            serializer.save()    
    return Response(serializer.data, status=status.HTTP_200_OK)
    

