from django.urls import path, include
from .views import ProductViewSet, ProductImageCreateAPIView, ProductImageDestroyAPIView

from rest_framework import routers

router = routers.DefaultRouter()
router.register("", ProductViewSet)


urlpatterns = [
    path("", include(router.urls), name="products"),
    path("<int:product_id>/images/",
         ProductImageCreateAPIView.as_view(), name="product_image"),
    path("images/<int:pk>/",
         ProductImageDestroyAPIView.as_view(), name="delete image")

]
