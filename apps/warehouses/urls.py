from django.urls import include, path
from rest_framework import routers

from .views import (WareHouseItemCreateViewSet, WareHouseItemViewSet,
                    WareHouseViewSet)

router = routers.DefaultRouter()
router.register('', WareHouseViewSet)
router.register('items', WareHouseItemViewSet)
router.register('items', WareHouseItemCreateViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
