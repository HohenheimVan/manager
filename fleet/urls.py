from django.conf.urls import url

from fleet.views import NewCarListView, NewCarDetailView, CarsListView, CarsDetailView

urlpatterns = [

    url(r'^api/(?P<pk>\d+)$', NewCarDetailView.as_view(), name="new_car_details"),
    url(r'^api/$', NewCarListView.as_view(), name="new_car"),
    url(r'^api/cars/$', CarsListView.as_view(), name="cars"),
    url(r'^api/cars/(?P<pk>\d+)$', CarsDetailView.as_view(), name="cars_details"),

]
