from apscheduler.schedulers.background import BackgroundScheduler
from ..views import WeatherViewSet

def start_2min_weather_updates():
    scheduler = BackgroundScheduler()
    scheduler.add_job(WeatherViewSet().save_weather_data, "interval", minutes=2, id="US_13202_weather_001", replace_existing=True)
    # replace_existing = True ensures that it doesn't create a new copy every time the program starts.
    # interval of 2 minutes, see docs for more: https://apscheduler.readthedocs.io/en/master/api.html
    scheduler.start()