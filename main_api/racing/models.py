from django.db import models

# Create your models here.
class Driver(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    car_brand = models.CharField(max_length=50)
    round_finishing_time = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.last_name + ', ' + self.first_name