from django.urls import path, include
from .views import PostViewSet, PostRatingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'post-ratings', PostRatingViewSet, basename='post-ratings')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]