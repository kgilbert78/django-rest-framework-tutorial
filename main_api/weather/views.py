import requests
from decouple import config
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
    
    def _get_weather_data(self):
        api_key = config("WEATHER_API_KEY")
        url = f"https://api.openweathermap.org/data/2.5/weather?lat=43.041&lon=-76.1489&units=imperial&appid={api_key}" # Syracuse lat & long, imperial means Fahrenheit (default is Kelvin)
        api_request = requests.get(url)

        try:
            api_request.raise_for_status() # tells us if request was successful
            return api_request.json()
        except:
            return None
        
    def save_weather_data(self):
        weather_data = self._get_weather_data()
        if weather_data is not None:
            print(weather_data)
            try:
                weather_obj = Forecast.objects.create(temperature=weather_data["main"]["temp"], description=weather_data["weather"][0]["description"], city=weather_data["name"])
                weather_obj.save()
                print("weather data saved")
            except:
                print("failed to save weather data")
                pass


            # add flag to "python manage.py runserver --noreload" or weather scheduler will launch twice