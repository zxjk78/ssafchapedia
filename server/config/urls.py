"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="finalPJT API",
      default_version='v1',
      description="endpoint 상세설명",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="zxjk78@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/', include('allauth.urls')), 
    # 소셜로그인 기능인데 이렇게 하게 되면 api 만으로서 작동하지 않아서 시간 나면 개선 필요

    path('api/v1/member/', include('accounts.urls')),
    path('api/v1/articles/', include('articles.urls')),
    path('api/v1/reviews/',include('reviews.urls')),
    path('api/v1/movies/',include('movies.urls')),
    path('api/v1/people/',include('people.urls')),
    
    

    path('api/v1/accounts/', include('dj_rest_auth.urls')), 
    path('api/v1/accounts/signup/', include('dj_rest_auth.registration.urls')),

    # swagger
    path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

