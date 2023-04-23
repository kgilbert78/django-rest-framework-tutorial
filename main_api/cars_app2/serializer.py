from rest_framework import serializers
from .models import Cars2

class Cars2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cars2
        fields = ['id', 'car_brand', 'car_model', 'car_year', 'car_color']