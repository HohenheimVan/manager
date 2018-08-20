from django.db import models


classes = (("economy class", "economy class"),
           ("business class", "business class"),
           ("first class", "first class"))
hybrid_or_electric = (("Hybrid", "Hybrid"),
                    ("Electric", "Electric"),
                    ("None", "None"))


class CarsModel(models.Model):
    owner = models.ForeignKey('auth.User', related_name='cars_model', on_delete=models.CASCADE)
    producer = models.CharField(max_length=64)
    car_model = models.CharField(max_length=64)
    car_type = models.CharField(max_length=64)

    def __str__(self):
        return self.producer + self.car_model + self.car_type


class NewCarModel(models.Model):
    owner = models.ForeignKey('auth.User', related_name='new_car_model', on_delete=models.CASCADE)
    registration_num = models.CharField(max_length=32)
    max_seats = models.IntegerField()
    year = models.IntegerField()
    car = models.ForeignKey(CarsModel, related_name="car")
    car_class = models.CharField(max_length=32, choices=classes)
    hybrid_or_electric = models.CharField(max_length=32, choices=hybrid_or_electric)
