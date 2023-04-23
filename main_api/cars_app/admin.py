from django.contrib import admin
from .models import Car, Owner, ServicePlan

# Register your models here.
admin.site.register(Car)
admin.site.register(Owner)
admin.site.register(ServicePlan)

# now it shows in the admin/ panel and you can add data there