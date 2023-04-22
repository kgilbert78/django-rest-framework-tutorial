from django.urls import path
from .views import drive

urlpatterns = [
    path('cars/', drive)
]