from django.urls import path 
from . import views

app_name='reviews'
urlpatterns = [
    path('', views.review_list),
    path('new/', views.review_create),
]