from django.urls import path, include
from .views import (
    ReceiveItemViewSet,
    ReceiveViewSet,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("receives", ReceiveViewSet,basename='receive')
router.register('receives-items', ReceiveItemViewSet,basename='receive_items')
urlpatterns = [
    path("", include(router.urls)),
]
