from django.urls import path, include
from .views import AlbumViewSet, TrackViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'album', AlbumViewSet, basename='album')
router.register(r'track', TrackViewSet, basename='track')

urlpatterns = [
    path('', include(router.urls))
]