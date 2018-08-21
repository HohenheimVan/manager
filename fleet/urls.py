from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from fleet.views import NewCarViewSet, CarsViewSet, UserViewSet

cars_detail = CarsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
new_car_detail = NewCarViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
router = DefaultRouter()
router.register(r'new-car', NewCarViewSet)
router.register(r'cars', CarsViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/cars/(?P<pk>\d+)$', cars_detail, name="cars-detail"),
    url(r'^api/new-car/(?P<pk>\d+)$', new_car_detail, name="new-car-detail"),

]
