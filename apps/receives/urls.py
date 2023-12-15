from django.urls import path, include
from .views import (
    ReceiveViewSet,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("", ReceiveViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
