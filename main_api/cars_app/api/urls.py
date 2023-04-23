from django.urls import path, include
from .views import drive, CarViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'car-data', CarViewSet, basename='car-data')
# urlpatterns = router.urls # ok if we didn't also have the function based url below

urlpatterns = [
    path('cars/', drive),
    path('', include(router.urls)),
]