from django.apps import AppConfig


class WeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather'

    # # uncomment to make calls to weather api every 2 minutes
    # def ready(self) -> None:
    #     print("Starting weather scheduler...")
    #     from .scheduler import updater
    #     updater.start_2min_weather_updates()
        