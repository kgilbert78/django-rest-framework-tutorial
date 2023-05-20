from rest_framework import serializers
from .models import Driver

best_time = 30 # to make things simple in lesson. should be coming from a database.

class DriverSerializer(serializers.ModelSerializer):
    best_record = serializers.SerializerMethodField('_get_best_record')

    def _get_best_record(self, driver_obj):

        global best_time

        # get round finishing time for each driver from model and assign to same name variable here
        round_finishing_time = getattr(driver_obj, 'round_finishing_time')

        if round_finishing_time and round_finishing_time < best_time:
            best_time = round_finishing_time
            return best_time
        else:
            return best_time

    class Meta:
        model = Driver
        fields = ['id', 'first_name', 'last_name', 'car_brand', 'round_finishing_time', 'best_record']

        # best_record returns in get request automatically for all drivers, updating in order by id, so each id's time is compared to those before it in the json list. 
        # doesn't save to database so if you stop the server it resets back to 30.
        # can do this with any data from the Driver object (or any object from your model).