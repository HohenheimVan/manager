import csv

from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.base import View
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from fleet.serializers import NewCarSerializer, CarsSerializer, UserSerializer
from fleet.models import CarsModel, NewCarModel
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

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


class NewCarViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = NewCarModel.objects.all()
    serializer_class = NewCarSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class CarsViewSet(ModelViewSet):
    queryset = CarsModel.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
