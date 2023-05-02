# from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CoursesViewSet, StudentsViewSet

router = DefaultRouter()
router.register(r'students', StudentsViewSet, basename='students')
router.register(r'courses', CoursesViewSet, basename='courses')
urlpatterns = router.urls

# urlpatterns = [
#     path('', include.router.urls)
# ]