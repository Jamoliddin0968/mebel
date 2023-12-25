from django.urls import path, include
from .views import OrderViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register("", OrderViewSet)


urlpatterns = [
    path("", include(router.urls), name="orders"),
]
