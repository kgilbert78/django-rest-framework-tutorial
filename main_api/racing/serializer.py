from rest_framework import serializers
from .models import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'first_name', 'last_name', 'car_brand', 'round_finishing_time']