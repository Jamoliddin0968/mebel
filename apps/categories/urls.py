from django.urls import path, include
from .views import CategoryViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register("", CategoryViewSet)


urlpatterns = [
    path("", include(router.urls), name="categories"),

]
