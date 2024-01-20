from django.urls import include, path
from rest_framework import routers

from .views import WareHouseItemViewSet

router = routers.DefaultRouter()


router.register('', WareHouseItemViewSet, basename='warehouseitem')

urlpatterns = [
    path('', include(router.urls)),
]
