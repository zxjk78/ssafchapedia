from django.urls import path 
from . import views


urlpatterns = [

    path('<str:username>/wish/', views.user_wish),
    path('<str:username>/watch/', views.user_watch),
    path('<str:username>/review/', views.user_review),
    path('<str:username>/profile/', views.profile),
]