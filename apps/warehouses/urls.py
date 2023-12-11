from django.urls import path, include
from .views import (
    WareHouseViewSet,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("", WareHouseViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
