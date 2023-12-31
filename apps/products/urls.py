from django.urls import path, include
from .views import ProductViewSet, ProductImageViewset

from rest_framework import routers

router = routers.DefaultRouter()
router.register("", ProductViewSet)
router.register("images", ProductImageViewset)


urlpatterns = [
    path("", include(router.urls), name="products"),
]
