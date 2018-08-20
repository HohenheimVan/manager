import csv

from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.base import View
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

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


class NewCarListView(ListCreateAPIView):
    queryset = NewCarModel.objects.all()
    serializer_class = NewCarSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NewCarDetailView(RetrieveUpdateDestroyAPIView):
    queryset = NewCarModel.objects.all()
    serializer_class = NewCarSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class CarsListView(ListCreateAPIView):
    queryset = CarsModel.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CarsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CarsModel.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'cars': reverse('cars-list', request=request, format=format),
        'new_car': reverse('new-car-list', request=request, format=format)
    })
