from django.urls import path, include
from .views import NotificationViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register("", NotificationViewSet)


urlpatterns = [
    path("", include(router.urls), name="notifications"),
]
