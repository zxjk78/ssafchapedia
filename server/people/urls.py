from django.urls import path 
from . import views

urlpatterns = [
    path('', views.people),
    path('search/',views.actor_search),
]