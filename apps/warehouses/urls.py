from rest_framework import routers
from django.urls import path, include
from .views import WareHouseViewSet, WareHouseItemViewSet

router = routers.DefaultRouter()
router.register('', WareHouseViewSet)
router.register('items', WareHouseItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
