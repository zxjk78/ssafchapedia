from django.urls import path 
from . import views


urlpatterns = [
    path('<int:movie_pk>/', views.review_movie_list),
    path('<int:movie_pk>/exist/', views.review_exist),
    path('<int:movie_pk>/new/', views.review_create),
    # path('<str:username>/list/', views.review_user_list),
    path('<str:username>/list/', views.UserReviewDetailView.as_view()),
    path('<int:review_pk>/delete/', views.review_delete),
    path('<int:review_pk>/get/', views.review_get),
    path('<int:review_pk>/update/', views.review_update),
]