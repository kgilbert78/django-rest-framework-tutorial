from django.db import models

# Create your models here.
class Car(models.Model):
    car_brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=50)
    car_year = models.CharField(max_length=4) # will be string
    car_color = models.CharField(max_length=30)

    # then run migrations after creating this ^

    # admin interface displays entries as Car object (1), this makes it display model name
    def __str__(self) -> str:
        return self.car_model