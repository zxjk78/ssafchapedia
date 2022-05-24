from django.urls import path 
from . import views

urlpatterns = [
    # path('', views.movie_list),
<<<<<<< HEAD
    path('', views.ListMovieView.as_view()),
=======
    path('',views.ListMovieView.as_view()),
>>>>>>> a1f66aa4e08ea43562b82fdc65c36bf38d166c2f
    path('movie/<int:movie_pk>/',views.movie_detail),
    path('random/',views.movie_random),
    path('search/',views.movie_search),
    path('recommend/',views.movie_recommend),
]