from django.urls import path, include
from .views import (
    CustomerViewSet,
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("", CustomerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
