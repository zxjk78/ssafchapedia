from django.urls import path 
from . import views

urlpatterns = [
    path('search/',views.actor_search),

    path('<int:actor_pk>/',views.actor_detail),

]