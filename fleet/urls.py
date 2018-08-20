from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from fleet.views import NewCarListView, NewCarDetailView, CarsListView, CarsDetailView, UserDetail, UserList, api_root

urlpatterns = [

    url(r'^api/(?P<pk>\d+)$', NewCarDetailView.as_view(), name="new-car-detail"),
    url(r'^api/$', NewCarListView.as_view(), name="new-car-list"),
    url(r'^api/cars/$', CarsListView.as_view(), name="cars-list"),
    url(r'^api/cars/(?P<pk>\d+)$', CarsDetailView.as_view(), name="cars-detail"),
    url(r'^api/users/$', UserList.as_view(), name="user-list"),
    url(r'^api/users/(?P<pk>\d+)$', UserDetail.as_view(), name="user-detail"),
    url(r'^$', api_root),

]

