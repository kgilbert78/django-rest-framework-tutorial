from django.db import models

# Create your models here.
class Cars2(models.Model):
    car_brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=50)
    car_year = models.CharField(max_length=4) # will be string
    car_color = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.car_brand + ' ' + self.car_model