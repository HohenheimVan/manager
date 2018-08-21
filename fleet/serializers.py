from .models import NewCarModel, CarsModel
from rest_framework import serializers
from django.contrib.auth.models import User


class CarsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = CarsModel
        fields = ("id", "producer", "car_model", "car_type", "owner")


class NewCarSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    car = serializers.HyperlinkedRelatedField(view_name="cars-detail", queryset=CarsModel.objects.all())
    class Meta:
        model = NewCarModel
        fields = ("id", "registration_num", "max_seats", "year", "car_class", "hybrid_or_electric", 'car', "owner")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    new_car_model = serializers.HyperlinkedRelatedField(many=True, view_name="new-car-detail",  read_only=True)
    cars_model = serializers.HyperlinkedRelatedField(many=True, view_name="cars-detail", read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'cars_model', 'new_car_model')
