from django.apps import AppConfig


class WeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather'

    def ready(self) -> None:
        print("Starting weather scheduler...")
        from .scheduler import updater
        updater.start_2min_weather_updates()
        