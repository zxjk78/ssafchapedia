from django.urls import path 
from . import views


urlpatterns = [
    path('<int:movie_pk>/', views.review_list),
    path('<int:movie_pk>/new/', views.review_create),
    path('<int:movie_pk>/new/detail', views.review_update_detail),
]