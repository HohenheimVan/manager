import csv
from django.shortcuts import render
from django.views.generic.base import View
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from fleet.serializers import NewCarSerializer, CarsSerializer
from fleet.models import CarsModel, NewCarModel


# funkcja dodająca dane z pliku csv do bazy
def add_cars_csv():
    with open('fleet/cars.csv', newline='') as f:
        reader = csv.reader(f)
        x = 0
        for row in reader:
            try:
                producer = row[0]
                model = row[1]
                car_type = row[2]
                # pomijam pierwszy rząd
                if x > 0:
                    CarsModel.objects.create(producer=producer, car_model=model, car_type=car_type)
                x += 1
            except IndexError:
                continue


class Add(View):
    def get(self, request):
        return render(request, "addCars.html")

    def post(self, request):
        add_cars_csv()
        return render(request, "addCars.html", {"message": "dodano"})


class NewCarListView(ListCreateAPIView):
    queryset = NewCarModel.objects.all()
    serializer_class = NewCarSerializer


class NewCarDetailView(RetrieveUpdateDestroyAPIView):
    queryset = NewCarModel.objects.all()
    serializer_class = NewCarSerializer


class CarsListView(ListCreateAPIView):
    queryset = CarsModel.objects.all()
    serializer_class = CarsSerializer


class CarsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CarsModel.objects.all()
    serializer_class = CarsSerializer
