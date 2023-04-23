from django.db import models

# Create your models here.
    
class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10) # no - or ()
    # better option to explore: https://pypi.org/project/django-phonenumber-field/
    email = models.EmailField(max_length=50)    

    def __str__(self) -> str:
        return self.last_name + ', ' + self.first_name
    
class ServicePlan(models.Model):
    plan_name = models.CharField(max_length=20)
    warranty_num_years = models.PositiveIntegerField(default=1)
    finance_plan = models.CharField(max_length=20, default="unavailable")

    def __str__(self) -> str:
        return self.plan_name
    
class Car(models.Model):
    car_brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=50)
    car_year = models.CharField(max_length=4) # will be string
    car_color = models.CharField(max_length=30)

    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)
    # on_delete sets what happens to the owner if the car is deleted.
    # other options: https://docs.djangoproject.com/en/4.2/ref/models/fields/#django.db.models.ForeignKey.on_delete

    service_plan = models.ForeignKey(ServicePlan, on_delete=models.SET_NULL, null=True)

    # then run migrations after adding new model & ^ ForeignKey

    # admin interface displays entries as Car object (1), this makes it display model name
    def __str__(self) -> str:
        return self.car_brand + ' ' + self.car_model