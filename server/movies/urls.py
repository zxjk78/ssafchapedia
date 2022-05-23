from django.urls import path 
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('movie/<int:movie_pk>/',views.movie_detail),
    path('random/',views.movie_random),
    path('search/',views.movie_search),
]