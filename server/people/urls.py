from django.urls import path 
from . import views

urlpatterns = [
<<<<<<< HEAD
    # path('', views.people),
    
=======
    path('', views.people),
    path('search/',views.actor_search),
>>>>>>> feat/review-front
]