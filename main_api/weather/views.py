import requests
from rest_framework import viewsets
from django.http import HttpResponse
from weather.models import Forecast
from .serializer import ForecastSerializer


# Create your views here.
class WeatherViewSet(viewsets.ModelViewSet):
    serializer_class = ForecastSerializer

    def get_queryset(self):
        data = Forecast.objects.all()
        return data