from django.urls import path, include
from .views import OrderViewSet, OrderImageViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register("", OrderViewSet)
router.register("images", OrderImageViewSet)

urlpatterns = [
    path("", include(router.urls), name="orders"),
]
