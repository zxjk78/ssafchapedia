from django.urls import path 
from . import views
app_name='movie'
urlpatterns = [
    # path('', views.movie_list),

    path('movie/',views.ListMovieView.as_view()),

    path('movie/<int:movie_pk>/',views.movie_detail),
    path('random/',views.movie_random),
    path('search/',views.movie_search),
    path('recommend/',views.movie_recommend),
]