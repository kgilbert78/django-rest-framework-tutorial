from django.db import models

# Create your models here.
class Forecast(models.Model):
    # auto_now_add=True automatically sets the field to now when the object is first created
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=150)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return "{}".format(self.timestamp)