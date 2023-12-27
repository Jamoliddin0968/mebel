from django.urls import path, include
from .views import (
    ReceiveItemViewSet,
    ReceiveViewSet,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("", ReceiveViewSet)
router.register('items', ReceiveItemViewSet)
urlpatterns = [
    path("", include(router.urls)),
]
