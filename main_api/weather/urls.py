from django.urls import path, include
from .views import WeatherViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'data', WeatherViewSet, basename='weather-data')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]