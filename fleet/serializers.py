from .models import NewCarModel, CarsModel
from rest_framework import serializers


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsModel
        fields = ("id", "producer", "car_model", "car_type")


class NewCarSerializer(serializers.ModelSerializer):
    # car = CarsSerializer()
    class Meta:
        model = NewCarModel
        fields = ("id", "registration_num", "max_seats", "year", "car", "car_class", "hybrid_or_electric")
