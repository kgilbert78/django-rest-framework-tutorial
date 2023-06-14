"""
URL configuration for main_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import Index

urlpatterns = [
    path('', Index),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('cars-app/', include('cars_app.api.urls')),
    path('cars-app2/', include('cars_app2.urls')),
    # include means put urls listed in cars-app2 urls.py after this 'cars-app2/'
    path('blog/', include('blog.urls')),
    path('school/', include('school.urls')),
    path('racing/', include('racing.urls')),
    path('weather/', include('weather.urls')),
    path('music/', include('albums.urls'))
]

# POST request to api/token/ with body:
# {
#     "username": "",
#     "password": ""
# }
# returns json with "refresh" and "access"
#
# GET request to blog/posts/ with:
# Headers:
# Authorization: Bearer access-token-here
# Body:
# {
#     "username": "",
#     "password": "",
#     "refresh": ""
# }