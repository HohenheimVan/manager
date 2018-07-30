from django.db import models


classes = (("economy class", "economy class"),
           ("business class", "business class"),
           ("first class", "first class"))
hybridOrElectric = (("Hybrid", "Hybrid"),
                    ("Electric", "Electric"),
                    ("None", "None"))


class CarsModel(models.Model):
    producer = models.CharField(max_length=64)
    car_model = models.CharField(max_length=64)
    car_type = models.CharField(max_length=64)

    def __str__(self):
        return self.producer + self.car_model + self.car_type


class NewCarModel(models.Model):
    registration_num = models.CharField(max_length=32)
    max_seats = models.IntegerField()
    year = models.IntegerField()
    car = models.ForeignKey(CarsModel, related_name="car")
    car_class = models.CharField(max_length=32, choices=classes)
    hybrid_or_electric = models.CharField(max_length=32, choices=hybridOrElectric)
