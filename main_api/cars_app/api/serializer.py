from rest_framework import serializers
from ..models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'owner', 'service_plan', 'car_brand', 'car_model', 'car_year', 'car_color']
        depth = 1 # nests foreignkey's model data in json response, instead of just foreignkey id